from app.models import Base
from sqlalchemy import Column, Numeric, Boolean, Text, ForeignKey, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Sale(Base):
    __tablename__ = "sales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id", ondelete="SET NULL"))
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="SET NULL"))
    total_amount = Column(Numeric(12,2), nullable=False)
    is_credit = Column(Boolean, default=False)
    paid = Column(Boolean, default=True)
    sale_date = Column(DateTime)
    notes = Column(Text)
