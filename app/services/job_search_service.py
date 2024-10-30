import os
from ..util import async_get

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")

import os
from ..util import async_get, async_post

# Base URL for the job search service
JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")

# Function to fetch today's jobs
async def fetch_todays_jobs():
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/today"
    return await async_get(url)

# Function to search for jobs by keyword
async def search_jobs_by_keyword(keyword):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/search"
    params = {"keyword": keyword}
    return await async_get(url, params=params)

# Function to search jobs by location
async def search_jobs_by_location(location):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/location"
    params = {"location": location}
    return await async_get(url, params=params)

# Function to apply for a job
async def apply_for_job(job_id, user_id, resume_url):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/{job_id}/apply"
    data = {
        "user_id": user_id,
        "resume_url": resume_url
    }
# PUT method to update job details
async def update_job_details(job_id, title=None, description=None, location=None):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/{job_id}"
    data = {}
    if title:
        data["title"] = title
    if description:
        data["description"] = description
    if location:
        data["location"] = location
    return await async_post(url, json=data)

