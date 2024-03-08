import asyncio

import google.generativeai as genai
import openai

from PyroUbot import AI_GOOGLE_API

class OpenAi:
    @staticmethod
    async def google_ai(question):
        """
        create by: NorSodikin.t.me
        request by: Dhilnihnge.t.me
        """
        genai.configure(api_key=AI_GOOGLE_API)
        model = genai.GenerativeModel(model_name="gemini-1.0-pro")
        convo = model.start_chat(history=[])
        convo.send_message(question)
        return convo.last.text

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
        response = await asyncio.to_thread(openai.Audio.transcribe, "whisper-1", audio_file)
        return response["text"]
