
burak_account = {
    'account no': '12345',
    'password': '123',
    'balance': 2000,
    'additional balance': 1000
}

hakan_account = {
    'account no': '98765',
    'password': '546',
    'balance': 3000,
    'additional balance': 1000
}

ipek_account = {
    'account no': '34567',
    'password': '987',
    'balance': 4000,
    'additional balance': 1000
}

users = [burak_account, hakan_account, ipek_account]

def get_valid_answer(question: str, valid_options: tuple) -> str:
    question += f' ({", ".join(valid_options)}): '
    
    response = input(question)
    
    while response.lower() not in valid_options:
        print('Please type the valid options..!')
        response = input(question)
    
    return response

def account_information(account: dict):
    print(
        f'Account No: {account["account no"]}\n'
        f'Balance: {account["balance"]}\n'
        f'Additional Balance: {account["additional balance"]}'
    )

def withdraw_money(account: dict, amount: int):
    if account['balance'] >= amount:
        account['balance'] -= amount
        account_information(account=account)
    else:
        total_balance = account['balance'] + account['additional balance']
        
        if total_balance >= amount:
            used_additional_balance = get_valid_answer(question='Insufficen balance..!\nDo you want to use additional balance?', valid_options=("y", "n"))
            
            match used_additional_balance:
                case 'y':
                    detech_amount = amount - account['balance']
                    account['balance'] = 0
                    account['additional balance'] -= detech_amount
                    account_information(account=account)
                case 'n':
                    print('Transaction has been cancaled..!')
                    account_information(account=account)
        else:
            print(
                'Insufficent balance..!\n'
                'Transaction has been cancaled..!'
            )
            account_information(account=account)

def deposit_money(account: dict, amount: int, transaction_name: str = 'owner'):
    short = 1000 - account['additional balance']
    if amount >= short:
        kalan = amount - short
        account['additional balance'] += short
        account['balance'] += kalan
    else:
        account['additional balance'] += amount
    
    if transaction_name == 'owner':
        account_information(account=account)

def eft(account: dict, receiver_no: str, amount: int) -> None:
    withdraw_money(account=account, amount=amount)

    # Path - I
    # finded_user = [user for user in users if user.get('account no') == receiver_no]

    # deposit_money(account=finded_user[0], amount=amount, transaction_name='eft')

    # Path - II
    for user in users:
        if user.get('account no') == receiver_no:
            deposit_money(account=user, amount=amount, transaction_name='eft')
    

def login(account_no: str, password: str) -> dict | None:
    for user in users:
        if user.get('account no') == account_no and user.get('password') == password:
            return user
    
    return None

def main():
    counter = 3
    while counter > 0:
        login_account = login(
            account_no=input('Account No: '),
            password=input('Password: ')
        )

        if login_account is not None:
            print(f'Welcome, {login_account["account no"]}')

            while True:
                transaction_no = input('Transaction No: ')

                if transaction_no == '1':
                    withdraw_money(
                        account=login_account,
                        amount=int(input('Amount: '))
                    )
                elif transaction_no == '2':
                    deposit_money(
                        account=login_account,
                        amount=int(input('Amount: '))
                    )
                elif transaction_no == '3':
                    eft(
                        account=login_account,
                        receiver_no=input('Receiver No: '),
                        amount=int(input('Amount: '))
                    )
                elif transaction_no == 4:
                    account_information(account=login_account)
                else:
                    print('Please enter the valid transaction number..!')
        else:
            print('Invalid Credentials..!')
            counter -= 1
main()