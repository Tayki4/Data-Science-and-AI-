#list_1 ve lst_2 icerisine rastgele 10 tane sayı uret doldur
#doldurma is nidex mant gore yap
#orn lst_1[0] + lst_2[0] toplanarak lst_3 ilgili indexsine yazılacak
# from random import randint

# lst_1 = []
# lst_2 = []
# lst_3 = []

# for i in range(10):
    # lst_1.insert(i, randint(0, 100))
    # lst_2.insert(i, randint(0, 100))

    # lst_3.insert(i, lst_1[i] + lst_2[i])

# print(lst_1)
# print(lst_2)
# print(lst_3)

# lst = [
#     ['Sarıyer'],
#     ['Etiler', 'Nispetiye', 'Ulus'],
#     ['Suadiye', ['Feneryolu' , 'Erenköy']],
#     [['Beşiktaş' , 'Maçka'], 'Harbiye', ['Naşantaşı']]
# ]

# print(lst[0][0])
# print(lst[3][1])

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

#!unpacking - unboxing
# my_family = [
#     ['Burak Yılmaz', 36, 'Developer'],
#     ['Hakan Yılmaz', 39, 'Chemist'],
#     ['İpek Yılmaz', 41, 'Art Historian']
# ]

# for Full_name, age, occupation in my_family:
#     print(
#         f'Fullname:{Full_name} \n'
#         f'Age: {age} \n'
#         f'Occupation: {occupation}'
#     )

#kullanıcı login olacak
#register olabilsin
# butn urunler topl fiyat nedri
# urun adı laptop olan urunlerın fiyatlarını top
#kullanıcı urun search 
# fiyatini 200 tl altında olan urunler listele


user = [
    ['beast', '123'],
    ['bear', '987'],
    ['keko', '567'],
]

products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60]
]

username = user[0][0] or user[1][0] or user[2][0]
password = user[0][1] or user[1][1] or user[2][1]
