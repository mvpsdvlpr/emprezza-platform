from app.models import Base
from sqlalchemy import Column, String, Text, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Client(Base):
    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String, nullable=False)
    phone_number = Column(String)
    email = Column(String)
    address = Column(Text)
    notes = Column(Text)
