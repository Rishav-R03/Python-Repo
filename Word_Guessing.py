import random

name = input("What is your name ?? ")
print("Good Luck ! ",name)

words = ["Ape","Car","Bar","Ear","Far"]

word = random.choice(words)

print("Guess the characters : ")
guesses = ""

turns = 12

while turns>0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_")
            failed +=1
    if failed == 0:
        print("You win")
        print("The word is : ",word)
        break

print()
guess = input("Guess a character ")
guesses += guess

if guess not in word:
    turns -=1
    print("Wrong")

    print("You have",+turns,"more guess")
    if turns == 0:
        print("You lost")