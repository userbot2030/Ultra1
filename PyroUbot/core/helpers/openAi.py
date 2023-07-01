import random
import aiohttp

import openai

from PyroUbot import OPENAI_KEY

openai.api_key = random.choice(OPENAI_KEY)

class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {openai.api_key}",
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": question}],
                },
            )
            data = await response.json()
            return data["choices"][0]["message"]["content"].strip()

    @staticmethod
    async def ImageDalle(question):
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                "https://api.openai.com/v1/images",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {openai.api_key}",
                },
                json={
                    "prompt": question,
                    "n": 1,
                },
            )
            data = await response.json()
            return data["data"][0]["url"]

    @staticmethod
    async def SpeechToText(file):
        async with aiohttp.ClientSession() as session:
            audio_file = open(file, "rb")
            response = await session.post(
                "https://api.openai.com/v1/audio/transcriptions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {openai.api_key}",
                },
                data=audio_file,
            )
            data = await response.json()
            return data["text"]
