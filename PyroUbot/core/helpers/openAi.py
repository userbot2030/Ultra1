import random

import aiohttp
import openai

from PyroUbot import OPENAI_KEY

openai.api_key = random.choice(OPENAI_KEY)


class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        session = aiohttp.ClientSession()
        try:
            response = await session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {openai.api_key}"},
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": question}],
                },
            )
            data = await response.json()
            return data["choices"][0]["message"]["content"].strip()
        finally:
            await session.close()

    @staticmethod
    async def ImageDalle(question):
        session = aiohttp.ClientSession()
        try:
            response = await session.post(
                "https://api.openai.com/v1/images/dalle",
                headers={"Authorization": f"Bearer {openai.api_key}"},
                json={"prompt": question, "n": 1},
            )
            data = await response.json()
            return data["data"][0]["url"]
        finally:
            await session.close()

    @staticmethod
    async def SpeechToText(file):
        session = aiohttp.ClientSession()
        try:
            audio_file = open(file, "rb")
            response = await session.post(
                "https://api.openai.com/v1/audio/transcriptions",
                headers={"Authorization": f"Bearer {openai.api_key}"},
                data={"engine": "whisper-1"},
                files={"file": audio_file},
            )
            data = await response.json()
            return data["text"]
        finally:
            await session.close()
