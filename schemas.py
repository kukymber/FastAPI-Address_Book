import datetime
from enum import Enum
import datetime

import pydantic
from pydantic import BaseModel, validator, EmailStr
from pydantic.schema import date


class User(BaseModel):
    id: int
    full_name: str
    gender: str
    birthday: date
    residential_address: str


# class Gender(str, Enum):
#     male = 'Male'
#     female = 'Female'


class PhoneNumber(BaseModel):
    id_user: int
    type_of_number: str
    phone_number: int

class Email(BaseModel):
    id_user: int
    type_of_email: str
    email: EmailStr


data = {'id': '1', 'type_of_email': "work", 'email': "male@mail.ru"}

user = Email(**data)
print(user.dict)
