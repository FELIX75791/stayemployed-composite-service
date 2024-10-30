import os
from ..util import async_get, sync_get
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

USER_PROFILE_SERVICE_URL = os.getenv("USER_PROFILE_SERVICE_URL")

# async def fetch_user_profile(user_email:str, token: str):
#     url = f"{USER_PROFILE_SERVICE_URL}/info/{user_email}"
#     headers = {"Authorization": f"Bearer {token}"}
#     return await async_get(url, headers=headers)

def fetch_user_profile(user_email:str, token: str):
    url = f"{USER_PROFILE_SERVICE_URL}/info/{user_email}"
    headers = {"Authorization": f"Bearer {token}"}
    try:
      response = sync_get(url, headers=headers)
      return {"data": response, "status_code": 200, "error": None}
    except HTTPException as e:
      if e.response.status_code == 401:
        raise HTTPException(status_code=401, detail="Unauthorized")
      return {"data": None, "status_code": e.status_code, "error": e.detail}
