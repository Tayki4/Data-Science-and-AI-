

# Encapsulation (Bilgi Gizleme)

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3

class BaseEntity:
    def __init__(self):
        self.__id = None
        self.__create_date = None
        self.__computer_name = None
        self.__ip_address = None
        self.__status = None

    def set_values_private_attributes(self):
        self.__id = uuid4()
        self.__create_date = datetime.now()
        self.__computer_name = gethostname()
        self.__ip_address = gethostbyname(gethostname())
        self.__status = Status.Active

class Product(BaseEntity):
    def __init__(self, name: str, description: str):
        super().__init__()
        self.description = description
        self.name = name
        self.__price = None
        self.__stock = None

    def set_values_product_attributes(self, price: float, stock: int):
        if price > 0 and stock > 0:
            super().set_values_private_attributes()
            self.__price = price
            self.__stock = stock
            print('Product has been created')
            pprint(self.__dict__)
        else:
            print('Invalid inputs..!\nProduct has not been created..!')

p1 = Product(name='Boxing Gloves', description='A boxing gloves')
p1.set_values_product_attributes(price=50, stock=10)
