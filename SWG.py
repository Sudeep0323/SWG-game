#Welcome to the snake ,water or gun game!
import random

dict={"snake":-1,
     "water":0,
     "gun":1}

reversedist={-1:"snake" ,
             0:"water",
             1:"gun"}

while True:
    computer = random.choice([-1,0,1])
    yourstr = input("enter you choice(snake,water,gun) or type 'exit' to quit :")

    if yourstr == 'exit':
        print("Thank for playing!")
        break

    if yourstr in dict:
        you = dict[yourstr]
        print(f"you chose:{reversedist[you]}\ncomputer chose:{reversedist[computer]}")

        if computer == you:
            print("It is Draw!")
        else:
            if(computer == -1 and you == 0 and computer == 0 and you == 1 or computer == 1 and you == 0):
                print("you Win!")
            else:
                print("you lose!")
    else:
        print("Envaild chose,please tpye(snake,,water or gun!")