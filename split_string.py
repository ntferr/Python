def take_numbers():
    string_numbers = input("Enter your numbers, separated by commas: ")
    numbers = string_numbers.split(",")
    return numbers


def sum_numbers():
    sum_numbers = 0
    numbers = take_numbers()

    for number in numbers:
        sum_numbers = sum_numbers + int(number)
    
    return sum_numbers

print(sum_numbers())
