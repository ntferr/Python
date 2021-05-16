import random

def lottery_app():
    user_numbers = get_user_numbers()
    lottery_numbers = get_lottery_numbers()
    sorted_numbers = lottery_numbers.intersection(user_numbers)
    print(f'You hit the numbers {sorted_numbers} you won {100 * len(sorted_numbers)}')


def get_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values


def get_user_numbers():
    user_numbers = input('Digit 6 numbers separated by commas: ')
    splited_numbers = user_numbers.split(',')
    set_numbers = {int(number) for number in splited_numbers}
    return set_numbers


if __name__ == '__main__':
    lottery_app()
