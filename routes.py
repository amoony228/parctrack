from typing import Optional, List, Annotated
from fastapi import APIRouter, Depends

import db_methods
from schemes import returnStatusShema
from dependencies import add_new_order_status_depend



crud_router = APIRouter(prefix="/crud")


@crud_router.get("/get_order_status/{order_id}")
async def get_order_status(order_id:str) -> Optional[List[returnStatusShema]]:
    return await db_methods.get_order_status_by_order(order_id)
    
@crud_router.post("/add_new_order_status")
async def add_new_order_status(data: Annotated[dict, Depends(add_new_order_status_depend)]) -> None:
    await db_methods.add_new_order_status(data['order_id'], data['status'], data['datetime'])

    
