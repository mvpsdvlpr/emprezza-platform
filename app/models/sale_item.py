from app.models import Base
from sqlalchemy import Column, Numeric, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID

class SaleItem(Base):
    __tablename__ = "sale_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sale_id = Column(UUID(as_uuid=True), ForeignKey("sales.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="SET NULL"))
    quantity = Column(Numeric(12,2), nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)
