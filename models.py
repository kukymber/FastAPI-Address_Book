from sqlalchemy import Column, String, Integer, DATETIME, Text, ForeignKey, UniqueConstraint
from database import Base
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy_utils import EmailType


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    gender = Column(ENUM('male', 'female'))
    birthday_year = Column(DATETIME)
    residential_address = Column(Text)


# class PhoneNumber(Base):
#     __tablename__ = 'phone_numbers'
#
#     id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
#     type_of_number = Column(ENUM('city', 'phone'))
#     phone_number = Column(Integer, unique=True, nullable=False)
#
#
# class Email(Base):
#     __tablename__ = 'email'
#
#     id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
#     type_of_email = Column(ENUM('working', 'personal'))
#     email = Column(EmailType)
