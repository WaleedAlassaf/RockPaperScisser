import random

def game():
    CPU = random.randint(1,3)
    print(CPU)
    player= input("please enter Rock, Paper or Scissers")

    if int(CPU) == 1:
        CPU = "Rock"
    elif int(CPU) == 2:
        CPU = "Paper"
    elif int(CPU) == 3:
        CPU = "Scissers"

    if CPU == "Rock" and player == "Paper":
        print("CPU choose Rock and choose Paper you win!")
    elif CPU == "Rock" and player == "Scissers":
        print("CPU choose Rock and you choose Scissers you lost")
    elif CPU == "Rock" and player == "Rock":
        print("You and the CPU choose Rock, its a tie")

    elif CPU == "Paper" and player == "Scissers":
        print("CPU choose Paper and you Scissers you win")
    elif CPU == "Paper" and player == "Rock":
        print("CPU paper and you rock you lost")
    elif CPU == "Paper" and player == "Paper":
        print("You and the CPU choose Rock, its a tie")

    elif CPU == "Scissers" and player == "Paper":
        print("CPU choose Scissers and you Paper you lost")
    elif CPU == "Scissers" and player == "Rock":
        print("CPU Scissers and you rock you win")
    elif CPU == "Scissers" and player == "Scissers":
        print("You and the CPU choose Scisser, its a tie")
    else:
        print("You might have inputed a wrong word")

    restart = input("go again ? Y/N")
    if restart == "y":
        game()
    elif restart == "n":
        print("Thanks for playing")

game()