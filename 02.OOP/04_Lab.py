
# Method Overriding

class BaseEntity:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def show_info(self):
        print(
            f'Name: {self.name}\n'
            f'Description: {self.description}'
        )

class Category(BaseEntity):
    pass

class Product(BaseEntity):
    def __init__(self, name, description, price: float, stock: int):
        super().__init__(name, description)
        self.price = price
        self.stock = stock

    def show_info(self):
        super().show_info()
        print(
            f'Price: {self.price}\n'
            f'Stock: {self.stock}'
        )

p1 = Product(name='Boxing Gloves', description='Boxing Gloves', price=10.999, stock=100)
p1.show_info()

class BasePhone:
    def __init__(self, phone_id: str, model: str, brand: str, price: float):
        self.phone_id = phone_id
        self.model = model
        self.brand = brand
        self.price = price

    def show_info(self):
        print(
            f'Id: {self.phone_id}\n'
            f'Model : {self.model}\n'
            f'Brand: {self.brand}\n'
            f'Price: {self.price}'
        )

    def phone_ring_sound(self) -> str:
        return 'general phone sound'

class Iphone(BasePhone):
    def __init__(self, airdrop: str, phone_id: str, model: str, brand: str, price: float):
        super().__init__(phone_id, model, brand, price)
        self.airdrop = airdrop

    def show_info(self):
        super().show_info()
        print(f'Airdrop: {self.airdrop}')

    def phone_ring_sound(self):
        return 'Iphone phone sound'

class Samsung(BasePhone):
    def __init__(self, phone_id, model, brand, price, os: str):
        super().__init__(phone_id, model, brand, price)
        self.os = os

    def show_info(self):
        super().show_info()
        print(f'Operating System: {self.os}')

    def phone_ring_sound(self):
        return 'samsung phone sound'

samsung_1 = Samsung(phone_id='1', model='Galaxy 20', brand='Samsung', price=120.000, os='Android')
samsung_1.show_info()
print(samsung_1.phone_ring_sound())

iphone_1 = Iphone(phone_id='2', model='Pro 16 Max', brand='Iphone', price=200.000, airdrop='True')
iphone_1.show_info()
print(iphone_1.phone_ring_sound())


# ! BaseBill atasınıfımız. bill_name: str, value_add_task: float, amount: float object attribute olsun
# * BaseBill sınıfının calculate_bill() olsun. Burada value_add_task * amount
# ? BaseBill sınıfının create_log() olsun. "bill_info.txt" dosyasına, bill name, total amount, payment date yazıcak
# ! WaterBill child class. mill object attribute olsun.
# * NaturalGasBill child class. m3 object attribute olsun
# ? ElectrictyBill chlid class. kw object attribute olsun.
from datetime import datetime

class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.amount = amount
        self.value_add_task = value_add_task
        self.bill_name = bill_name

    def calculate_bill(self) -> float:
        return self.value_add_task * self.amount

    def create_log(self):
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(
                f'Bill Name: {self.bill_name}\n'
                f'Total Amount: {self.calculate_bill()}\n'
                f'Payment Date: {datetime.now()}\n'
                f'================================\n'
            )
        print(f'{self.bill_name} payment.')

class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: int):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

    def calculate_bill(self) -> float:
        return super().calculate_bill() * self.mill

class NaturalGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

    def calculate_bill(self) -> float:
        return  super().calculate_bill() * self.m3

class ElectricityBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw

    def calculate_bill(self) -> float:
        return  super().calculate_bill() * self.kw

water_bill = WaterBill(bill_name='ISKI', value_add_task=25.5, amount=45.7, mill=100)
water_bill.create_log()

naturel_gas_bill = NaturalGasBill(bill_name='IGDAŞ', value_add_task=45.6, amount=89.9, m3=120)
naturel_gas_bill.create_log()

