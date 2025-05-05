from typing import List
import datetime

from db_connection import database
from schemes import returnStatusShema
from common.decorators import json_return


@json_return
async def get_order_status_by_order(order_id:int) -> List[returnStatusShema]:
    async with database.connections_pool.acquire() as connection:
        return await connection.fetch('''SELECT status, datetime FROM public.orders_status WHERE order_id = $1;''', order_id)

async def get_admin_password_by_name(admin_name:str) -> List[returnStatusShema]:
    async with database.connections_pool.acquire() as connection:
        return await connection.fetchval('''SELECT admin_password FROM public.admins WHERE admin_name = $1;''', admin_name)

async def add_new_order_status(order_id:str, status:str, datetime:datetime.datetime) -> None:
    async with database.connections_pool.acquire() as connection:
        await connection.execute('''INSERT INTO public.orders_status(order_id, status, datetime) VALUES ($1, $2, $3)''', order_id, status, datetime)

async def is_order_exist(order_id:str) -> bool:
    async with database.connections_pool.acquire() as connection:
        return not await connection.fetchval('''SELECT id FROM public.orders WHERE id = $1;''', order_id) is None