
#! Zip Func

# names = ['burak', 'hakan', 'ipek']
# age = [36, 39, 41]

# result = list(
#     zip(names, age)
# )

# print(result)

# names = ['burak', 'hakan', 'ipek']
# age = [36, 39, 41]
# occupation = ['developer', 'chemist - chemical engineer']

# result = list(
#     zip(names, age, occupation)
# )

# print(result)

# rastgele 10 tane sayı ile number_1 ve number_2 doldurulacak
# aynı index depolanan değerler toplanarak sonuçları liste olarak verilecek
# from random import randint

# number_1 = [randint(a=0, b=100) for _ in range(100)]
# number_2 = [randint(a=0, b=100) for _ in range(10)]

# temp_lst = list(
#     zip(number_1, number_2)
# )

# result = [x + y for x, y in temp_lst]

# print(result)

#! Unzip
lst = [('burak', 36, 'developer'), ('hakan', 39, 'chemist - chemical engineer')]

names, ages, occupations = zip(*lst)

print(names)
print(ages)
print(occupations)

# lst = ['ayhan', 'elton', 'adal', 'merve']

# print(
#     list(zip(range(len(lst)), lst))
# )

# character_1 = 'xyz'
# character_2 = 'XYZ'

# print(
#     list(
#         zip(character_1, character_2)
#     )
# )

# matrix = [
#     [34, 56, 123, 56], # --> bu iç listeler list comprehnsion ile rastgele sayılar ile doldurulacak
#     [23, 67, 12, 45],
#     [11, 54, 89, 22], # --> 3 line yeterli
# ]

# Output:
# [(34, 23, 11), (56, 67, 54), (123, 12, 89), ....]

from random import randint


matrix = [[randint(a=0, b=100) for _ in range(10)] for i in range(3)]

print(matrix)

print(list(zip(*matrix)))
