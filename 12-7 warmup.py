import random

questions = ["What is your name? ","What is your favorite Christmas song? ","Who is the best CompSci Club Leader? "]

number = random.randint(0,2)

answer = input(questions[number])

# You didn't have to do this, but here is the appeal of such a program!

if number == 0:
    print("Hello there", answer, "!")
elif number == 1:
    print('No way! I love "', answer, '"as well!')
else:
    if answer == "Fillip":
        print("Fillip is great, he is just too tall (Zoom doesn't show that)")
    elif answer == "Krish":
        print("Krish has been a great person to know this year at RCHS!")
    elif answer == "Arnav":
        print("Awww :) This is the right answer, good job!")
    else:
        print("Lol, who?")
