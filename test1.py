print("Guess the number I'm thinking: ")
secret = 47
attemps = 5

while attemps > 0:
    answer = int(input("Enter your guess: "))
    if answer == secret:
        print("Correct!")
        break
    elif answer < secret:
        print("Too low, try again")
    else:
        print("Too high, try again")
    attemps = attemps-1
    print("Attemps left: ", attemps)

if attemps == 0:
    print("Oh no, game over, the number was:", secret)