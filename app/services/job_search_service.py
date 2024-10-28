import os
from ..util import async_get

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")


# TODO : replace below according to actual service
async def fetch_todays_jobs():
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/today"
    return await async_get(url)
