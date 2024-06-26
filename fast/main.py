import uvicorn
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# Database configurations
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
    
    # open database editor:
    # 	create database "Interview"
    # 	create table [Person] (
    # 				personID int
    # 				, name unicode string(100)
    # 				, age decimal
    # 				, nationalityID int
    # 				, birthDate datetime
    # 				)
 
# CREATE TABLE Person (
# id INT,
# name varchar(100) 
# age int,
# nationalityID int,
# last_login DATETIME,
# )   

# -- insert values into the Users table.
# INSERT INTO Users
# VALUES
 
# SQLAlchemy models
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True) # decimal
    nationalityID = Column(Integer, index=True)
    description = Column(String, index=True)
    #start_date: datetime.date = datetime.date.today(),

 
 
Base.metadata.create_all(bind=engine)
 
# FastAPI app instance
app = FastAPI()
 
 
# CRUD operations
# Create (Create)
@app.post("/items/")
async def create_item(name: str, description: str):
    db = SessionLocal()
    db_item = Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
 
 
# Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    return item
 
 
# Update (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, description: str):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db_item.name = name
    db_item.description = description
    db.commit()
    return db_item
 
 
# Delete (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
 
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", ports=[30000,8443])


