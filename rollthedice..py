# Rolling-the-dice-game
import random
all = (1,2,3,4,5,6)
length = 1
temp1 = random.sample(all,length)
temp2 = random.sample(all,length)
#print(temp1, temp2)
rolling = (input("rolling the dice(y/n): "))
if rolling == "y" or rolling == "Y":
    print(temp1,temp2)
elif rolling == "n" or rolling == "N":
    print("game is completed, thank you")
else:
    print("invalid command")

