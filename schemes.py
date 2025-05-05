from pydantic import BaseModel, AfterValidator
from typing import Annotated
import datetime 


offset_naive_datetime = Annotated[
    datetime.datetime,
    AfterValidator(lambda x: x.replace(tzinfo=None))]


class returnStatusShema(BaseModel):
    status: str
    datetime: offset_naive_datetime


class orderStatusShema(BaseModel):
    order_id: str
    status: str
    datetime: offset_naive_datetime

class addNewStatusShema(BaseModel):
    admin_name: str
    admin_password: str
    body: orderStatusShema


    