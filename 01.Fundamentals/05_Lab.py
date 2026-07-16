

#! List
# lst = ['burak', 12, True, 'hakan', 3.14, False]
# print(lst[0])
# print(lst[3])

# boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', 'Evender Holyfiled', 'George Foreman']
# print(boxers)

# # region Add New Item
# # Listenin sonuna 'Rocky Marciano'
# boxers.append('Rocky Marciano')
# print(boxers)
# # endregion

# # region Add New Item Spesific Index
# # Kullanıcıdan alınan boksör ismini yine kullanıcıdan alınan index değerine yazdıralım
# # boxer_name = input('Boxer Name: ')
# # index_value = int(input('Index Value: '))
# # boxers.insert(index_value, boxer_name)
# # print(boxers)
# # endregion

# # region Merge Two Lists
# royal_division = ['Antony Jasua', 'Tyson Fury', 'Deantony Wilder']
# boxers.extend(royal_division)
# print(boxers)
# # endregion

# # region Read An Item
# # Boxers listesinin 2. indexsinde bulunan veriyi ekrana basın
# print(boxers[2])
# # endregion

# # region Update Item
# # 5. index'te bulunan item "Joe Frazeir" ile değiştirin
# boxers[5] = 'Joe Frazeir'
# print(boxers)
# # endregion

# # region Remevo Item By Index
# # 0. index elemanı sileim
# boxers.pop(0)
# print(boxers)
# # endregion

# # region Remevo Item By Itself
# # Lenox Lewis silelim
# boxers.remove('Lenox Lewis')
# print(boxers)
# endregion

# for boxer in boxers:
#     print(boxer)

# for i in range(len(boxers)):
#     print(f'{i}. indexte ki değer --> {boxers[i]}')

# for ch in 'burak':
#     print(ch, end='-')

# for i in range(len('burak')):
#     print(i)

#! users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'Kerim Abdurrahman Burak YIlmaz']
#? users listesindeki kullanıcılardan kurumsal mail adresi craft ediyoruz.
#* sample mail address --> rana.ceylan@outlook.com
#todo: craft mail address, mail_address listesine eklenerek ekrana basılacak
#? Hint: split(), bir listenin uzunluğu ne olursa olsun son elemanına nasıl get ederim

# users = ['Burak Yılmaz', 'Rana Nur Ceylan', 'İpek Yılmaz', 'Kerim Abdurrahman Burak Yılmaz']
# mail_addresses = []
# domain_name = '@outlook.com'

# for user in users:
#     user_names = user.lower().split(' ')
#     mail_address = f'{user_names[0]}.{user_names[-1]}{domain_name}'
#     mail_addresses.append(mail_address)

# print(mail_addresses)


#! end-user bir söz öbeği alalım
#? sample --> buRa1k _Ayi?lm2aZu
#* sesli harfleri --> sesli_herfler = []
#* sesssiz harfleri --> sessiz_harfler = []
#* hazım hatalarını --> typo_characters = []
#* space karekteri ignore edilecek.
#* ilgili listelerdeki hiç bir eleman tekrar etemeyecek
# sesli_herfler = []
# sessiz_harfler = []
# typo_characters = []

# word = input('Type something: ')

# for ch in word.lower():
#     if ch.isalpha():
#         if ch not in sesli_herfler and ch not in sessiz_harfler:
#             if ch in 'aeıioöuü':
#                 sesli_herfler.append(ch)
#             else:
#                 sessiz_harfler.append(ch)
#         else:
#             continue
#     else:
#         if ch == ' ':
#             continue
#         typo_characters.append(ch)

# print(sesli_herfler)
# print(sessiz_harfler)
# print(typo_characters)

# lst_1 ve lst_2 içerisine rastegele 10 tane sayı üretip doldurun
# doldurma işlemini index mantığına göre yapın. 
# örneğin lst_1[0] + lst_2[0] toplanarak lst_3 ilgili index'sine yazılacak
# her şey tek bir for loop içerisinde çözülecek
# sayılar 0 ile 100 arasında üretilsin
# from random import randint

# lst_1 = []
# lst_2 = []
# lst_3 = []

# for i in range(10):
#     lst_1.insert(i, randint(a=0, b=100))
#     lst_2.insert(i, randint(a=0, b=100))
    
#     lst_3.insert(i, lst_1[i] + lst_2[i])

# print(lst_1)
# print(lst_2)
# print(lst_3)

# ilceler = [
#     ['Sarıyer'],
#     ['Etiler', 'Nispetiye', 'Ulus'],
#     ['Suadiye', ['Feneryolu', 'Erenköy']],
#     [['Beşiktaş', 'Maçka'], 'Harbiye', ['Naşantaşı']]
# ]

# print(ilceler[1][2])
# print(ilceler[0][0])
# print(ilceler[2][1][0])
# print(ilceler[3][1])
# print(ilceler[3][0][1])

#! Slicing (Dilimleme)
# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# print(fruits[2:7])
# print(fruits[:3])
# print(fruits[1::2])
# print(fruits[::4])
# print(fruits[::-1])
# print(fruits[::-2])
# print(fruits[10::-3])

#! Unpacking - Unboxing
# my_family = [
#     ['Burak Yılmaz', 36, 'Developer'],
#     ['Hakan Yılmaz', 39, 'Chemist'],
#     ['İpek Yılmaz', 41, 'Art Historian']
# ]

# for full_name, age, occupation in my_family:
#     print(
#         f'Full Name: {full_name}\n'
#         f'Age: {age}\n'
#         f'Occupation: {occupation}'
#     )
# kullanıcı login olacak
# register olsun
# bütün ürünlerin toplam fiyatı nedir
# ürün adı laptop olan ürünlerin fiyatlarını toplayalım
# kullanıcı ürün search 
# fiyatı 200 TL altında olan ürünler listelensin

# users = [
#     ['beast', '123'],
#     ['bear', '987'],
#     ['keko', '567'],
# ]

# products = [
#     ["Laptop", 850],
#     ["Smartphone", 499],
#     ["Headphones", 79],
#     ["Keyboard", 45],
#     ["Monitor", 220],
#     ["Mouse", 25],
#     ["Smartwatch", 150],
#     ["Tablet", 310],
#     ["External Hard Drive", 95],
#     ["Webcam", 60],
#     ["Laptop", 856],
# ]


# while True:
#     first_process = input('Sign In --> 1\nSign Up -- 2\nTuşlayınız: ')
    
#     match first_process:
#         case '1':
#             kullanici_adi = input('User Name: ')
#             sifre = input('Password: ')
            
#             is_success = False
#             for user in users:
#                 if user[0] == kullanici_adi and user[1] == sifre:
#                     is_success = True
#                     break
            
#             if is_success:
#                 print(f'Giriş başarılı..!\nHoşgeldiniz, {kullanici_adi}')
#                 while True:
#                     second_process = input('İşlem Adı Giriniz: ')
                    
#                     match second_process:
#                         case 'toplam fiyat':
#                             total = 0
#                             for product in products:
#                                 total += product[1]
#                             print(f'Toplam Fiyatlar: {total}')
#                         case 'laptop toplam fiyat':
#                             total = 0
#                             for product in products:
#                                 if product[0] == 'Laptop':
#                                     total += product[1]
#                             print(f'Toplam Fiyatlar: {total}')
#                         case 'ürün ara':
#                             urun_adi = input('Ürün adı giriniz: ')
#                             for product in products:
#                                 if product[0] == urun_adi:
#                                     print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
#                             else:
#                                 print('Aradığınız ürün bulunmamaktadır..!')
#                         case 'fiyat aralığına göre ara':
#                             alt = int(input('Alt limit fiyato: '))
#                             ust = int(input('Üst limit fiyato: '))
#                             for product in products:
#                                 if product[1] >= alt and product[1] <= ust:
#                                     print(f'Ürün Adı: {product[0]}\nFiyatı: {product[1]}')
#                         case 'çıkış':
#                             print('Uygulama kapatılıyor...!')
#                             break
#                         case _:
#                             print('Lütfen doğru işlem türü giriniz..!')
#             else:
#                 print('Kullanıcı adı yada şifre hatalı..!')
#         case '2':
#             kullanici_adi = input('User Name: ')
#             sifre = input('Password: ')

#             is_exist = False
#             for user in users:
#                 if user[0] == kullanici_adi:
#                     is_exist = True
#                     break

#             if is_exist:
#                 print('Kullanıcı adı zaten var.')
#             else:
#                 new_user = [kullanici_adi, sifre]
#                 users.append(new_user)
#                 print('Üyelik işleminiz tamamlandı.')
#         case _:
#             print('Lütfen uygun işlem numarasını giriniz..!')


# enumarete()
# boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', 'Evender Holyfiled', 'George Foreman']

# for index, item in enumerate(boxers):
#     print(
#         f'Index Value: {index}\n'
#         f'Item Value: {item}'
#     )


# List Comprehensions
# lst = [i for i in range(10)]
# print(lst)

# lst_1 = []
# for i in range(10):
#     lst_1.append(i)
# print(lst_1)

# rastgele üretilmiş 10 tane sayı ile list comprehension yapalım
# from random import randint

# lst = []
# for _ in range(10):
#     lst.append(randint(a=0, b=100))
# print(lst)

# print([randint(a=0, b=100) for _ in range(10)])

# rakamların karesini alıp listeye ekleyelim
# print([i ** 2 for i in range(10)])

# 0 - 100 arasındaki çift sayıları listeye ekleyelim
# lst = [i for i in range(101) if i % 2 == 0]
# print(lst)

# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# print([fruit for fruit in fruits if 'a' in fruit.lower()])

# meyve ismi içerisinde "an" ifadesi geçiyorsa True geçmiyorsa False değerini listeye ekleyelim
# Hint: 'adult' if age >= 18 else 'child'
# print(
#     [True if 'an' in fruit.lower() else False for fruit in fruits]
# )

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print('=========================')

# print(
#     [
#         [f'{i} x {j} = {i * j}']  for i in range(1, 11) for j in range(1, 11)
#     ]
# )

