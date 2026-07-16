

# Abstraction

from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass

# region Example - 1
# class BaseMuzikAleti:
#     def __init__(self, model: str, brand: str):
#         self.model = model
#         self.brand = brand
#
# class Gitar(BaseMuzikAleti):
#     def __init__(self, model: str, brand: str, tel: str):
#         super().__init__(model, brand)
#         self.tel = tel
#
# class Keman(BaseMuzikAleti):
#     def __init__(self, model: str, brand: str, kasa: str):
#         super().__init__(model, brand)
#         self.kasa = kasa
#
# class BaseService(ABC):
#     @abstractmethod
#     def call_sound(self) -> str:
#         pass
#
#     def harmonize(self):
#         return 'harmonize completed..!'
#
# class ViolinService(BaseService):
#     def call_sound(self) -> str:
#         return 'Violin Sound'
#
# class GuitarService(BaseService):
#     def call_sound(self) -> str:
#         return 'Guitar Sound'
#
#     def harmonize(self):
#         return 'guitar harmonize incompleted..!'
#
# k1 = ViolinService()
# print(k1.call_sound())
#
# g1 = GuitarService()
# print(g1.harmonize())
# print(g1.call_sound())
# endregion

# region Example - 2
# @dataclass
# class BaseBill:
#     bill_name: str
#     value_add_task: float
#     amount: float
#
# @dataclass
# class WaterBill(BaseBill):
#     mill: int
#
# @dataclass
# class NaturalGasBill(BaseBill):
#     m3: float
#
# @dataclass
# class ElectricityBill(BaseBill):
#     kw: float
#
#
# class BaseService(ABC):
#     @abstractmethod
#     def calculate_bill(self, bill: BaseBill) -> float:
#         pass
#
#     def create_log(self, bill: BaseBill, calculate_bill_result: float) -> str:
#         with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
#             file.write(
#                 f'Bill Name: {bill.bill_name}\n'
#                 f'Total Amount: {calculate_bill_result}\n'
#                 f'Payment Date: {datetime.now()}\n'
#                 f'================================\n'
#             )
#         return f'{bill.bill_name} payment.'
#
# class WaterBillService(BaseService):
#     def calculate_bill(self, bill: WaterBill) -> float:
#         return bill.value_add_task * bill.amount * bill.mill
#
# class NaturalGasService(BaseService):
#     def calculate_bill(self, bill: NaturalGasBill) -> float:
#         return bill.value_add_task * bill.amount * bill.m3
#
# class ElectricityService(BaseService):
#     def calculate_bill(self, bill: ElectricityBill) -> float:
#         return bill.value_add_task * bill.amount * bill.kw
#
# water_bill = WaterBill(bill_name='ISKI', value_add_task=25.5, amount=45.7, mill=100)
# water_bill_service = WaterBillService()
# bill_result = water_bill_service.calculate_bill(bill=water_bill)
# msg = water_bill_service.create_log(bill=water_bill, calculate_bill_result=bill_result)
# print(msg)
# endregion

# region Example - 3
# class BaseService(ABC):
#     @abstractmethod
#     def ship_from(self) -> str:
#         pass
#
# class SumatraService(BaseService):
#     def ship_from(self) -> str:
#         return "from Sumatra"
#
# class ColumbiaService(BaseService):
#     def ship_from(self) -> str:
#         return "from Columbia"
#
# class SouthAfricaService(BaseService):
#     def ship_from(self) -> str:
#         return 'from SouthAfrica'
#
# class DefaultService(BaseService):
#     def ship_from(self) -> str:
#         return 'not available'
#
# class Shipment:
#     @staticmethod
#     def shipment_method(month) -> BaseService:
#         if 4 <= month <= 7:
#             return ColumbiaService()
#         elif 8 <= month <= 11:
#             return SumatraService()
#         else:
#             if month == 1 or month == 2 or month == 12:
#                 return SouthAfricaService()
#             else:
#                 return DefaultService()
#
# def main():
#     for month in range(1, 13):
#         product_shipment = Shipment.shipment_method(month)
#         print(f'Coffee beans shipment {product_shipment.ship_from()}')
#
# main()
# endregion

# region Example - 4
class CreditCard:
    def __init__(self):
        self.bank_name = None
        self.card_limit = None
        self.card_type = None
        self.installment_shopping = None

class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()

    @property
    def credit_card(self) -> CreditCard:
        return self._credit_card

    @abstractmethod
    def bank_name_func(self) -> str:pass

    @abstractmethod
    def card_limit_func(self) -> int:pass

    @abstractmethod
    def card_type_func(self) -> str:pass

    @abstractmethod
    def installment_shopping_func(self) -> str:pass

class AmericanExpressCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = 'Garanti'
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 1000000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = 'American Express'
        return self._credit_card.card_type

    def installment_shopping_func(self) -> str:
        self._credit_card.installment_shopping = 'True'
        return self._credit_card.installment_shopping

class VisaCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card

    def bank_name_func(self) -> str:
        self._credit_card.bank_name = 'İş Bankası'
        return self._credit_card.bank_name

    def card_limit_func(self) -> int:
        self._credit_card.card_limit = 10000000
        return self._credit_card.card_limit

    def card_type_func(self) -> str:
        self._credit_card.card_type = 'Visa'
        return self._credit_card.card_type

    def installment_shopping_func(self) -> str:
        self._credit_card.installment_shopping = 'True'
        return self._credit_card.installment_shopping

class Creator:
    @staticmethod
    def create(credit_card_builder: CreditCardBuilder) -> None:
        print(
            f'Bank Name: {credit_card_builder.bank_name_func()}\n'
            f'Card Limit: {credit_card_builder.card_limit_func()}\n'
            f'Card Type: {credit_card_builder.card_type_func()}\n'
            f'Shopping: {credit_card_builder.installment_shopping_func()}\n'
        )

def main():
    Creator.create(credit_card_builder=AmericanExpressCard())
    Creator.create(credit_card_builder=VisaCard())

main()
# endregion

