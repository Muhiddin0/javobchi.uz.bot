from loader import dp
from aiogram import types
import requests
import time

@dp.message_handler(commands=['image'])
async def image_ai(message: types.Message):
    await message.answer('⏱ Iltimos Biroz kuting...')
    q = message.get_full_command()[1]
    url = "https://stablediffusionapi.com/api/v1/enterprise/text2img"
    payload = {
        "enhance_prompt": "no",
        "guidance_scale": 8,
        "height": 600,
        "init_image": "",
        "key": "2pma11c5oni6n2",
        "loadbalancer": "yes",
        "mask_image": "",
        "model_id": "dream_shaper",
        "multi_lingual": "yes",
        "negative_prompt": ", sexy, nsfw, show skin, dress sexually, nude",
        "num_inference_steps": 25,
        "prompt": q,
        "safety_checker": "no",
        "samples": 1,
        "seed": 796354777,
        "strength": 0.5,
        "width": 600
    }
    headers = {
        "accept-encoding": "gzip",
        "connection": "Keep-Alive",
        "content-type": "application/json; charset=UTF-8"
    }
    
    
    for i in range(0,4):
        response = requests.request("POST", url, json=payload, headers=headers).json()
        if response['status'] == 'success':
            # print('----------------')
            # print(response)
            # print('----------------')

            img_url = ''.join(response['output'][0].split('\\'))
            time.sleep(3)
            for i in range(0,4):
                try:
                    await message.answer_photo(photo=img_url)
                    return
                except:pass
                
    await message.answer(
        """Ming bor uzur Xatolikga duch keldik qaytadan urinib ko'ring"""
    )