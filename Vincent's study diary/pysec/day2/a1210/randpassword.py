#100个随机8位密码
import random
import string

str_range=string.ascii_letters+string.digits+string.punctuation
i=0
while i<100:
    i+=1
    password = ""
    num = 0
    while num<8:
        num+=1
        password+=random.choice(str_range)
    print(password)
