from fastapi import APIRouter, HTTPException, Request
from ..services.user_profile_service import fetch_user_profile
from ..services.application_tracker_service import fetch_user_applications
from ..services.job_search_service import fetch_todays_jobs

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard(user_id: int, request: Request):
    try:
        # Extract JWT token from the incoming request's authorization header
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is missing")

        # Use the token when calling user-profile-service
        user_profile = await fetch_user_profile(user_id, token)
        applications = await fetch_user_applications(user_id)  # Assume no auth required for simplicity
        todays_jobs = await fetch_todays_jobs()  # Assume no auth required for simplicity

        return {
            "user_profile": user_profile,
            "applications": applications,
            "todays_jobs": todays_jobs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
