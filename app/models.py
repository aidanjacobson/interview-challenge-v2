from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)

class Symptom(Base):
    __tablename__ = "symptom"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    business_id = Column(Integer, ForeignKey('business.id'), nullable=False)
    code = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    diagnostic = Column(Boolean, nullable=False)