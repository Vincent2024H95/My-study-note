data = int(input("输入数字:"))
sum0 = 0
num = 0
while num <= data:
    sum0 += num  # 这里改为累加num，而不是data
    num += 1  # 让计数变量num自增1，来逐步遍历从0到data的每个数
print(sum0)
#按需输入