import random

computer = random.choice([0,-1,1])
youstr=input("Enter Your choice : ")
youdict= {"s":1,"w":-1,"g":0}
r={1:"Snake",-1:"Water",0:"Gun"}

you = youdict[youstr]

print(f"You choice {r[you]}\n Computer choice {r[computer]}")

if(computer == you):
    print("It's a drow")
else:
    if(computer - you == -1 or computer - you == 2 ):
        print("you lose!")
    else:
        print("You win!")


