

#! Map Func

print(
    list(
        map(lambda x: x ** 2, [i for i in range(10)])
    )
)

print(
    list(
        map(str, [i for i in range(10)])
    )
)

# mail_address = ['burak.yilmaz@outlook.com', 'hakan.yilmaz', 'ipek.yilmaz@outlook.com']

# print(
#     list(
#         map(lambda x: '@' in x, mail_address)
#     )
# )

products = [
    ['Boxing Gloves', 100, 59.99],
    ['Punching Bags', 150, 160.99],
    ['Hand Wrap', 200, 11.99],
]

# price yüzde 10 kdv uygulayalım
print(
    list(
        map(lambda x: x[2] * 1.10, products)
    )
)
# sadece ürün fiyatlarını ekrana bastıralım
print(
    list(
        map(lambda x: x[2], products)
    )
)


# baş harfleri büyüterek listeleyin
names = ['burak yilmaz', 'hakan yilmaz', 'ipek yilmaz']
print(
    list(
        map(str.title, names)
    )
)

domain_name = '@outlook.com'
print(
    list(
        map(lambda x: f"{x.replace(' ', '.')}{domain_name}" , names)
    )
)

# aşağıdaki iki listeyi toplayarak listeye ekleyin
# bir liste diğerinden kısa olabilir bunu göz önünde bulundurarak çözünüz
lst_1 = [87, 67, 81, 69, 65, 99, 79, 57, 62, 65]
lst_2 = [20, 39, 46, 100, 48, 34, 75, 59]

print(type(zip(lst_1, lst_2)))

# Path I
print(
    list(
        map(lambda x, y: x + y, lst_1, lst_2)
    )
)

# Path II
print(
    list(
        map(lambda x: x[0] + x[1], zip(lst_1, lst_2))
    )
)

# -100 ile + 100 arasında 10 tane rastegele sayı üretelim
# sadece pozitif sayıları string dönüştürerek bir liste içerisinde çıktı verin
from random import randint

numbers = (randint(a=-100, b=100) for _ in range(10))

positive_str = list(
    map(
        str,
        filter(lambda x: x > 0, numbers)
    )
)

print(positive_str)

# list comprehension ile 2 tane rastgele sayılar içeren liste oluşturun
# üretilecek sayı aralıkları -100, +100
# her iki listedeki sayıları toplayalım
# toplamları negatif olanları pozitif dönüştürerek bir liste içerisinde yazıdralım

a = [randint(a=-100, b=100) for _ in range(10)]
b = [randint(a=-100, b=100) for _ in range(10)]

result = [abs(x + y) for x, y in zip(a, b)]

lst_result = list(map(str, result))

print(lst_result)
# output: ['132', '51', '66', '21', '54', '150', '66', '79', '6', '105']

# hint: str.join()
# beklenen çıktı:
# 132-51-66-21....
str_result = '-'.join(lst_result)

print(str_result)

