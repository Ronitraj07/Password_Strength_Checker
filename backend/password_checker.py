from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:3000",
        "https://password-strength-checker-pi-tan.vercel.app",  # Your Vercel frontend
        "https://*.vercel.app"  # Allow all Vercel preview deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class PasswordRequest(BaseModel):
    password: str

@app.post("/check-password/")
async def check_password(request: PasswordRequest):
    password = request.password
    
    # Simple password strength checker
    if len(password) < 6:
        strength = "Weak"
    elif len(password) < 10:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {"strength": strength}
