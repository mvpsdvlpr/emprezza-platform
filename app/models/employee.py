from app.models import Base
from sqlalchemy import Column, String, Boolean, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
