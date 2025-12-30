from fastapi import APIRouter, Depends, HTTPException, status
from product.routers.login import get_current_user
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(
    request: schemas.Product,
    db: Session = Depends(get_db)
):
    product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=1
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/", response_model=List[schemas.DisplayProduct])
def get_products(db: Session = Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    return db.query(models.Product).all() 


@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


@router.put("/{id}")
def update_product(
    id: int,
    request: schemas.Product,
    db: Session = Depends(get_db)
):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=404, detail="Product not found")

    product.update(request.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=404, detail="Product not found")

    product.delete(synchronize_session=False)
    db.commit()
    return {"message": "Product deleted successfully"}
