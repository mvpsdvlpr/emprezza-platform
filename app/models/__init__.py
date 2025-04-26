from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Importamos TODOS los modelso disponibles en el projecto
# para utilizar con Alembic

from app.models.users import Users
from app.models.employee import Employee
from app.models.client import Client
from app.models.category import Category
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem 
from app.models.debt import Debt
from app.models.inventory_movement import InventoryMovement
from app.models.online_order import OnlineOrder
from app.models.online_order_item import OnlineOrderItem
from app.models.sii_document import SiiDocument
from app.models.audit_log import AuditLog