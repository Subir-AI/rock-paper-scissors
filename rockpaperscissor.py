print("===ROCK PAPER SCISSOR GAME===")
import random 
choices = ["rock", "paper","scissor"]

user = input("Choose one :").lower()

computer = random.choice(choices)
print("computer chose :",computer)

if(user == computer):
    print("Its a Draw")
elif(user == "rock"):
    if(computer == "scissor"):
        print("You win!!!")
    else:
        print("Computer win")
elif(user == "paper"):
    if(computer == "rock"):
        print("You win!!!")
    else:
        print("Computer win")
elif(user == "scissor"):
    if(computer == "paper"):
          print("You win!!!")
    else:
        print("Computer win")
else:
    print("Invalid input")
                