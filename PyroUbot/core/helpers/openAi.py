import asyncio
import random

import openai

from PyroUbot import OPENAI_KEY

openai.api_key = random.choice(OPENAI_KEY)


class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        response = await asyncio.to_thread(
            openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
            stream=True,
        )
        return response

    @staticmethod
    async def ImageDalle(question):
        response = await asyncio.to_thread(
            openai.Image.create,
            prompt=question,
            n=1,
        )
        return response["data"][0]["url"]

    @staticmethod
    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.to_thread(
            openai.Audio.transcribe, "whisper-1", audio_file
        )
        return response["text"]
