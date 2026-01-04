
#! loops 
#? while for 

# counter = 0 
# while counter <= 9:
#     print(counter)
#     counter = counter + 1 

#! 0 100 arasu sayukaru yazdır ekrana

# a = 0 
# while a <= 100:
#     print(a)
#     a = a + 1

#! 100-0
# counter = 100 
# while counter >= 0:
#     print(counter, end='-')
#     counter -= 1

#! 0 100 arasında kac tane cift kac tane tek sayı var sapta ve ekrana yazdir.

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

#! minik bir hesap makinesi.
#? kull istedigi kadar islem yapabilecek (infinitive loop)
#* sadece 2 tam sayi üzerinden islemy apacak
#todo 4 islem ecerecek hesap makinasi
#? islem turune göre gerekli islem yapılacak. 
#* kull islem turu olarak 'e' girerse uygulama duraccak.
#! try except olacak
#? match- case
#todo login olunacak. username password kisinin 3 hakki var.

# counter = 3 
# while counter >= 1:
#     username = input('Username ')
#     password = input('Password ')

#     if username == 'savage' and password == '123' :
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

#                 except(TypeError,ZeroDivisionError, ValueError) as err:
#                     print('err')
#             else:
#                 print('Application has been closed..!')
#                 break

#     else:
#         print('Invalid username or password..!')

#     counter -= 1
# else:
#     print('Invalid username or password..!')

#! while loop kull faktöriyel hesapla
# x = int(input('sayı'))

# if x < 0: 
#     print('Sıfırda küçük sayıların faktöriyeli hesaplanmaz..!')
# elif x == 0 or x ==1:
#     print('Faktöriyel: 1')
# else:
#     sonuc = 1

#     while x > 0:
#         sonuc *= x 
#         x -= 1
        
#     print(f'Faktöriyel: {sonuc}')

#kull bir sayi alalim bu sayı asal mı degil mi 
# sayi = int(input('sayı:  '))

# if sayi < 2:
#         print("2'den kucuk sayıların asallık durumu kontrol edilmez..!")
# else:
#     is_prime = True
#     sayac = 2
#     while sayac < sayi:
#         if sayi % sayac == 0:
#             is_prime = False
#             break
#         sayac += 1
    
# if is_prime:   # is_prime is true
#     print(f'{sayi} asaldir..!')
# else:
#     print(f'{sayi} asal degildir..!')
       

#!for loop 
#? in ve range()

# in operetoru
# print('b' in 'burak')
# print('z' in 'burak')

# not in 
# print('z' not in 'burak')
# print('z' not in 'burak')

# range()
# for i in range(10):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(10,20,2):
#     print(i)