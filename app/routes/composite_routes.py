from fastapi import APIRouter, HTTPException, Request, Body
from ..services.user_profile_service import fetch_user_profile
from ..services.application_tracker_service import fetch_user_applications
from ..services.application_tracker_service import update_application_status
from ..services.job_search_service import fetch_all_jobs

from ..services.auth_service import decode_access_token

router = APIRouter()

# @router.get("/")
# def hello(request: Request):
#   return {"he": "hi"}

@router.get("/dashboard")
async def get_dashboard(user_id: int, request: Request):
    try:
        # Extract JWT token from the incoming request's authorization header
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is missing")
        
        payload = decode_access_token(token)
        email: str = payload.get("sub")
        # Use the token when calling user-profile-service
        user_profile = await fetch_user_profile(email, token)
        applications = await fetch_user_applications(token)  # Assume no auth required for simplicity
        all_jobs = await fetch_all_jobs()  # Assume no auth required for simplicity

        return {
            "user_profile": user_profile,
            "applications": applications,
            "todays_jobs": all_jobs
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
    
