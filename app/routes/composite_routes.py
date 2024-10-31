from fastapi import APIRouter, HTTPException, Request, Body
from ..services.user_profile_service import fetch_user_profile
from ..services.application_tracker_service import fetch_user_applications
from ..services.application_tracker_service import update_application_status
from ..services.application_tracker_service  import submit_new_application
from ..services.job_search_service import fetch_all_jobs

from ..services.auth_service import decode_access_token
from ..services.Hateoas import Hateoas


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

# Helper function to generate HATEOAS links

@router.get("/dashboard")
def get_dashboard(user_id: int, request: Request):
    try:
        # Extract JWT token from the incoming request's authorization header
        token = request.headers.get("Authorization")
        print(token)
        if not token:
            raise HTTPException(status_code=401, detail="Authorization token is missing")
        
        payload = decode_access_token(token)
        email: str = payload.get("sub")
        print(email)
        # Use the token when calling user-profile-service
        user_profile = fetch_user_profile(email, token)
        applications = fetch_user_applications(token)
        
        # all_jobs = fetch_all_jobs() 
        hateoas = Hateoas(user_profile["status_code"], applications["status_code"], -1)
        links = hateoas.generate_hateoas("/dashboard")

        return {
            "user_profile": user_profile["data"],
            "applications": applications["data"],
            "links": links
            # "todays_jobs": all_jobs
        }
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/applyJobs")
async def apply_jobs(request: Request, apply_jobs: dict = Body(...)):
  try:
      # Extract JWT token from the incoming request's authorization header
      token = request.headers.get("Authorization")
      if not token:
          raise HTTPException(status_code=401, detail="Authorization token is missing")

      results = []
      application_code = 200
      user_code = 200
      for job_id, apply in apply_jobs.items():
        submit = await submit_new_application(apply, token)
        data = submit["data"]
        results.append(data)
        if submit["status_code"] != 200:
          application_code = -1
      
      hateoas = Hateoas(user_code, application_code, -1)
      links = hateoas.generate_hateoas("/applyJobs")

      return {
          "new_applications": results,
          "links": links
      }
  except HTTPException as e:
      raise HTTPException(status_code=e.status_code, detail=str(e.detail))
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
        update_code = 200
        user_code = 200
        for application_id, updates in app_updates.items():
            result = await update_application_status(application_id, updates, token)
            data = result["data"]
            results.append(data)

        hateoas = Hateoas(user_code, -1, result["status_code"])
        links = hateoas.generate_hateoas("/applyJobs")
        
        return {
            "new_application_status": results,
            "links": links
        }
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
    
