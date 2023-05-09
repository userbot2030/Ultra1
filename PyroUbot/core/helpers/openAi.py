import asyncio
import random

import openai

from PyroUbot import OPENAI_KEY

openai.api_key = random.choice(OPENAI_KEY)


class OpenAi:
    async def ChatGPT(question):
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.5,
                stop=None,
                n=1,
                user="arc",
                max_tokens=768,
            ),
        )
        return response["choices"][0].text.strip()

    async def ImageDalle(question):
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: openai.Image.create(
                prompt=question,
                n=1,
                size="1024x1024",
                user="arc",
            ),
        )
        return response["data"][0]["url"]

    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.get_event_loop().run_in_executor(
            None, lambda: openai.Audio.transcribe("whisper-1", audio_file)
        )
        return response["text"]
