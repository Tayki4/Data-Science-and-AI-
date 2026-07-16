

#! Variable (Değişken)
#? Değişken tanımlarken dikkat edilecek hususlar
#* 1.Değişken isimleri rakam ile başlamaz
#* 2.Boşluk karakteri içermez, boşluk yerine "_" sembolü kullanılır
#* 3.Türkçe karaketer kullanmayalım.
#todo: Not --> Yukarıdaki satırlar yorum satırıdır (Comment Line). Interpeter tarafından yorumlanmazlar yani çalıştırılmazlar.
#! NOt: IDE'ler kodları yukarıdan aşağıya doğru satır satır çalıştırırlar.


user_name = 'beast'
print(user_name)
print(type(user_name))
#! Not: Python'da değişkenler içerisine attığımız değerin tipine sahip olurlar.
#todo: Yukarıda ki user_name değişkenin tipi string'tir. 
user_name = 100
print(user_name)
print(type(user_name))

x = 10 #* x değişkenin tipi integer'dır
y = 3.14 #? y değişkeninin tipi float'tır
is_active = True #* True yada False değer alan değişkenler boolean yada bool olarak isimlendirilir.

#! ARİTMATİKSEL İŞLEMLER
# number_1 = int(input('Type a number: '))
# number_2 = int(input('Type a number: '))

# result = number_1 + number_2

# print(result)

# num_1 = int(input('Type a number: '))
# num_2 = int(input('Type a number: '))

# result = num_1 - num_2

# print(result)

#! Kullanıcıdan alınan kenar bilgisine göre karenin alanını ve çevresini hesaplayan ve sonuçları çıktı veren uygulamayı geliştirelim.
# edge = float(input('Edge: '))

# area = edge * edge
# premiter = 4 * edge

# print(f'Area: {area} - Premiter: {premiter}')

#! Kullanıcıdan allınan kısa kenar ve uzun kenar bilgisine göre bir dikdörtgenin alanını ve çevresini hesaplayan ve sonuçları çıktı veren uygulamayı yazınız.
# kisa_kenar = int(input('Kısa Kenar: '))
# uzun_kenar = int(input('Uzun Kenar: '))

# print(f'Alan: {kisa_kenar * uzun_kenar} - Cevre: {2 * (kisa_kenar + uzun_kenar)}')

#! üçgen alanını hesaplayın. 
taban: int | float = float(input('Taban: '))
yukseklik: int | float = float(input('Yükseklik: '))

sonuc = taban * yukseklik / 2

print(f"Üçgenin'in Alannı: {sonuc}")
