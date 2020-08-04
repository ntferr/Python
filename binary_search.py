def binarySearch(target):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    min = 0
    max = len(numbers)
    guess = 0 

    count = 0

    while True:
        guess = floor((min + max) / 2)
        print(f'PC: {guess}')


        if guess == target:
            count = count + 1
            print(f'Contador: {count}')
            return guess
        
        if guess > target:
            count = count + 1
            max = guess - 1
        else:
            count = count + 1
            min = guess + 1
    
    return -1

print(binarySearch(2))"""
