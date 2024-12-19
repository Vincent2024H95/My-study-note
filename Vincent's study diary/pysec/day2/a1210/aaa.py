#猜拳目标
#每一次游戏开始
import random
quan=["石头","剪刀","布"]#列表
winlist=["石头剪刀","剪刀布","布石头"]#定义人赢的列表

#if (pchoice=="石头"and robotchoice=="剪刀") or (pchoice=="剪刀" and robotchoice=="布") or (pchoice=="布"and robotchoice=="石头"):
    #and优先级高于or
    #判断人与机器出拳的组合是否在winlist
"""
if pchoice+robotchoice in winlist:
    print(f"你出的:{pchoice},机器出的:{robotchoice},你赢了")
elif pchoice==robotchoice:
    print(f"你出的:{pchoice},机器出的:{robotchoice},平局")
else:
    print(f"你出的:{pchoice},机器出的:{robotchoice},你输了")
"""
num=0
while num<3:
    num+=1
    pchoice = input("出拳：")
    robotchoice = random.choice(quan)  # 从列表随机抽取一个字符串
    if pchoice + robotchoice in winlist:
        print(f"你出的:{pchoice},机器出的:{robotchoice},你赢了")
    elif pchoice == robotchoice:
        print(f"你出的:{pchoice},机器出的:{robotchoice},平局")
    else:
        print(f"你出的:{pchoice},机器出的:{robotchoice},你输了")