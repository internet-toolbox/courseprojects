import random as rand

yescounter = 0

while yescounter < 10:

    randomyr = rand.randint(1945,1960)
    usrinput = input("Your grandpa likes it when you talk.Be nice to him: ")

    if usrinput.isupper():
        print("NO, NOT SINCE" , randomyr , "!")

    if usrinput.islower():
        print("HUH?! SPEAK LOUD KID!")

    if usrinput.lower() == "bye":
        yescounter+=1

    if yescounter == 3:
        print("You can leave now")
