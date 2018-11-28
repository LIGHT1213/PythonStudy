# Guess my number

import random
print("welcome to 'Gues my number")
print("I am thinking of a number between 1 and 100")
print("try to guess it as few attempts as possible")


the_number=random.randint(1,100)
guess=int(input("Take a guess:"))
tries=1
while guess!=the_number:
    if guess>the_number:
        print("Lower..")
    else:
        print("Higner..")

    guess=int(input("Take a guess:"))
    tries+=1

print("You guessed it! The number was",the_number)
print("And it only took you ",tries,"tries!\n")
