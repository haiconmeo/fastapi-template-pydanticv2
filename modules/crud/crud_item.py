"""crud user"""
from typing import Any, List
from sqlalchemy.orm import Session
from modules.common.client_filter import new_filter
from modules.crud.base import CRUDBase
from modules.models import Item
from modules.schema import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):

    pass


crud_item = CRUDItem(Item)
