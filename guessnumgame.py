import random
num=random.randint(1,9)
guess=int(input("enter a number what i guess(from 1 to 9)\n"))
while guess!=num:
    if guess<num:
        print ("you guessed lower")
    else:
        print("you guessed higher")
    guess=int(input ("guess again"))
      
print ("you won the match")
    