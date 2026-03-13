from fastapi import APIRouter
from database.supabase import supabase
from models.user import UserRegister, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserRegister):

    # check if user already exists
    existing = supabase.table("users") \
        .select("*") \
        .eq("email", user.email) \
        .execute()

    if existing.data:
        return {"message": "User already exists"}

    # insert new user
    response = supabase.table("users").insert({
        "name": user.name,
        "email": user.email,
        "password": user.password
    }).execute()

    return {
        "message": "User registered successfully",
        "user": response.data
    }


@router.post("/login")
def login(user: UserLogin):

    response = supabase.table("users") \
        .select("*") \
        .eq("email", user.email) \
        .execute()

    users = response.data

    if not users:
        return {"message": "User not found"}

    db_user = users[0]

    if db_user["password"] != user.password:
        return {"message": "Incorrect password"}

    return {
        "message": "Login successful",
        "user": {
            "name": db_user["name"],
            "email": db_user["email"]
        }
    }