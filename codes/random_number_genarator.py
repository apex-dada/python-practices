import random
from operator import truediv

# number=random.randint(1,20)  #randint(start,ends) gives random integer from a range of integers
# print(number)

# low=1
# high=100
# number2=random.randint(low,high)
# number3=random.random() #random.random() creates a random flooting number
# print(number3)
# number4=random.uniform(low,high) #random.uniform(start,ends) creates a random flooting number from a range
# print(number4)
# options=("rock","paper","scissors")
# option=random.choice(options) #random.choice prints a random value from a given collection
# print(option)
# cards=["2","3","4","5","6","7","8","9","10","J","Q","A"] # random.shuffle() shuffles the collection
# random.shuffle(cards)
# print(cards)

# exercise 1: number guessing game

lowest_num =1
highest_num=100
answers=random.randint(lowest_num,highest_num)
#print(answers)
is_running=True
guesses=0
print("welcome")
while is_running:

    guess=input("enter your guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess>100 or guess<0:
            print("guess a number between 1 to 100")
        elif guess>answers:
            print("too high! Try again")
        elif guess<answers:
            print("too low! try again")
        else:
            print("correct")
            is_running=False

    else:
        print("invalid guess")
        print(f"please select number between {lowest_num} to {highest_num}")


# --------------------practice 2-------------------
# rock paper scissors game

import random

options = ("rock", "paper", "scissors")

print("---------------------welcome---------------------")

playing = True
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter your move(rock,paper,scissors) :")

    if computer == player:
        print("it is tie")
        print(f"computer picked {computer} you picked {player}")
    elif player == "rock" and computer == "scissors":
        print("you win!!!!!!")
        print(f"computer picked {computer} you picked {player}")
    elif player == "paper" and computer == "rock":
        print("you win!!!!!!")
        print(f"computer picked {computer} you picked {player}")

    elif player == "scissors" and computer == "paper":
        print("you win!!!!!!")
        print(f"computer picked {computer} you picked {player}")
    else:
        print("you loss!")
        print(f"computer picked {computer} you picked {player}")
    if input("play again?y/n: ").lower() == "n":
        playing = False

print("\nthanks for playing")
print("------------------------------------------------")