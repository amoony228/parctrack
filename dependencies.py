from fastapi import HTTPException

from schemes import addNewStatusShema
import db_methods

async def add_new_order_status_depend(data:addNewStatusShema) -> dict:
    if await db_methods.get_admin_password_by_name(data.admin_name) != data.admin_password:
        raise HTTPException(status_code=403)
    if not await db_methods.is_order_exist(data.body.order_id):
        raise HTTPException(status_code=404, detail='order not found')
    
    return {'order_id' : data.body.order_id, 'status' : data.body.status, 'datetime' : data.body.datetime}