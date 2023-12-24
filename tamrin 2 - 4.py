import random
n = int(input("How many times do you want to roll the dice: "))
for i in range(n):
    dice = random.randint(1,6)
    print("*", dice, "*")
    if dice==6:
       for i in range (1):
         print("You have another chance!")
         dice = random.randint(1,6)
         print("->", dice)