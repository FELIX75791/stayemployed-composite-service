from fastapi import FastAPI
from app.routes import composite_routes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Include routers
app.include_router(composite_routes.router)