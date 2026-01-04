
# Dictionary (Sözlükler)

relase_year_movie = {
    'Fight Club': 1999,
    'Matrix': 1999,
    'Interstaller': 2014,
    'Inception':2010,
    'Dune': 2021
}

# region Read
# 'Fight Club' anahtarında tutulan value ekrana yazdırın
# Path - I
print(
    relase_year_movie['Fight Club']
)
# Path - II
print(
    relase_year_movie.get('Fight Club')
)

# Get All Values
for value in relase_year_movie.values():
    print(value)

# Get All Keys
for key in relase_year_movie.keys():
    print(key)

# Get All Items
for key, value in relase_year_movie.items():
    print(
        f'Movie Name: {key}\n'
        f'Release Year: {value}'
    )
# endregion

# region Create Item
relase_year_movie['Dune II'] = 2023
print(relase_year_movie)
# endregion

# region Update Item
relase_year_movie.update({
    'Dune II': 2024
})
print(relase_year_movie)
# endregion

# region Delete
del relase_year_movie['Dune II']
print(relase_year_movie)
# endregion

products = [
    {'name': 'Lenovo X1 Carbon', 'price': 110.000},
    {'name': 'Lenovo Thinkpad', 'price': 89.000},
    {'name': 'Macbook Pro', 'price': 250.000},
    {'name': 'Macbook Air', 'price': 125.000},
    {'name': 'Asus Zenbook', 'price': 150.000},
    {'name': 'Monster Huma', 'price': 55.000},
    {'name': 'Monster Alba'},
    {'price': 100_000_000},
]

# region Q1
#todo: products listesinde ki tüm ürünlerin fiyatlarını toplayalım
# total_price = 0
# for product in products:
#     total_price += product.get('price') # total_price = total_price + product.get('price')

# print(f'Total Price: {total_price}')

# Path II
# total_price = sum(product.get('price', 0) for product in products)
# print(f'Total Price: {total_price}')
# endregion

# region Q2
#todo: ürünlerin fiyat aralığı 100.000 büyük olan ürünleri listeleyelim
# price_thershold = 100.000

# filtered_products = [product for product in products if product.get('price', 0) > price_thershold]

# for product in filtered_products:
#     print(
#         f'Product Name: {product["name"]}\n'
#         f'Price: {product["price"]}'
#     )
# endregion

# region Q3
#todo: ürün adı içerisinde Lenovo geçen ve fiyat aralığı 100 bin ile 150 bin aralığında olan ürünleri listeleyin
name_kwd = 'Lenovo'
min_price = 100.000
max_price = 150.000

filtered_products = [
    product for product in products 
    if name_kwd in product.get('name', '') and 
    min_price < product.get('price') < max_price
]

for product in filtered_products:
    print(
        f'Product Name: {product["name"]}\n'
        f'Price: {product["price"]}'
    )
# endregion

# 1. yeni kayıt eklenecek (Create New Record)
# 1.1. id bilgisi 'd912b8cf-0b59-4efb-bfcf-17356dd59c9b' uuid modülünden faydalanarak yaratılacak
# 2. var olan bir kayıt güncellenecek (Update) --> kullanıcıdan id bilgisi alınacak ve ilgili kayıt güncelenecek
# 3. var olan bir kayıt silinecek (Delete) --> kullanıcıdan id bilgisi alınacak ve ilgili kayıt güncelenecek
# 4. Read operasyonları --> bütün kayıtlar listelenecek, kullanııdan ürün adı alınacak ve ilgli ürün listelenecek,

from uuid import uuid4
from pprint import pprint

categories = {
    'd912b8cf-0b59-4efb-bfcf-17356dd59c9b': {
        'name': 'Boxing Gloves',
        'description': 'Best boxing gloves'
    },
    '9ecfa748-ee8e-4ac3-a471-33e1fd9fe52c': {
        'name': 'MMA Gloves',
        'description': 'Best MMA gloves'
    }
}

while True:
    process = input('Type a process name: ')
    
    match process:
        case 'create':
            new_name = input('Please type a category name: ')
            new_descp = input('Please type a description: ')
            
            categories[str(uuid4())] = {
                'name': new_name,
                'description': new_descp 
            }
            
            pprint(categories)
        case 'get all':
            pprint(categories)
        case 'get by id':
            category_key = input('Category Key: ')
            result = categories.get(category_key)
            if result is None:
                print('There is no such a category..!')
            else:
                print(result)
        case 'get by name':
            cat_name = input('Category name: ')
            filtered_categories = [category for category in categories.values() if cat_name in category.get('name')]
            pprint(filtered_categories)
        case 'update':
            category_key = input('Category Key: ')
            
            is_exist = any(key == category_key for key in categories.keys())
            
            if is_exist:
                new_name = input('Please type a category name: ')
                new_descp = input('Please type a description: ')
                
                categories.update({
                    category_key: {
                        'name': new_name,
                        'description': new_descp
                    }
                })
                
                print(
                    f'{category_key} has been edited..!'
                    f'{categories[category_key]}'
                )
            else:
                print('There is no such a category..!')
        case 'delete':
            category_key = input('Category Key: ')
            
            is_exist = any(key == category_key for key in categories.keys())
            
            if is_exist:
                del categories[category_key]
                print(
                    f'{category_key} has been removed..!\n'
                    f'{categories}'
                )
            else:
                print('There is no such a category..!')
        case _:
            print('Invalid process type..!')


