
#! *args vs **kwargs

#todo: *args
def total(*args):
    return sum(args)

print(total(1, 2, 3))

print(total(9, 8, 12, 45, 23))

print(total())

def concat_str(*args, seperator: str=" "):
    return seperator.join(args)

print(concat_str("burak", 'yılmaz', '36'))
print(concat_str("bugün", 'sınıf', 'mevcudu', 'çok', 'az'))

from datetime import datetime

def sys_log(*args):
    for msg in args:
        print(f'System log: {msg}\nLog Date: {datetime.now()}')

sys_log('Status Code --> 200', 'DB Connection has been lost', 'Passive')

#todo: **kwargs
def get_info(**kwargs):
    return (
        f'Full Name: {kwargs.get("full_name")}\n'
        f'Occupation: {kwargs.get("occupation")}\n'
        f'Alias: {kwargs.get("alias")}'
    )

print(get_info(full_name='Burak Yılmaz'))
print(get_info(full_name='Hakan Yılmaz', occupation='Chemist'))
print(get_info(full_name='İpek Yılmaz', occupation='Art Historian', alias='keko'))

from socket import gethostname, gethostbyname

def log(*args, **kwargs):
    return (
        f'Message: {kwargs.get("msg")}\n'
        f'IP Address: {kwargs.get("ip_address")}\n'
        f'Machine Name: {kwargs.get("machine_name")}\n'
        f'Exception Date: {kwargs.get("exception_date")}\n'
    )


print(
    log(
        msg='Internal Gateway', 
        ip_address=gethostbyname(gethostname()), 
        machine_name=gethostname(), 
        exception_date=datetime.now()
    )
)

