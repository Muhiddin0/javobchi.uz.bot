from loader import dp
from aiogram import types
import requests

@dp.message_handler(content_types=['text'])
async def chat_ai(message: types.Message):
    await message.answer('⏱...')

    url = "https://twitter.blueto.app:8443/cargpt/sendPrompt"
    payload = {
        "app": "com.dominapp.supergpt",
        "deviceId": "4e2a3d23384a4dfc",
        "email": "mkabraliev2005@gmail.com",
        "isPremiumUser": False,
        "isProUser": False,
        "page": 0,
        "proUserId": "",
        "proUserToken": "",
        "text": message.text,
        "token": "4e2a3d23384a4dfc"
    }
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 13; SM-A037F Build/TP1A.220624.014)",
        "host": "twitter.blueto.app:8443",
        "accept": "application/json"
    }


    response = requests.request("POST", url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        await message.answer(text=data['textResponse'])
        return
    
    await message.answer("Kechirasiz xatolik sodir bo'ldi qaytdan urinib ko'ring")
    