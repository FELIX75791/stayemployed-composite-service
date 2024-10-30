import os
from ..util import async_get
from dotenv import load_dotenv

load_dotenv()

USER_PROFILE_SERVICE_URL = os.getenv("USER_PROFILE_SERVICE_URL")

async def fetch_user_profile(user_email:str, token: str):
    url = f"{USER_PROFILE_SERVICE_URL}/info/{user_email}"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_get(url, headers=headers)

