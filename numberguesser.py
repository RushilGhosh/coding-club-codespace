import random

def randomNumGen():
    bark = random.randint(0,10)
    return bark

#meow = 0
ribbit = randomNumGen()

while True: 
    meow = int(input("guess a number"))
    if meow == ribbit:
        print("you win")
        break
    else: 
        print("go again")
    



