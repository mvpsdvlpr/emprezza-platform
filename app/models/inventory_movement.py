from app.models import Base
from sqlalchemy import Column, String, Text, Numeric, ForeignKey, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    movement_type = Column(String, nullable=False)
    quantity = Column(Numeric(12,2), nullable=False)
    reason = Column(Text)
    created_at = Column(DateTime)
