from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from schemas.profile import Job, Demo, Profile
from database.connectToDatabase import connectToDatabase as db
from app.middleware.hashPassword import get_hashed_password
from uuid import uuid4
from app.middleware.dependecies import get_current_user

@app.get('/me', summary='Get details of currently logged in user', response_model=Profile)
async def get_me(user: Profile = Depends(get_current_user)):
    return user

@app.post('/signup', summary="Create new user", response_model=Profile)
async def create_user(data: Profile):
    # querying database to check if user already exist
    user = db.get(data.email, None)
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db[data.email] = user    # saving user to database
    return user