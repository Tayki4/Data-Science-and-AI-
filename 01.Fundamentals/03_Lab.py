
#! LOOPS
#? While - For

# counter = 0
# while counter <= 9:
#     print(counter)
#     counter = counter + 1 # counter += 1


#! 0-100 arasındaki sayıları ekrana yazdıralım
# counter = 0
# while counter <= 100:
#     print(counter, end='-')
#     counter += 1


#! 100-0 arasındaki sayıları ekrana yazdıralım
# counter = 100
# while counter >= 0:
#     print(counter, end='-')
#     counter -= 1

#! 0-100 arasında kaç tane çift kaç tane tek sayı var saptayalım ve ekrana yazdıralım.
# counter = 0
# even = 0
# odd = 0
# while counter <= 100:
#     if counter % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     counter += 1

# print(f'Even Count: {even}\nOdd Count: {odd}')

#! 0-100 arasında ki çift ve tek sayıların toplamlarını bulup ekrana yazdıralım
# counter = 0
# even = 0
# odd = 0
# while counter <= 100:
#     if counter % 2 == 0:
#         even += counter
#     else:
#         odd += counter
#     counter += 1

# print(f'Even Count: {even}\nOdd Count: {odd}')

#! Minnak bir hesap makinası yapalım
#? kullanıcı istediği kadar işlem yapabilecek. Hint --> infinitive loop
#* sadece 2 tam sayı üzerinden işlem yapılacak
#todo 4 işlem içericek hesap makinası
#? İşlem türüne göre gerekli işlem yaptırılacak. Hint --> '+', '-' etc
#* kullanıcı işlem türü olarak 'e' girerse uygulama durdurulacak
#! try-except olacak
#? match-case
#todo login olunacak. username, password, kişinin 3 hakkı olacak.
# counter = 3
# while counter >= 1:
#     print('Login Page')
#     username = input('Username: ')
#     password = input('Password: ')
    
#     if username == 'savage' and password == '123':
#         print(f'Welcome {username}')
#         while True:
#             process = input('Process: ')
#             if process != 'e':
#                 try:
#                     number_1 = float(input('First Number: '))
#                     number_2 = float(input('Second Number: '))
#                     match process:
#                         case '+':
#                             print(f'Result: {number_1 + number_2}')
#                         case '-':
#                             print(f'Result: {number_1 - number_2}')
#                         case '*':
#                             print(f'Result: {number_1 * number_2}')
#                         case '/':
#                             print(f'Result: {number_1 / number_2}')
#                         case _:
#                             print('Invalid process type..!')
#                 except (TypeError, ZeroDivisionError, ValueError) as err:
#                     print(err)
#             else:
#                 print('Application has been closing..!')
#                 break
#     else:
#         print('Invalid username or password..!')
    
#     counter -= 1
# else:
#     print('Your account suspendent..!')

# while loop kullanarak bana faktöriyel hesaplayın
# x = int(input('Sayı: '))

# if x < 0:
#     print('Sıfırdan küçük sayıların faktöriyeli hesaplanmaz..!')
# elif x == 0 or x == 1:
#     print('Faktöriyel: 1')
# else:
#     sonuc = 1
    
#     while x > 0:
#         sonuc *= x  # sonuc = sonuc * x
#         x -= 1
    
#     print(f'Faktöriyel: {sonuc}')


# kullanıcıdan bir sayı alalım. bu sayı asal mı değil mi kontrolünü yapalım ve sonucu ekrana basalım
# sayi = int(input('Sayı: '))

# if sayi < 2:
#     print("2'den küçük sayıların asallık durumu kontrol edilmez..!")
# else:
#     is_prime = True
    
#     sayac = 2
#     while sayac < sayi:
#         if sayi % sayac == 0:
#             is_prime = False
#             break
#         sayac += 1
    
#     if is_prime: # is_prime is True:
#         print(f'{sayi} asaldir..!')
#     else:
#         print(f'{sayi} asal değildir..!')