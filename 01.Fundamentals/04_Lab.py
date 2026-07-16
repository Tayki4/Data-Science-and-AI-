
# For Loop
# "in" operatörü - "range()" fonksiyonu

# in operatörü
# print('b' in 'burak')
# print('z' in 'burak')

# # not in operatörü
# print('b' not in 'burak')
# print('z' not in 'burak')

# range()
# for i in range(10):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(10, 20, 2):
#     print(i)

#! Kullanıcıdan başlangıç, bitiş ve artış mikarlarını alalım.
#? kullanıcın belirlediği bu şarlatra göre oluşan sayıları ekrana yazdıralım
# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))
# adim = int(input('Adım: '))
#         # 0-1-2-3-4-5-6-7-8-9-
# for i in range(baslangic, bitis, adim):
#     print(i, end='-')

# 0-100 arasındaki sayıları ekrana yazdıralım
# for i in range(101):
#     print(i, end='-')

# 0-100 arasındaki çift ve tek sayıların toplamını ekrana yazdırın
# ciftlerin_toplami = 0
# teklerin_toplami = 0
# for i in range(101):
#     if i % 2 == 0:
#         ciftlerin_toplami += i # ciftlerin_toplami = ciftlerin_toplami + 1
#     else:
#         teklerin_toplami += i

# print(f'Çiftlerin Toplami: {ciftlerin_toplami}     ||     Teklerin Toplami: {teklerin_toplami}')

from random import randint

#! 10 tane rastgele sayı üretip ekrana yazdırın
# for i in range(1, 11):
#     random_number = randint(a=0, b=100)
#     print(f'{i}. üretilen sayı --> {random_number}')

#! kullanıcı rastgele üretilen sayıyı tahmin etsin. 3 kez deneme şansı olsun.
generated_number = randint(a=0, b=100)
print(generated_number)
hak = 2
while hak >= 0:
    x = int(input('Tahmin Gir: '))
    if generated_number == x:
        print('Tebrikler kazandınız..!')
        break
    else:
        print(f'Bilemediniz..!\nKalan hakkınız: {hak}')
    hak -= 1

# list konusu çalışacak
# listeler index mantığı nedir?
# python'da listler ait build-in fonksiyonlar araştırlısın. örnğin: sort(), extend(), pop(), insert(), append(), remove() etc etc.
# for loop ile liste örnekleri incenlesin, bol bol örnek çözün
# belki list comprehension
