import math
import os
from functools import wraps

from PIL import Image
from pyrogram import errors, raw
from pyrogram.types import InputStickerSetShortName, InputDocument, DocumentAttributeFilename

STICKER_DIMENSIONS = (512, 512)


async def resize_file_to_sticker_size(file_path):
    im = Image.open(file_path)
    if im.size < STICKER_DIMENSIONS:
        size1, size2 = im.size
        if im.width > im.height:
            scale = STICKER_DIMENSIONS[0] / size1
            size1new = STICKER_DIMENSIONS[0]
            size2new = size2 * scale
        else:
            scale = STICKER_DIMENSIONS[1] / size2
            size1new = size1 * scale
            size2new = STICKER_DIMENSIONS[1]
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(STICKER_DIMENSIONS)
    try:
        os.remove(file_path)
        file_path = f"{file_path}.png"
        return file_path
    finally:
        im.save(file_path)


async def upload_document(client, file_path, chat_id):
    media = await client.invoke(
        raw.functions.messages.UploadMedia(
            peer=await client.resolve_peer(chat_id),
            media=raw.types.InputMediaUploadedDocument(
                mime_type=client.guess_mime_type(file_path) or "application/zip",
                file=await client.save_file(file_path),
                attributes=[
                    DocumentAttributeFilename(
                        file_name=os.path.basename(file_path)
                    )
                ],
            ),
        )
    )
    return InputDocument(
        id=media.document.id,
        access_hash=media.document.access_hash,
        file_reference=media.document.file_reference,
    )


async def get_document_from_file_id(file_id):
    decoded = FileId.decode(file_id)
    return InputDocument(
        id=decoded.media_id,
        access_hash=decoded.access_hash,
        file_reference=decoded.file_reference,
    )


async def get_sticker_set_by_name(client, name):
    try:
        return await client.invoke(
            raw.functions.messages.GetStickerSet(
                stickerset=InputStickerSetShortName(short_name=name),
                hash=0,
            )
        )
    except errors.exceptions.not_acceptable_406.StickersetInvalid:
        return None


async def create_sticker_set(client, owner, title, short_name, stickers):
    return await client.invoke(
        raw.functions.stickers.CreateStickerSet(
            user_id=await client.resolve_peer(owner),
            title=title,
            short_name=short_name,
            stickers=stickers,
        )
    )


async def add_sticker_to_set(client, stickerset, sticker):
    return await client.invoke(
        raw.functions.stickers.AddStickerToSet(
            stickerset=InputStickerSetShortName(
                short_name=stickerset.set.short_name
            ),
            sticker=sticker,
        )
    )


async def create_sticker(sticker, emoji):
    return raw.types.InputStickerSetItem(document=sticker, emoji=emoji)
