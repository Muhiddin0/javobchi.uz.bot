import requests
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

def create_user(user_id, first_name, user_name=None):
    """
        Foydalanuvchi ro'yxatdan o'tkazish
    """
    users = requests.get(url=BASE_URL).json()
    for i in users:
        if i['user_id'] == user_id: return
    post = requests.post(url=BASE_URL, data={
        "first_name": first_name,
        "user_id": user_id,
    }).json()
    return post
