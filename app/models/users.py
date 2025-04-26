from app.models import Base # desde __init__.py donde definimos nuestra base
from sqlalchemy import Column, String
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name= Column(String, nullable=False)
    email=Column(String, nullable=False)
    password_hash= Column(String, nullable=False)
    phone_number= Column(String)