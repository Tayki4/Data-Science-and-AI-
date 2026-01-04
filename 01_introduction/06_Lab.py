

#! Filter Function

# rastegele sayılar ile bir listeyi dolduralım. 
# 1000 adet sayı yeterli
# a=-100, b=100
# list comprehensions yapıyoruz
from random import randint

numbers = [randint(a=-100, b=100) for i in range(1000)]

#! Soru: Yukarıda oluşturulan liste içerisinden pozitif olanları listleyelim

# todo: Path I --> List Comprehension
# positive_numbers = [number for number in numbers if number > 0]

# todo: Path II --> Filter()
# temp_lst = filter(lambda x: x > 0, numbers)
# positive_numbers = list(temp_lst)
# print(positive_numbers)

# todo: Filter Fonksiyonu ile çift sayıları filtreleyelim liste olarak ekrana yazdıralım
# print(
#     list(
#         filter(lambda x: x % 2 == 0, numbers)
#     )
# )

# fruits = [
#     "Apple", "Banana", "Orange", "Mango", "Pineapple",
#     "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
#     "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
#     "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
# ]

# print(
#     list(
#         filter(lambda fruit: '@' in fruit, fruits)
#     )
# )

lst = [None, 2, 'b', 3.19, True, 9, 'mike tyson']

numbers = list(
    filter(lambda x: isinstance(x, (int, float)), lst)
)

print(numbers)

mails = ['burak.yilmaz@outlok.com', 'savage@mail.com', 'bear@', 'beast@com.xyz', 'burak@gmail.com']

correct_mail = list(
    filter(lambda x: x.endswith('.com') ,mails)
)

print(correct_mail)

some_values = ['123', 'burak', 'zxc', '987', '345']

only_digit = list(
    filter(str.isalpha, some_values)
)

print(only_digit)

# 100.000.000 tane rastgele sayı üretilecek. list comprhenbsion ile yapılacak
# Path I, II, III time ve memory cost hesaplayarak ekrana rapor olarak yazdırın
# Path I --> List Comprehensions ile poszitif sayılar bulunacak ve liste olarak ekrana basılacak.
# Path II --> Filter fonksiyonu ile poszitif sayılar bulunacak ve liste olarak ekrana basılacak.
# Path III --> For loop yapıalcak
# from random import randint
# import time
# import tracemalloc


# tracemalloc.start()
# t1 = time.perf_counter()

# # Sayı yaratırken aşağıdaki list comprehension kullanmak yerine generator pattern kullansaydınız işin rengi baya değişirdi. 
# # Sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti azalırdı.
# # numbers = [randint(a=-100, b=100) for _ in range(1000000)]
# numbers = (randint(a=-100, b=100) for _ in range(1000000))

# # List Comprehension
# positive_number = [number for number in numbers if number > 0]

# # Filter Func
# # positive_number = list(filter(lambda number: number > 0, numbers))

# # With For Loop
# # positive_number = []
# # for number in numbers:
# #     if number > 0:
# #         positive_number.append(number)

# print(positive_number)

# t2 = time.perf_counter()
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# runtime_ms = (t2 - t1) * 1000
# peak_memory = peak / 1024 / 1024

# print(
#     '===============================\n'
#     'Method --> List Comprehension\n'
#     f'Runtime: {runtime_ms}\n'
#     f'Peak Memory: {peak_memory}'
    
# )

"""
===============================
Method --> List Comprehension
Runtime: 5728.366099996492
Peak Memory: 28.39721393585205
===============================
Method --> Filter Func
Runtime: 3872.5149999954738
Peak Memory: 28.40944004058838
===============================
Method --> With For Loop
Runtime: 4765.219499997329
Peak Memory: 28.41720485687256
"""
