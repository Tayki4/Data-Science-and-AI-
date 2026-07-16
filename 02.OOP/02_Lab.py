
#! Inheritance (Kalıtım)

#todo: Single Inheritance
class Human:
    def __init__(self, full_name: str, weight: float, height: float):
        self.full_name = full_name
        self.weight = weight
        self.height = height
    
    def show_info(self):
        return self.__dict__

class FootSoldier(Human):
    pass

class Knight(Human):
    pass

fs_1 = FootSoldier(full_name='burak', weight=100.03, height=1.83)
print(fs_1.show_info())

k_1 = Knight(full_name='hakan', weight=165, height=2.01)
print(k_1.show_info())


# todo: Multiple Inheritance
class YuzebilenKus:
    def yuzebilmek(self):
        print('Yüzebilir kuşlar')

class UcabilenKus:
    def ucabilmek(self):
        print('Uçabilen kuşlar')

class YuruyenKus:
    def yurumek(self):
        print('Yürüyebilen kuşlar')


class Penguen(YuzebilenKus, YuruyenKus):
    pass

class Tavuk(YuruyenKus):
    pass

class Kartal(UcabilenKus, YuzebilenKus):
    pass

penguen_1 = Penguen()
penguen_1.yurumek()
penguen_1.yuzebilmek()