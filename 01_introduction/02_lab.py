
 #! karar mekanizmaları (if else, match-case)
# x = int(input('tam Sayı: '))
# y = int(input('tam Sayı: '))

# if x > y:
#     print(f'{x} büyüktür..!')
# elif x == y:
#     print(f'{x}, {y} değerine esittir..!')
# else:
#     print(f'{y} büyüktür...!')

#todo: kull bir tane tam sayı a. poz mu neg mi nötr mü bak sonucu yaz.

# x = int(input('tam Sayı: '))
# if x < 0 :
#     print(f'{x} negatiftir..!')
# elif x == 0 :
#     print(f'{x} nötrdür..!')
# else :
#     print(f'{x} pozitiftir..!')    
  
#! kullnıcıdan alınan sayi tek mi cift mi 

# x = int(input("Bir sayi giriniz: "))
# if x % 2 == 0:
#     print("Çift sayi")
# else:
#     print("Tek sayi")

##! (% bu mod almak) (/ veya // bölme)

#? kullanıcıdan gelen mevsim bilg göre ayları ekrana yaz.

# x = (input("Bir mevsim giriniz: ")).lower() # . koyup lower yazarak girilen
# if x == ('winter'):         # her harf kucultuldu büyük harfi farklı algılar
#     print('december-jan-feb')
# elif x == ('spring'):
#     print('march-april-may')
# elif x== ('summer'):
#     print('june-july-august')
# else:
#     print('there is no such season?')      

# and - or , nested if

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

# kullanıcı uyg.. login olmaya calısıyor
# kullanıcı kilo boy big girecek bmi gore kull durumu feedback
# username = input('user name: ')
# password = input('password: ')

# if username =='beast' and password =='123':
#     print(f'{username}, welcome..!')

#     height = float(input('Height '))
#     weight = float(input('Weight: '))

#     bmi = weight / (height ** 2) 
#     status = ''
#     if 0 < bmi <= 18.5: #! 0 < bmi and bmi <= 18.5
#         status = 'lean'
#     elif 18.6 < bmi < 24.9:
#         status = 'normal'
#     elif 25 <= bmi <=29.9:
#         status = 'overweight'
#     elif 30 <= bmi <=34.9:
#         status = 'obesity'
#     elif 35 <=bmi <= 39.9:
#         status = 'jesus'

    
#     print(f'User Name: {username} \n'
#           f'BMI: {bmi}\n'
#           f'Status: {status}'
#          )
        
# else: 
#     print('invalid credantials..!')

#todo: Bir kitap 5 TL.
#? Kullanıcıdan satın aldığı kitap sayısını alalım
#* Alınan kitap sayısı 1 ile 5 arasında ise yüzde 5 iskonto
#! Alınan kitap sayısı 6 ile 10 arasında ise yüzde 10 iskonto
#? Alınan kitap sayısı 11 ile 15 arasında ise yüzde 15 iskonto
#* Alınan kitap sayısı 16 ile 20 arasında ise yüzde 20 iskonto
#! toplam fiyata alınan kitap sayısına göre indirim uygulanarak ödencek toplam tutar ekrana yazdırılsın
#todo: kullanıcıdan araç türü ve hız alalım
#? araç türü otomobil, hız 60'tan büyükse cezalı değilse ceza yok
#* araç türü kamyon, hız 40'tan büyükse cezalı değilse ceza yok
#! araç türü motorsiklet, hız 70'tan büyükse cezalı değilse ceza yok


# kitap = 5
# kitap_miktari = int(input('satin alınan kitap sayısı: '))
# if kitap_miktari <= 0:
#     print('eksi kitap sayısı olamaz')
# else:
#     if 1 <= kitap_miktari <= 5:
#         print(f'ödenecek tutar:{kitap * kitap_miktari * 0.95}')
#     elif  DOLDUR

#     elif  DOLDUR

#     elif  DOLDUR

#     else:
#         print('en fala 20 kitap alabilirsin')

#! match - case
#? mevsim bilg.

# season = input('type a season: ').lower()

# match season:
#     case 'winter':
#         print('december-jan-feb')
#     case 'spring':
#         print('march-april-may')
#     case 'summer':
#         print('june-july-august')
#     case 'autumn' / 'fall':   # or ifadesi icin match-case icersiinde "/" pipe sembolunu kullanıyoruz
#         print('september-october-noverber')
#     case _:
#         print('there is no such a season..!')


#! match case, durum (status) kontrolu icin sıklıkla tercih edilir.
# boxing_gloves_status = 'Passive'

# match boxing_gloves_status:
#     case 'Active':
#         pass
#     case 'Passive':
#         pass
#     case 'Modified':
#         pass
#     case _:
#         print('none')


# kitap_miktari = int(input('satn alınan kitap sayısı: '))
# if kitap_miktari <= 0:
#     print('eksi kitap sayısı olamaz.')
# else:
#     match kitap_miktari:
#         case n if 1 <= kitap_miktari <= 5:
#             print(f'ödenecek tutar: {5 * kitap_miktari * 0.95}')
#         case n if 6 <= kitap_miktari <=10:



#   Ternery If
# age = int(input('Age: '))

# status = 'adult' if age >= 18 else 'child'
# print(status)

# number = int(input('Number: '))
# print(f"Status: {'positive' if number > 0 else 'negative'}")

#! Nested Ternary If 
# exam_score = 75
# result = 'AA' if exam_score >= 80 else 'BB' if exam_score >= 60 else 'CC'
# print(f'Result: {result}')

#try-except- finally

# try: 
#     bolunen = int(input('bolunen: '))
#     bolen = int(input('Bolen: '))
#     sonuc = bolunen / bolen
#     print(f'Sonuc: {sonuc}')
    
# except ZeroDivisionError as err:
#     print('bir tam sayı sıfıra bölünemez..!')
#     #! kendimize mail dönderiyoruz.
#     #* log ==> uygulamada ne oldu bitti bunların kayıtlarının tutulmasına "log"
#     print(f'{err}')
# finally 



#todo match case if else try exc finally calis . while loop calıs