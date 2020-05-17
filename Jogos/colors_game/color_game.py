import random;

colors = ["red", "yellow", "black", "white", "grey"];
index = random.randint(0, 4);

correct = False;

answer = input("Which one of follow colors: Red, Yellow, Black, White, Grey ->").lower();

while (correct != True):
    if (answer == colors[index]):
        print("You hit!");
        correct = True;
    else:
        key = input("Do you wanna continue playing? ").lower();
        if (key == 'n'):
            print("Thanks for playing!");
            break;
        else:
            print("Try again");
            answer = input("Which one of follow colors: Red, Yellow, Black, White, Grey ->").lower();
