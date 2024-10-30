import os
from ..util import async_get

JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")


# TODO : replace below according to actual service
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

# Function to filter jobs by date or other criteria
async def filter_jobs(date=None, job_type=None, experience_level=None):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/filter"
    params = {}
    if date:
        params["date"] = date
    if job_type:
        params["job_type"] = job_type
    if experience_level:
        params["experience_level"] = experience_level
    return await async_get(url, params=params)

# Function to apply for a job
async def apply_for_job(job_id, user_id, resume_url):
    url = f"{JOB_SEARCH_SERVICE_URL}/jobs/{job_id}/apply"
    data = {
        "user_id": user_id,
        "resume_url": resume_url
    }
    return await async_post(url, json=data)

