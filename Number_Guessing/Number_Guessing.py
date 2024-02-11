from tkinter import *
import random

num = random.random()*100
comp = int(num)
print(comp)
count = 1
health = 100
for i in range(0,10):
    user = int(input("enter your guess :"))

    if(user==comp):
        print("You win :) ")
        print("You took ",count," chances to win :")
        break
        
    else:
        count = count + 1
        health = health - 10
        print("You lost :(")
        if(comp>user):
            print("Increase your guess :")
        elif(comp<user):
            print("Lower your guess :")
        if(health<0):
            print("your health is finished :")
            break
    


    