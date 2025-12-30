from sqlalchemy import Column, Integer, String, Float,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    seller_id = Column(Integer, ForeignKey("sellers.id"))
    seller = relationship("Sellers", back_populates="products")



class Sellers(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String)
    password = Column(String)

    products = relationship("Product", back_populates="seller")




