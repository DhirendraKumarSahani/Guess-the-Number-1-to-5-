import random
target = random.randint(1, 5)

while True:
    userChoice = input("Guess the target or quit : ")
    if(userChoice == "quit"):
        break
    userChoice  = int(userChoice)
    if(target == userChoice):
        print("Success : Correct Guess!!")
        break
    elif(target > userChoice):
        print("Your number is too small. Take a bigger guess..")

    else:
        print("Your number was too big. Take a smaller guess..")

print("--------GAME OVER--------")