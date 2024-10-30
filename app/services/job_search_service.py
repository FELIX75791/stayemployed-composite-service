import os
from ..util import async_get

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")


# TODO : replace below according to actual service
async def fetch_all_jobs():
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/"
    return await async_get(url)
