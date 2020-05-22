import requests;
import json;
import pprint;
import random;
import html;

score_correct = 0;
score_incorrect = 0;

url = "https://opentdb.com/api.php?amount=10"
endGame = "";

while endGame != "quit":
    r = requests.get(url);

    if (r.status_code != 200):
        endGame = input("There was a problem retrieving the question " +
        "Press enter to try again or digit 'quit to exit'");
    else:
        valid_answer = False;
        answer_number = 1;
        data = json.loads(r.text);
        question = data['results'][0]['question'];
        answers = data['results'][0]['incorrect_answers'];
        correct_answer = data['results'][0]['correct_answer'];
        answers.append(correct_answer);
        random.shuffle(answers);

        print(html.unescape(question) + "\n");

        for answer in answers:
            print(str(answer_number)+ " " + html.unescape(answer));
            answer_number += 1;

        while valid_answer == False:
            user_answer = input("Type the number of the answer: ");
            try:
                user_answer = int(user_answer);
                if (user_answer > len(answers) or user_answer <= 0):
                    print("Invalid answer");
                else:
                    valid_answer = True;
            except:
                print("Invalid answer. Use only numbers");

            user_answer = answers[int(user_answer) -1];

        if (user_answer == correct_answer):
            print("You hit! The answer was: " + html.unescape(correct_answer));
            score_correct += 1;
        else:
            print("Sorry, the correct answer is " + html.unescape(correct_answer));
            score_incorrect += 1;

        print('\n---------------------------------------');
        print("Your score is:");
        print("Correct answers: " + str(score_correct));
        print("Incorrect answers: " + str(score_incorrect));
        print('---------------------------------------');

        endGame = input("\nDo you wanna quit the game, if yes digit 'quit'").lower();

print("\nThanks for playing!");
