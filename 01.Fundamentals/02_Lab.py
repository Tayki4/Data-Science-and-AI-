
#! Karar Mekanizmaları (If-Else, Match-Case)
# x = int(input('Tam Sayı: '))
# y = int(input('Tam Sayı: '))

# if x > y:
#     print(f'{x} büyüktür..!')
# elif x == y:
#     print(f'{x}, {y} değerine eşittir..!')
# else:
#     print(f'{y} büyüktür..!')

#todo: Kullanıcıdan bir tane tam sayı alalım. bu sayı pozitif mi? negatif mi? nötr mü? bakalım. sonucu ekrana yazdıralım.
# x = int(input('Tam Sayı: '))

# if x > 0:
#     print(f'{x} pozitif..!')
# elif x == 0:
#     print(f'{x} nötr..!')
# else:
#     print(f'{x} negatif..!')

#todo: Kullanıcıdan alınan sayı çifti mi tek mi?
# x = int(input('Tam Sayı: '))

# result = x % 2

# if result == 0:
#     print(f'{x} çift..!')
# else:
#     print(f'{x} tek..!')

#todo: Kullanıcıdan mevsim bilgisi alıyoruz.
#? kullanıcıdan gelen mevsim bilgisine göre ayları ekrana yazdırıyoruz.
# season = input('Type a season: ').lower()

# if season == 'winter':
#     print('December-Januray-February')
# elif season == 'spring':
#     print('March-April-May')
# elif season == 'summer':
#     print('June-July-August')
# elif season == 'autumn':
#     print('September-Octobar-November')
# else:
#     print('There is no such season. Are you allen?')

# and - or
#todo: Kullanıcıdan 3 adet sayı alalım. sayılardan büyük olanı ekrana yazdıralım. a > b, a > c ise a en büyük
# a = int(input('Tam Sayı: '))
# b = int(input('Tam Sayı: '))
# c = int(input('Tam Sayı: '))

# if a > b and a > c:
#     print(f'{a} en büyüktür.')
# elif b > a and b > c:
#     print(f'{b} en büyüktür.')
# elif c > a and c > b:
#     print(f'{c} en büyüktür.')
# else:
#     print('Sayılar birbirlerine eşit olabilir.')

#todo: Kullanıcıdan bir adet ürün adı alıyoruz.
#? ürün adı, domates, biber, patlican ise sebze reyonuna gidiniz
#* ürün adı, notebook, kindle, tablet ise teknoloji reyonuna gidiniz
#! ürün adı, şampuan, sabun, parfüm ise kozmetik reyonuna gidiniz.
# product = input('Type a product name: ').lower()

# if product == 'domates' or product == 'biber' or product == 'patlican':
#     print('Sebze reyonuna git..!')
# elif product == 'kindle' or product == 'notebook' or product == 'tablet':
#     print('Teknoloji reyonuna git..!')
# elif product == 'şampuan' or product == 'sabun' or product == 'parfüm':
#     print('Kozmetik reyonu git..!')
# else:
#     print('Aradığını ürün bulunmamaktadır..!')

#todo: kullanıcıdan username ve password allalım. username, beast, password 123 ise hoşgeldiniz, değilse hatalı kullanıcı bilgileri.
# username = input('User name: ')
# password = input('Password: ')

# if username == 'beast' and password == '123':
#     print('Hoşgeldiniz..!')
# else:
#     print('Hatalı kullanıcı bilgileri..!')

#! Nested IF (iç İçe If)
# x= 0
# y=0
# if x > y:
#     z  = x + y
#     if z > 10:
#         pass
#     elif z == 0:
#         pass
#     else:
#         if x > 0 and y > 0:
#             pass

# kullanıcı uygulamaya login olacak
# kullanıcı kilo, boy bilgisini girecek bmi göre kullanıcıya durumu feedback 
# username = input("User name: ")
# password =input("Password:")

# if username =='beast' and password =='123':
#     print(f'{username}, welcome..!')
    
#     height = float(input('Height: '))
#     weight = float(input("Weight: "))
    
#     bmi = weight / (height ** 2)
#     status = ''
    
#     if 0 < bmi <= 18.5: #! 0 < bmi and bmi <= 18.5
#         status = 'lean'
#     elif 18.6 <= bmi <= 24.9: #? 18.6 <= bmi and bmi <= 24.9
#         status = 'normal'
#     elif 25 <= bmi <= 29.9:
#         status = 'weighted'
#     elif 30 <= bmi <= 34.9:
#         status = 'overweighted'
#     elif 35 <= bmi <= 39.9:
#         status = 'obesity'
    
#     print(
#         f'User Name: {username}\n'
#         f'BMI: {bmi}\n'
#         f'Status: {status}')
# else:
#     print('Invalid credantials..!')


#todo: Bir kitap 5 TL.
#? Kullanıcıdan satın aldığı kitap sayısını alalım
#* Alınan kitap sayısı 1 ile 5 arasında ise yüzde 5 iskonto
#! Alınan kitap sayısı 6 ile 10 arasında ise yüzde 10 iskonto
#? Alınan kitap sayısı 11 ile 15 arasında ise yüzde 15 iskonto
#* Alınan kitap sayısı 16 ile 20 arasında ise yüzde 20 iskonto
#! toplam fiyata alınan kitap sayısına göre indirim uygulanarak ödencek toplam tutar ekrana yazdırılsın
# kitap = 5
# kitap_miktarı = int(input('Satın Alınan Kitap Sayısı: '))
# if kitap_miktarı <= 0:
#     print('Eksi kitap sayısı olamaz.')
# else:
#     if 1 <= kitap_miktarı <= 5:
#         print(f'Ödenecek Tutar: {kitap * kitap_miktarı * 0.95}')
#     elif 6 <= kitap_miktarı <= 10:
#         print(f'Ödenecek Tutar: {kitap * kitap_miktarı * 0.90}')
#     elif 11 <= kitap_miktarı <= 15:
#         print(f'Ödenecek Tutar: {kitap * kitap_miktarı * 0.85}')
#     elif 16 <= kitap_miktarı <= 20:
#         print(f'Ödenecek Tutar: {kitap * kitap_miktarı * 0.80}')
#     else:
#         print('En fazla 20 kitap satın alabilirsiniz.')

#todo: kullanıcıdan araç türü ve hız alalım
#? araç türü otomobil, hız 60'tan büyükse cezalı değilse ceza yok
#* araç türü kamyon, hız 40'tan büyükse cezalı değilse ceza yok
#! araç türü motorsiklet, hız 70'tan büyükse cezalı değilse ceza yok
# vehicle = input('Type your vehicle: ').lower()
# speed = float(input('Speed: '))

# if speed > 0:
#     if vehicle == 'car':
#         if speed >= 60:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'truck':
#         if speed >= 40:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     elif vehicle == 'motorcycle':
#         if speed >= 70:
#             print('Penalty..!')
#         else:
#             print('No penalty..!')
#     else:
#         print('Please type a proper vehicle type..!')
# else:
#     print('Invalid speed value..!')


# match-case
#todo: Kullanıcıdan mevsim bilgisi alıyoruz.
#? kullanıcıdan gelen mevsim bilgisine göre ayları ekrana yazdırıyoruz.
# season = input('Type a season: ').lower()

# match season:
#     case 'winter':
#         print('December-Januray-February')
#     case 'spring':
#         print('March-April-May')
#     case 'summer':
#         print('June-July-August')
#     case 'autumn' | 'fall': # or ifadesi için match-case içerisinde "|" pipe sembolünü kullanıyoruz
#         print('September-Octobar-November')
#     case _:
#         print('There is no such season..!')

#! match-case, durum (status) kontrolü için sıklıkla tercih edilir.
# boxing_gloves_status = 'Passive'

# match boxing_gloves_status:
#     case 'Active':
#         pass
#     case 'Passive':
#         pass
#     case 'Modified':
#         pass
#     case _:
#         print('None')

#! match-case içerisinde "and" kullanımı

# kitap_miktarı = int(input('Satın Alınan Kitap Sayısı: '))
# if kitap_miktarı <= 0:
#     print('Eksi kitap sayısı olamaz.')
# else:
#     match kitap_miktarı:
#         case n if 1 <= kitap_miktarı <= 5:
#             print(f'Ödenecek Tutar: {5 * kitap_miktarı * 0.95}')
#         case n if 6 <= kitap_miktarı <= 10:
#             print(f'Ödenecek Tutar: {5 * kitap_miktarı * 0.90}')
#         case n if 11 <= kitap_miktarı <= 15:
#             print(f'Ödenecek Tutar: {5 * kitap_miktarı * 0.85}')
#         case n if 16 <= kitap_miktarı <= 20:
#             print(f'Ödenecek Tutar: {5 * kitap_miktarı * 0.80}')
#         case _:
#             print('En fazla 20 kitap satın alabilirsiniz.')

#todo: Okuma Ödevi --> 1. match-case vs if-else, 2. try-except-finally güzelce çalışıalcak, 3. while loop çok iyi çalışın

#! Ternery If
# age = int(input('Age: '))

# status = 'adult' if age >= 18 else 'child'
# print(status)

# number = int(input('Number: '))
# print(f"Status: {'positive' if number > 0 else 'negative'}")

# #! Nested Ternary If
# exam_score = 75
# result = 'AA' if exam_score >= 80 else 'BB' if exam_score >= 60 else 'CC'
# print(f'Result: {result}')

# # 246 satırdaki nested ternary if, normal yazılmış hali
# if exam_score >= 80:
#     print('AA')
# else:
#     if exam_score >= 60:
#         print('BB')
#     else:
#         print('CC')

# Try-Except-Finally
# try:
#     bolunen = int(input('Bolunen: '))
#     bolen = int(input('Bolen: '))
#     sonuc = bolunen / bolen
#     print(f'Sonuc: {sonuc}')
# except (ZeroDivisionError, ValueError) as err:
#     print('Bir tam sayı sıfıra bölünemez..!')
#     #! kendimize mail dönderiyoruz
#     #* log --> uygulamada ne oldu ne bitti bunların kayıtlarının tutulmasına "log"
#     print(f'{err}')
# finally:
#     print('Ne olursa olsun çalışırım')


#! Bazı durumlarda bilerek Exception kendimiz raise ederiz
try:
    mail_address = input('Type mail address: ')
    
    if '@' not in mail_address:
        raise TypeError('Mail address have to contains "@" symbol..!')
except TypeError as err:
    print(err)

