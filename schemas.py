from enum import Enum

from pydantic import BaseModel, validator, EmailStr
from pydantic.schema import date

#  this class is used in User.gender for
#  validation objects
class GenderEnum(str, Enum):
    male = 'Male'
    female = 'Female'


class TypePhoneNumberEnum(str, Enum):
    city = 'city'
    phone = 'phone'


class User(BaseModel):
    id: int
    full_name: str
    gender: GenderEnum
    birthday: date
    residential_address: str


class PhoneNumber(BaseModel):
    id_user: int
    type_of_number: TypePhoneNumberEnum
    phone_number: int


class Email(BaseModel):
    id_user: int
    type_of_email: str
    email: EmailStr

