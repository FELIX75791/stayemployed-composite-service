import os
from ..util import async_get, sync_put, sync_post, async_patch
from dotenv import load_dotenv

load_dotenv()

APPLICATION_SERVICE_URL = os.getenv("APPLICATION_SERVICE_URL")

# TODO : replace below according to actual service
async def fetch_user_applications(token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications?page=1"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_get(url, headers=headers)

async def update_application_status(application_id:int, updates: dict, token:str):
    url = f"{APPLICATION_SERVICE_URL}/my_applications/{application_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return await async_patch(url, json=updates, headers=headers)


def submit_new_application(data):
    url = f"{APPLICATION_SERVICE_URL}/applications/new"
    return sync_post(url, json=data)
