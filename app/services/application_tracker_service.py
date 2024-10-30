import os
from ..util import async_get, sync_put, sync_post, async_patch, sync_get
from dotenv import load_dotenv

load_dotenv()

APPLICATION_SERVICE_URL = os.getenv("APPLICATION_SERVICE_URL")

async def fetch_user_applications(token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications?page=1"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_get(url, headers=headers)

def fetch_user_applications(token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications?page=1"
    headers = {"Authorization": f"Bearer {token}"}
    return sync_get(url, headers=headers)

async def update_application_status(application_id:int, updates: dict, token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications/{application_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_patch(url, json=updates, headers=headers)

async def submit_new_application(data, token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications"
    headers = {"Authorization": f"Bearer {token}"}
    return sync_post(url, json=data, headers=headers)
