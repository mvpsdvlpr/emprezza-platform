from app.models import Base
from sqlalchemy import Column, String, Text, Numeric, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="SET NULL"))
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric(12,2), nullable=False)
    stock_quantity = Column(Numeric(12,2), default=0)
    unit_type = Column(String, default="unit")
