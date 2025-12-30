from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/seller",
    tags=["Seller"]
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

@router.post("/", response_model=schemas.Display_seller)
def create_seller(
    request: schemas.Seller,
    db: Session = Depends(get_db)
):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Sellers(
        username=request.username,
        email=request.email,
        password=hashed_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
