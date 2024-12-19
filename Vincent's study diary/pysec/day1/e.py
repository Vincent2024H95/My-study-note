cj=input("输入成绩：")
cj=int(cj)
if cj<0 or cj>100:
    print("Error")
else:
    if cj<60:
        print("不及格")
    elif 60 < cj <= 80:
        print("良")
    elif 80 < cj <= 90:
        print("优")
    else:
        print("秀儿")

