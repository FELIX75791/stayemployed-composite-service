import os
from ..util import async_get

USER_PROFILE_SERVICE_URL = os.getenv("USER_PROFILE_SERVICE_URL")

async def fetch_user_profile(user_id: int, token: str):
    url = f"{USER_PROFILE_SERVICE_URL}/info/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_get(url, headers=headers)
