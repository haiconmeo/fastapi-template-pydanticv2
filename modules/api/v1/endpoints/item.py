from typing import Any, List, Optional

from io import BytesIO
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.common.parameters import common_filter_parameters
from modules.crud import crud_item
from modules.api import deps
from modules.schema.item import Item, ItemCreate, Items
router = APIRouter()


@router.get("/", response_model=Items)
def read_items(
    db: Session = Depends(deps.get_db),
    filter_param: str = Depends(common_filter_parameters),
) -> Any:

    return crud_item.get_multi(
        db, filter_param=filter_param)


@router.post("/", response_model=Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: ItemCreate,

) -> Any:

    item = crud_item.create(db=db, obj_in=item_in)
    return item
