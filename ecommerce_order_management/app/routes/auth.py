from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.user import User

from app.schemas.auth import (
    UserRegister
)

from app.utils.security import (
    verify_password,
    hash_password
)

from app.utils.jwt import (
    create_access_token
)


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# REGISTER
@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()


    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="admin"
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return {
        "message": "User Registered"
    }



# LOGIN
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()


    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )


    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )


    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }