import random

lowest=0
highest=100
output=random.randint(lowest,highest)
guesses=0
running=True

print("This is PYTHON number guessing game")
print(f"enter a number between {lowest} and {highest}")

while running:
    guess=input("enter a guess:")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess<output:
            print("The number is LOW! TRY AGAIN")
        elif guess>output:
            print("The number is HIGH! TRY AGAIN")
        else:
            print("your guess is correct")
            break

    else :
        print("invalid syntax")
        print(f"enter a number between {lowest} and {highest}")
    
