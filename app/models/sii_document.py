from app.models import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class SiiDocument(Base):
    __tablename__ = "sii_documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sale_id = Column(UUID(as_uuid=True), ForeignKey("sales.id", ondelete="CASCADE"), nullable=False)
    sii_folio = Column(String)
    document_type = Column(String)
    status = Column(String)
    created_at = Column(DateTime)
