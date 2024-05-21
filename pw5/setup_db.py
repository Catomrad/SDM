from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class ClientModel(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class OrderModel(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    clients = Column(Integer)
    products = Column(Integer)

class ProductModel(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    material = Column(String)

# Database setup
engine = create_engine('sqlite:///jobs.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()