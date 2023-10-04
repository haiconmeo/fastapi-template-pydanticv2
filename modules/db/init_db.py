from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.models import Users
from app.crud import crud_user
from app.db import base  # noqa: F401
from app.schemas import UserCreate
from app.core import security


def init_db(db: Session) -> None:

    user = crud_user.get_by_email(db, email='admin@admin.com')
    if not user:
        user_in = UserCreate(
            email='admin@admin.com',
            password=security.get_password_hash(''),
            full_name='admin'
        )
        user = crud_user.create(db, obj_in=user_in)
