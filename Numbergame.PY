import random
playing = True
number = str(random.randint(0,9))
print("Guess what number I am thinking")
while playing:
    guess = input("guess the number :")
    if playing == guess:
        print("You won")
        print("the number was", number)
        break
    else:
        print("You lost")