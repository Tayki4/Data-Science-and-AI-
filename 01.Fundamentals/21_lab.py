
from random import randint, choice

easy_bots = ['elton', 'adal', 'özlem', 'furkan', 'mirza']

hard_bots = ['burak', 'hakan', 'ipek']

users = {
    '1': {
        'user name': 'beast',
        'password': '123',
        'safe':2000
    },
    '2': {
        'user name': 'savage',
        'password': '987',
        'safe':2000
    },
    '3': {
        'user name': 'bear',
        'password': '657',
        'safe':3000
    },
}

minimum_bet = 100

def gain_daily_chips(x: int = 1000, y: int = 2000) -> int:
    return randint(a=x, b=y)

def select_bot_player(bots_type: list = easy_bots) -> str:
    return choice(bots_type)

def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False

def roll_dice() -> int:
    return randint(a=2, b=12)

def update_safe(user: dict, chip_amount: int, status: str = 'win') -> str:
    if status == 'win':
        user.update({
            'safe': user.get('safe') + chip_amount
        })

        return (
            f'Well done..!\nYour current safe is {user.get("safe")}'
        )
    else:
        user.update({
            'safe': user.get('safe') - chip_amount
        })

        return (
            f'You losed..!\nYour current safe is {user.get("safe")}'
        )

def main():
    sign_user = users.get('1')

    gained_chip = gain_daily_chips()

    msg = update_safe(user=sign_user, chip_amount=gain_daily_chips)

    print(
        f'Welcome, {sign_user.get("user name")}\n'
        f'You earned daily free chips --> {gained_chip}\n'
        f'{msg}'
    )

    while True:
        if sign_user.get('safe') >= minimum_bet:
            print(f'Your oppent came, {select_bot_player()}')

            bet = int(input('Please make a bet: '))

            if is_bet_valid(current_bet=bet, safe=sign_user.get('safe')):
                user_roll = roll_dice()
                bot_roll = roll_dice()

                if user_roll > bot_roll:
                    print(f'{update_safe(user=sign_user, chip_amount=bet)}')
                elif bot_roll > user_roll:
                    print(f'{update_safe(user=sign_user, chip_amount=bet, status="lose")}')
                else:
                    print('Player are tie..!')
            else:
                print(f'Your bet is not valid..!')
        else:
            print(
                f'Your safe {sign_user.get("safe")} is under the minimum table bet..\n'
            )
            break

main()