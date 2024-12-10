import os
from ..util import async_get, sync_put, sync_post, async_patch, sync_get, async_post
from dotenv import load_dotenv
from httpx import HTTPStatusError
from fastapi import HTTPException

load_dotenv()

APPLICATION_SERVICE_URL = os.getenv("APPLICATION_SERVICE_URL")

# async def fetch_user_applications(token:str):
#     url = f"{APPLICATION_SERVICE_URL}/my_applications?page=1"
#     headers = {"Authorization": f"Bearer {token}"}
#     return await async_get(url, headers=headers)

def fetch_user_applications(token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications?page=1"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = sync_get(url, headers=headers)["applications"]
        return {"data": response, "status_code": 200}
    except HTTPStatusError as e:
        if e.response.status_code == 401:
          raise HTTPException(status_code=401, detail="Unauthorized")
        return {"data": None, "status_code": e.response.status_code}


async def update_application_status(application_id:int, updates: dict, token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications/{application_id}"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = await async_patch(url, json=updates, headers=headers)
        return {"data": response, "status_code": 200}
    except HTTPStatusError as e:
        if e.response.status_code == 401:
          raise HTTPException(status_code=401, detail="Unauthorized")
        return {"data": None, "status_code": e.response.status_code}

async def submit_new_application(data, token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = await async_post(url, json=data, headers=headers)
        return {"data": response, "status_code": 200}
    except HTTPStatusError as e:
        if e.response.status_code == 401:
          raise HTTPException(status_code=401, detail="Unauthorized")
        return {"data": None, "status_code": e.response.status_code}
