import json
import os
import asyncio
import aiohttp
from ..util import async_get, sync_post, sync_get

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")

def fetch_all_jobs(location, keywords, contract_period):
    url = f"{JOB_SEARCH_SERVICE_URL}/fetch-jobs/"
    body = {
        "location": location,
        "keywords": keywords,
        "sort": "relevance",
        "contract_period": contract_period,
        "purpose": "dashboard"
    }
    try:
        response = sync_post(url, json=body)
        return response
    except Exception as e:
        return {"error": str(e)}

# def create_job():
#     url = f"{JOB_SEARCH_SERVICE_URL}/jobs/"
#     return sync_post(url, json=apply_job)
