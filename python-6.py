import random
computer=random.randint(1,10)
player=int(input("guess the number between 1 to 10 "))
if player==computer:
    print("well done you guessed the number correct ")
else:
    print("try again 1")