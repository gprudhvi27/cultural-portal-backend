from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Google API Key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Create FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Cultural Discovery Portal API is running!"}

# Test endpoint to check API Key loading
@app.get("/check-api-key")
def check_api_key():
    if GOOGLE_API_KEY:
        return {"Google API Key": GOOGLE_API_KEY}
    else:
        return {"error": "Google API Key not found!"}
