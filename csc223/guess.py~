import random
answer=random.randint(1,100)

while True:
    guess = input("Guess a number ")
    try:
        int(guess)
    except:
        print("You must enter a number")
        continue
    if answer == int(guess):
        print("You won")
        break
    elif answer < int(guess):
        print("Too High")
    else: 
        print("Too Low")
