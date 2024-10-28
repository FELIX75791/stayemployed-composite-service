import os
from ..util import async_get, sync_put, sync_post

APPLICATION_SERVICE_URL = os.getenv("APPLICATION_SERVICE_URL")


# TODO : replace below according to actual service
async def fetch_user_applications(user_id: int):
    url = f"{APPLICATION_SERVICE_URL}/applications"
    return await async_get(url, params={"user_id": user_id})


def update_application_status(data):
    url = f"{APPLICATION_SERVICE_URL}/applications/updateStatus"
    return sync_put(url, json=data)


def submit_new_application(data):
    url = f"{APPLICATION_SERVICE_URL}/applications/new"
    return sync_post(url, json=data)
