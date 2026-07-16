
#! Custom Funcs

# def greeting_people():
#     print('Hello..!')


# greeting_people()
# greeting_people()
# greeting_people()
# greeting_people()
# greeting_people()

# def greeting(full_name: str):
#     print(f'hello {full_name}..!')

# greeting(full_name='burak')
# greeting(full_name='hakan')


# def sum_two_number(a: int, b: int):
#     """Bu fonksiyon 2 tane tam sayı toplar.

#     Args:
#         a (int): integer tipinde tam sayı
#         b (int): integer tipinde tam sayı
#     """
#     print(a+b)


# sum_two_number(2, 4)
# sum_two_number(a=3, b=10)
# sum_two_number(a=-1, b=13)

# sum_two_number(
#     a=int(input('Tam Sayı: ')),
#     b=int(input('Tam Sayı: ')),
# )

# #todo: full name ve domain name alalım. kurumsal mail adresi yaratalım
# def create_email(full_name: str, domain_name: str = '@skilledhub.com'):
#     names = full_name.lower().split(' ')
#     print(f'Mail Adress: {names[0]}.{names[-1]}{domain_name}')

# create_email(
#     full_name='Burak Yılmaz',
# )

# create_email(
#     full_name='Adal Su Uygur',
#     domain_name='@xyz.com'
# )

# #todo: 3 tane sayıyı çarpan bir fonksiyon yazın
# def multiply(x: int = 1, y: int = 1, z: int = 1):
#     print(x * y * z)

# multiply(x=2, y=3)

# #todo: daire alanını hesaplın
# def calculate_area_disk(radius: int | float, pi: float = 3.14):
#     """_summary_

#     Args:
#         radius (int | float): _description_
#         pi (float, optional): _description_. Defaults to 3.14.
#     """
#     print(radius * pi)


# calculate_area_disk(
#     radius=1.2
# )

# Returnable (Değer Döndüren) Fonksiyonlar
# def pow_number(x: int, pow: int) -> int:
#     """Bir tamsayının kuvvetini hesaplayan fonksiyon

#     Args:
#         x (int): kuveeti alınacak sayı, integer
#         pow (int): kuvvet değeri, integer

#     Returns:
#         int: sonuç
#     """
#     return x ** pow

# result = pow_number(x=3, pow=2)
# result_1 = pow_number(x=2, pow=2)
# print(result)
# print(result_1)

# #todo: kullanıcıdan alınan 3 adet sayıyı toplayan fonksiyonu yazın
# def sum_numbers(x: int = 0, y: int = 0, z: int = 0) -> int:
#     return x + y + z

# sum_result = sum_numbers(
#     x=int(input('Tam Sayı: ')),
#     y=int(input('Tam Sayı: ')),
#     z=int(input('Tam Sayı: '))
# )

# print(sum_result)

#todo: bir söz öbeğinde ki tekrar eden kelimelerden arındırarak string formatında çıktı veren fonksiyonu yazalım
#? Sample Input --> 'merhaba ben burak burak ben merhaba'
#* Sample Output --> 'merhaba ben burak'
# def remove_duplicate_word(sentence: str) -> str:
    # Path I
    # lst = []
    
    # for item in sentence.split():
    #     if item not in lst:
    #         lst.append(item)
    
    # str_output = ' '.join(lst)
    
    # return str_output

    # Path II
    # lst_1 = [item for item in sentence.split()]
    # lst_2 = set(lst_1)
    # str_output = ' '.join(lst_2)
    
    # return str_output

    # Path III (Path II) aynı mantık ama burada tek atıyoruz daha bir artistlik duruyor kodlar
#     return ' '.join(set([item for item in sentence.split()]))

# result = remove_duplicate_word(sentence='merhaba ben burak burak ben merhaba')

# print(result)

#! SRP (Single Responsibility Principle) ve SOC (Seperation of Concern)
#todo: kullanıcıdan üretilecek rastgele sayı miktarın ve end point alalım. çift olanları even_lst tek olanları odd_lst ekleyerek çıktı verelim.
# from random import randint

# def number_generator(amount: int, start_point: int, end_point: int) -> list[int]:
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]

# def find_even_odd(number_lst: list[int]):
#     even_lst = []
#     odd_lst = []
    
#     for i in number_lst:
#         if i % 2 == 0:
#             even_lst.append(i)
#         else:
#             odd_lst.append(i)
    
#     return even_lst, odd_lst

# nbr_generator = number_generator(amount=100, start_point=0, end_point=9)

# even_list, odd_list = find_even_odd(number_lst=nbr_generator)

# print(
#     f'Even List: {even_list}\n'
#     f'Odd List: {odd_list}'
# )

#! rakamlardan oluşan bir liste generate edin.
#? bu liste içerisinde bulunan rakamların geçme sıklılığı bulan ve aşağıdaki yapı return eden fonksiyonu yazın
# {
#     1: 10,
#     2: 30,
#     3: 12, ....
# }

# from random import randint

# def number_generator(amount: int, start_point: int, end_point: int) -> list[int]:
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]


# def find_frequnacy(numbers: list[int]) -> dict[int, int]:
#     frequancy = {}
    
#     for number in numbers:
#         if number in frequancy.keys():
#             frequancy[number] += 1
#         else:
#             frequancy[number] = 1
    
#     return frequancy

# nbr_generator = number_generator(amount=100, start_point=0, end_point=9)

# result = find_frequnacy(numbers=nbr_generator)

# print(result)

#todo: 1. Sign In ve Sign Up
#! SRP (Single Responsibility Principle) ve SOC (Seperation of Concern)
#* Sign Up işleminde kullanıcının girdiği password valid mi? email valid mi? kontrol edilecek ve bu kurallardan geçerse üyelik işlemi tamamlanacak
#? Sign In yine password ve email login olacak.
#todo: tüm bu problem main() fonksiyonu içinde çalışacak
#! Aşağıda Sample Data Structe 
users = {
    'xyz.xyz@skilledhub.com': 'pwd',
    'qwe.qwe@skilledhub.com': '987',
}

def is_pwd_valid(password: str) -> bool:
    ch_set = set(password)
    
    result = (
        any(ch.isupper() for ch in ch_set) and
        any(ch.islower() for ch in ch_set) and
        any(ch.isdigit() for ch in ch_set) and
        any(not ch.isalnum() for ch in ch_set)
    )
    
    return result

def is_mail_valid(mail_address: str) -> bool:
    try:
        if '@' not in mail_address:
            raise TypeError('The mail address must contaion the "@" symbol...!')
        
        if mail_address in users.keys():
            raise ValueError('This email address already has been taken..!')
        
        return True
    except (TypeError, ValueError) as err:
        print(err)
        return False

def sign_in(mail_address: str, password: str) -> str:
    for key, values in users.items():
        if key == mail_address and values == password:
            return f'Welcome, {mail_address}..!'
    return 'Invalid Credentials..!'

def sign_up(mail_address: str, password: str) -> str:
    if is_pwd_valid(password=password) and is_mail_valid(mail_address=mail_address):
        users[mail_address] = password
        return 'Your membership has been completed..!'
    else:
        return 'Invalid credentials..!'

def main():
    while True:
        process = input('Type process name: ')
        
        match process:
            case 'sign in':
                print(
                    sign_in(
                        mail_address=input('Mail Address: '),
                        password=input('Password: ')
                    )
                )
            case 'sign up':
                print(
                    sign_up(
                        mail_address=input('Mail Address: '),
                        password=input('Password: ')
                    )
                )
            case _:
                print('Type a valid process name..!')

main()