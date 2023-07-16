import asyncio

import openai

from PyroUbot import OPENAI_KEY

openai.api_key = OPENAI_KEY


class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        response = await asyncio.to_thread(
            openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message["content"].strip()

    @staticmethod
    async def ImageDalle(question):
        response = await asyncio.to_thread(
            openai.Completion.create,
            model="dall-e-2-0",
            prompt=question,
            n=1,
        )
        return response.choices[0].text.strip()

    @staticmethod
    async def SpeechToText(file):
        with open(file, "rb") as audio_file:
            response = await asyncio.to_thread(
                openai.SpeechApi.transcribe, audio=audio_file
            )
        return response["transcriptions"][0]["text"]
