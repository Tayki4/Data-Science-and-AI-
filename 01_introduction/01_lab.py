

#! Variable (değişken)
#? değişken tanımlarken dikkat edilecek hususlar 
#* 1. Değişken isimleri rakam ile başlamaz.
#* 2. Bosluk karakteri içermez, boşluk yerine "_" sembolü kullanılır.
#* 3. Türkçe karakter kullanmayalim.
#todo: Not--> Yukarıdaki satırlar yorum satırıdır(comment Line). Inerpeter tarafından yorumlanmazlar yani çaşıştırılmazlar.
#! Not: IDE'ler kodları yukarıdan aşğıya doğru satr satır calıstırırlar.


user_name = 'beast' 
print (user_name)
#1 Not: Python'da degiskenler icerisine attıgımız degerin tipine sahip olurlar.
#todo: yukarıda ki user_name degiskeninin tipi string'tir.

x = 10 # x degiskeni integer
y = 3.14 # y tiği float'tır
is_active = True # true ya da false değer alan degiskenler boolean ya da bool olarak isimlendirilir.

#! aritmatiksel islemler
# number_1 = int(input('type a number: ')) # python 2 string ifadeyi + ile birlestirir yani yan yana yazar ve input cıktısı string 
# number_2 = int(input('type a number : '))
# result = number_1 - number_2

# print(result)

#! kullanıcıdan alınan kenar bilgisi ile kare alan ve cev hesapla.

# edge = float(input('edge: '))
# area = edge * edge 
# premiter = 4 * edge 

# print('area: ', area)
# print(f'premiter: {premiter} ')
# print(f' Area: {area} - Premiter: {premiter}')

#! kull alinan ksa kenar ve uzun ken bilg göre bir dikdörtgen alanini ve cev hesaplayan cıktıları yaz.

# edge_1 = float(input('edge1: '))
# edge_2 = float(input('edge2: '))
# area = edge_1 * edge_2
# premiter = edge_1 * 2 + edge_2 * 2
# print (f'Area: {area}  -  Premiter: {premiter}')

#! ucgenin alani hesap.

edge_1 = float(input('edge1: '))
high = float(input('high: '))
area = edge_1 * high // 2
print (f'Area: {area}')
