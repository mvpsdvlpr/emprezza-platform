from app.models import Base
from sqlalchemy import Column, String, Numeric, ForeignKey, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class OnlineOrder(Base):
    __tablename__ = "online_orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    client_name = Column(String, nullable=False)
    status = Column(String, default="pending")
    total_amount = Column(Numeric(12,2), nullable=False)
    created_at = Column(DateTime)
