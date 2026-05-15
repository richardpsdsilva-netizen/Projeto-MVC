from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

#Tabela
class Usuario (Base):
    __table__ = "usuarios"

