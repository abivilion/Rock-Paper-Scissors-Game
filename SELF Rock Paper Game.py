import sys, random

win = 0
lose = 0
tie = 0
while True:

    # Logic runs and to be compared from here
    tied = "Game Tie!"
    lost = "Oops! You lose!"
    won = "You won!"
    user = input("Enter you move -> (r)ock,(p)aper,(s)cissor or (q)uit: ").lower()
    if user == "r" or user == "rock":
        user = "ROCK"
        print("You choose :" + user)

    # working()
    elif user == "p" or user == "paper":
        user = "PAPER"
        print("You choose :" + user)

        # working()
    elif user == "s" or user == "scissor":
        user = "SCISSOR"
        print("You choose :" + user)

    # working()
    elif user == "q" or user == "quit":
        print("You Choose: Quit \n The Game is Turning Off... Done! Bye,See ya")
        sys.exit()
    else:
        print("Invalid Input!! Try Again")

    # System Choice Code From here
    system_c = random.randint(0, 2)

    if system_c == 0:
        syste = "Rock"
        print("I choose Rock ")

    elif system_c == 1:
        syste = "Paper"
        print("I choose Paper")

    elif system_c == 2:
        syste = "Scissor"
        print("I choose Scissor")

    # Now, Comparing user choice and system choice with each other AND calculating WINS,LOSES and TIE.

    user = user.lower()
    system_c = syste.lower()

    if user == system_c:
        tie = tie + 1
        print(tied)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "rock" and system_c == "scissor":
        win = win + 1
        print(won)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "rock" and system_c == "paper":
        lose = lose + 1
        print(lost)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "paper" and system_c == "rock":
        win = win + 1
        print(won)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "paper" and system_c == "scissor":
        lose = lose + 1
        print(lost)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "scissor" and system_c == "paper":
        win = win + 1
        print(won)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "scissor" and system_c == "rock":
        lose = lose + 1
        print(lost)
        print("\n", win, " win", lose, " lose", tie, " tie")
    elif user == "rock" and system_c == "scissor":
        win = win + 1
        print(won)
        print("\n", win, " win", lose, " lose", tie, " tie")
