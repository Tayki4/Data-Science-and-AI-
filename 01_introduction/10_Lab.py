
# Set Func

# numbers = [1, 1, 2, 2, 9, 9, 6]

# print(
#     set(numbers)
# )

# full_name = 'buraburak'

# unique_ch = list(set(full_name))

# unique_ch.sort()

# print(unique_ch)

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}

# print(x & y)

# print(x | y)

# boxers = {'muhammed ali', 'mike tyson'}
# boxers.add('lenox lewis')
# boxers.add('evander holyfield')
# boxers.add('antony jasua')
# print(boxers)

# boxers.remove('lenox lewis')
# boxers.discard('evander holyfield')

# All Func
ages = [18, 34, 13, 67, 23]

member = all(age > 18 for age in ages)

print(member)

products = [
    ['name', 'boxing gloves', 'price', 59.99, 'stock', 5],
    ['name', 'punching bags', 'price', 159.99, 'stock', 15],
    ['name', 'handwrap', 'price', 19.99, 'stock', 0]
]

print(
    all(
        product[5] > 0 for product in products
    )
)

password = 'Bu?ra4k_'

is_password_valid = [
    any(ch.isupper() for ch in password),
    any(ch.islower() for ch in password),
    any(ch.isdigit() for ch in password),
    any(not ch.isalnum() for ch in password),
]

print(is_password_valid)

print(
    all(is_password_valid)
)
