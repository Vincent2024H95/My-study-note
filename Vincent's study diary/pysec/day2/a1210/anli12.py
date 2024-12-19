import random
quan=["石头","剪刀","布"]
winlist=["石头剪刀","剪刀布","布石头"]

wincount=0
losecount=0
while 1:
    pchoicenum = int(input("输入猜拳：0-石头，1-剪刀，2-布："))
    if not pchoicenum in range(0,3):
        #如果不是0.1.2则轮空
        continue
    robotchoice = random.choice(quan)  # 从列表随机抽取一个字符串
    pchoice=quan[pchoicenum]

    if pchoice + robotchoice in winlist:
        print(f"你出的是{pchoice}，机器出的是{robotchoice}，你赢了")
        wincount += 1
    elif pchoice == robotchoice:
        print(f"你出的是{pchoice}，机器出的是{robotchoice}，平局")
        losecount += 1
    else:
        print(f"你出的是{pchoice}，机器出的是{robotchoice}，你输了")
        losecount += 1

    if wincount == 2:
        print("游戏结束，你赢了")
        break
    elif losecount == 2:
        print("游戏结束，你输了")
        break