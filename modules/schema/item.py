from typing import List, Optional
from pydantic import BaseModel, UUID4
from datetime import datetime

from modules.common.string_case import to_camel_case


class ItemBase(BaseModel):
    full_name: str

    class Config:
        alias_generator = to_camel_case
        populate_by_name = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemInDBBase(ItemBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class Item(ItemInDBBase):
    pass


class Items(BaseModel):
    total: int
    results: List[Item]
