
products = [
    {'name': 'Lenovo X1 Carbon', 'price': 110_000, 'stock': 12},
    {'name': 'Lenovo Thinkpad', 'price': 89_000, 'stock': 7},
    {'name': 'Macbook Pro', 'price': 250_000, 'stock': 3},
    {'name': 'Macbook Air', 'price': 125_000, 'stock': 5},
    {'name': 'Asus Zenbook', 'price': 150_000, 'stock': 4},
    {'name': 'Monster Huma', 'price': 55_000, 'stock': 18},
    {'name': 'Monster Alba', 'price': None, 'stock': 0},
    {'name': None, 'price': 100_000_000, 'stock': 0},
]

#todo: kullanıcıdan aradığı ürünün adını, fiyat aralığı ve stock bilgilerini alıp ilgili ürünleri dönen foksiyon yazın
def get_data(data: list, product_name: str, stock: bool, start_price: int, end_price: int) -> list | str:
    temp_list = []
    
    for item in data:
        if item.get('stock') > 0:
            if product_name.lower() in item.get('name').lower() and start_price <= item.get('price') <= end_price:
                temp_list.append(item)
    
    if len(temp_list) > 0:
        return temp_list
    else:
        return 'aradığınız ürün bulunmamaktadır..!'

result = get_data(
    data=products,
    product_name='Lenovo',
    stock=True,
    start_price=80_000,
    end_price=120_000
)

print(result)
