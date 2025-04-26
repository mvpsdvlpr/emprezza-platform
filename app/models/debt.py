from app.models import Base
from sqlalchemy import Column, Numeric, ForeignKey, Text, Date, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Debt(Base):
    __tablename__ = "debts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sale_id = Column(UUID(as_uuid=True), ForeignKey("sales.id", ondelete="CASCADE"), nullable=False)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="SET NULL"))
    amount_due = Column(Numeric(12,2), nullable=False)
    due_date = Column(Date)
    status = Column(Text, default="pending")
    payment_date = Column(DateTime)
