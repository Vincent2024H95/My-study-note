import random

while True:
    pchoice = input("出拳：")
    quan = ["石头", "剪刀", "布"]
    robotchoice = random.choice(quan)
    winlist = ["石头剪刀", "剪刀布", "布石头"]
    if pchoice in quan:
        if pchoice + robotchoice in winlist:
            print(f"你出的:{pchoice},机器出的:{robotchoice},你赢了")
            break
        elif pchoice == robotchoice:
            print(f"你出的:{pchoice},机器出的:{robotchoice},平局")
            break
        else:
            print(f"你出的:{pchoice},机器出的:{robotchoice},你输了")
            break
    else:
        print("输入有误，请重新输入石头、剪刀或布。")