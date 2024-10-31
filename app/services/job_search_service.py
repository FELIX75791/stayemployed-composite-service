import os
from ..util import async_get, sync_post

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")

async def fetch_all_jobs():
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/"
    return await async_get(url)

# def create_job():
#     url = f"{JOB_SEARCH_SERVICE_URL}/jobs/"
#     return sync_post(url, json=apply_job)
