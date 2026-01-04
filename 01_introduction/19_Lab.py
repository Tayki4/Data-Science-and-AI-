
#! Decorator

# def my_decorator(func):
#     def wrapper():
#         print('Bazı işler burada çalıaşcak..!')
#         func()
#         print('belki bazı işlerde burada çalışacak..!')
    
#     return wrapper

# @my_decorator
# def hello():
#     print('Merhaba')

# hello()

# from math import pow, factorial
# from time import time_ns

# def calculate_time_execution(func):
#     def wrapper(*args, **kwargs):
#         start_time = time_ns()
#         func(*args, **kwargs)
#         end_time = time_ns()
#         print(f'Perfomace: {end_time - start_time} ns')
    
#     return wrapper

# @calculate_time_execution
# def calculate_pow(x: int, y: int):
#     print(f'Sonuç: {pow(x, y)}')

# @calculate_time_execution
# def calculate_factorial(number: int):
#     print(f'Sonuç: {factorial(number)}')

# @calculate_time_execution
# def sum_number(x: int, y: int, z: int):
#     print(f'Sonuç: {x + y + z}')

# calculate_pow(x=2, y=3)
# calculate_factorial(number=5)
# sum_number(x=1, y=2, z=3)


# from datetime import datetime

# def log_info(func):
#     def wrapper(*args, **kwargs):
#         print(
#             '===============================\n'
#             f'Yapılan İşlem: {func.__name__}\n'
#             f'İşlem Tarihi: {datetime.now()}\n'
#         )
#         return func(*args, **kwargs)
#     return wrapper

# @log_info
# def para_cekme(hesap_no: str, bakiye: int, cekilecek_tutar: int):
#     bakiye -= cekilecek_tutar
#     return (
#         f'Bu {hesap_no}, para çekildi..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
    
# @log_info
# def para_yatırma(hesap_no: str, bakiye: int, yatırılacak_tutar: int):
#     bakiye += yatırılacak_tutar
#     return (
#         f'Bu {hesap_no}, para yatırıldı..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )
    
# print(
#     para_cekme(
#         hesap_no='1234456',
#         bakiye=1000,
#         cekilecek_tutar=500
#     )
# )

# print(
#     para_yatırma(
#         hesap_no='1234456',
#         bakiye=1000,
#         yatırılacak_tutar=500
#     )
# )

def is_manager(func):
    def wrapper(user):
        if user.get('role') in ['manager', 'general manager']:
            return func(user)
        else:
            print(f'{user.get("username")} - {user.get("role")}\nRaporu görüntüleme yetkiniz bulunmamaktadır..!')
    return wrapper

@is_manager
def get_report(user):
    print(f'{user.get("username")} - {user.get("role")}\nReport görüntülendi..!')

user_1 = {
    'username': 'Hasan Cobanoğlu',
    'role': 'manager'
}

user_2 = {
    'username': 'Rana Nur Ceylan',
    'role': 'general manager'
}

user_3 = {
    'username': 'Burak Yılmaz',
    'role': 'Irgat'
}

get_report(user_1)
get_report(user_3)
get_report(user_2)
