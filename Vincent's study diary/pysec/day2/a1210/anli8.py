import random

robotnum=random.randint(1,10)
i=0
while i<5:
    i+=1
    personnum=int(input("输入数字（1-10）："))
    if personnum>robotnum:
        print("猜大了")
    elif personnum<robotnum:
        print("猜小了")
    else:
        print("猜对了")
        break
