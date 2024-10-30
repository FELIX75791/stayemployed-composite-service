from fastapi import APIRouter, HTTPException, Request, Body,Depends
from ..services.user_profile_service import fetch_user_profile
from ..services.application_tracker_service import fetch_user_applications
from ..services.application_tracker_service import update_application_status
from ..services.application_tracker_service  import submit_new_application
from ..services.job_search_service import fetch_all_jobs
from .models import Link
from ..services.auth_service import decode_access_token
import os
router = APIRouter()

# @router.get("/")
# def hello(request: Request):
#   return {"he": "hi"}

# @router.get("/dashboard")
# async def get_dashboard(user_id: int, request: Request):
#     try:
#         # Extract JWT token from the incoming request's authorization header
#         token = request.headers.get("Authorization")
#         if not token:
#             raise HTTPException(status_code=401, detail="Authorization token is missing")
        
#         payload = decode_access_token(token)
#         email: str = payload.get("sub")
#         # Use the token when calling user-profile-service
#         user_profile = await fetch_user_profile(email, token)
#         applications = await fetch_user_applications(token)  # Assume no auth required for simplicity
#         all_jobs = await fetch_all_jobs()  # Assume no auth required for simplicity

#         return {
#             "user_profile": user_profile,
#             "applications": applications,
#             "todays_jobs": all_jobs
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
USER_PROFILE_SERVICE_URL = os.getenv("USER_PROFILE_SERVICE_URL")
JOB_SEARCH_SERVICE_URL = os.getenv("JOB_SEARCH_SERVICE_URL")
APPLICATION_SERVICE_URL = os.getenv("APPLICATION_SERVICE_URL")
@router.get("/dashboard")
def get_dashboard(user_id: int, request: Request):
    try:
        # Extract JWT token from the incoming request's authorization header
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is missing")

        payload = decode_access_token(token)
        email: str = payload.get("sub")
        # Use the token when calling user-profile-service
        user_profile = fetch_user_profile(email, token)
        applications = fetch_user_applications(token)  # Assume no auth required for simplicity
        # all_jobs = fetch_all_jobs()  # Assume no auth required for simplicity
        links = [
            {"rel": "self", "href": f"/dashboard?user_id={user_id}"},
            {"rel": "view_profile", "href":f"{USER_PROFILE_SERVICE_URL}/info/{user_id}"},
            {"rel": "job_search", "href": f"{JOB_SEARCH_SERVICE_URL}/jobs/"},
            {"rel": "application_management", "href": f"{APPLICATION_SERVICE_URL}/my_applications/{user_id}"}
        ]
        return {
            "user_profile": user_profile,
            "applications": applications,
            "links": [Link(**link) for link in links]
            # "todays_jobs": all_jobs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/applyJobs")
async def apply_jobs(request: Request, apply_jobs: dict = Body(...)):
  try:
      # Extract JWT token from the incoming request's authorization header
      token = request.headers.get("Authorization")
      if not token:
          raise HTTPException(status_code=401, detail="Authorization token is missing")

      results = []
      for job_id, apply in apply_jobs.items():
          result = await submit_new_application(apply, token)
          results.append(result)
      
      return {
          "new_applications": results
      }
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

@router.put("/changeStatus")
async def change_status(request: Request, app_updates: dict = Body(...)):
    try:
        # Extract JWT token from the incoming request's authorization header
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is missing")

        results = []
        for application_id, updates in app_updates.items():
            result = await update_application_status(application_id, updates, token)
            results.append(result)
        
        return {
            "new_application_status": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
    
