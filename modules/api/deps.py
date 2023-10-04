from typing import Generator
import json
from fastapi import Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.orm import Session
from modules.core.config import settings
from modules.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
