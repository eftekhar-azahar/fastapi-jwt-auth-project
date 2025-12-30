from fastapi import FastAPI
from . import models
from .database import engine
from .routers import product, seller,login

app = FastAPI(
    title="Product API",
    description="Get details of all the products on our website",
    terms_of_service="http://www.google.com",
    contact={
        "name": "Eftekhar Azahar",
        "url": "http://www.google.com",
        "email": "demo@gmail.com",
    }
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)

models.Base.metadata.create_all(bind=engine)

