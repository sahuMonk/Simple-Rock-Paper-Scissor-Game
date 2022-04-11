import random

n = int(input("enter total number of round: "))
user_score = 0
computer_score = 0

while n > 0:
    print("Enter:-\n1. ROCK\n2. PAPER\n3. SCISSOR")
    user_choice = int(input("your's turn "))

    if user_choice == 1:
        print("ROCK")
    elif user_choice == 2:
        print("PAPER")
    elif user_choice == 3:
        print("SCISSOR")

    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        print("ROCK")
    elif computer_choice == 2:
        print("PAPER")
    elif computer_choice == 3:
        print("SCISSOR")

    if user_choice == 3 and computer_choice == 2:
        print("you won this round")
        user_score = user_score + 1
    elif user_choice == 2 and computer_choice == 1:
        print("you won this round")
        user_score = user_score + 1
    elif user_choice == 1 and computer_choice == 3:
        print("you won this round")
        user_score = user_score + 1
    elif user_choice == computer_choice:
        print("its draw")
    else:
        print("computer won this round")
        computer_score = computer_score + 1
    n = n - 1

print()
if user_score > computer_score:
    print("you won the tournament: " + str(user_score) + "-" + str(computer_score))
elif user_score < computer_score:
    print("computer won the tournament: " + str(computer_score) + "-" + str(user_score))
else:
    print("its draw")
