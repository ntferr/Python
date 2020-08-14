import random


def menu():
    player_numbers = getPlayerNumbers()
    lottery_numbers = createLotteryNumbers()
    matched_numbers = player_numbers & lottery_numbers

    print(f"You matched {matched_numbers}\nYou won ${100 ** len(matched_numbers)}")


def getPlayerNumbers():
    number_csv = input("Enter 6 numbers, separeted by commas: ")
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    
    return integer_set


def createLotteryNumbers():
    values = set()
    
    while len(values) < 6:
        values.add(random.randint(1, 20))
    
    return values


menu()
