import random

robotnum=random.randint(1,30)
while True:
    personnum=int(input("输入数字0-30："))
    if personnum>robotnum:
        print("猜大了")
    elif personnum<robotnum:
        print("猜小了")
    else:
        print("猜对了")
        break
