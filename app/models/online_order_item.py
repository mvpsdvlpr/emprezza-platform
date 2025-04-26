from app.models import Base
from sqlalchemy import Column, Numeric, ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID

class OnlineOrderItem(Base):
    __tablename__ = "online_order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    online_order_id = Column(UUID(as_uuid=True), ForeignKey("online_orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="SET NULL"))
    quantity = Column(Numeric(12,2), nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)
