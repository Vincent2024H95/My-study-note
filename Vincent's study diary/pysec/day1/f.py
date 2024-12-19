import random
personnum=int(input("enter your person number:"))
robotnum=random.randint(1,10)

if personnum>robotnum:
    print("大了")
elif personnum<robotnum:
    print("小了")
else:
    print("对了")