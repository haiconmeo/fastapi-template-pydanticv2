from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from re import sub
from sqlalchemy import Column, DateTime, Boolean, Integer
from datetime import datetime
from sqlalchemy.dialects.postgresql.base import UUID
import uuid


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


@as_declarative()
class Base():
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True),
                        default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True), default=None)

    __name__: str

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)


@as_declarative()
class BaseMTM():
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__)
