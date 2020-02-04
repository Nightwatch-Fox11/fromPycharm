#求分数和1+1/2+1/3+...+1/x
'''x =int(input("请输入数字: "))
sum =0
for i in range(1,x+1):
    sum += float(1/i)
print("{:.3f}".format(sum))'''
#列表推导式法
'''x =int(input("请输入数字: "))
sum2 = sum([float(1/i) for i in range(1,x+1)])
print("{:.3f}".format(sum2))'''
'''x =int(input("请输入数字: "))
sum3 = sum([float(i/(2*i-1))*((-1)**(i+1)) for i in range(1,x+1)])
print("{:.3f}".format(sum3))'''
#抽签(一）
'''import random
a = [i for i in range(1,51)]
x = int(input("请输入人数: "))
for i in range(x):
    print(random.choice(a), end = ' ')'''
#抽签(二）相比于（一）避免了重复，操作相对简简洁
import random
x = int(input("请输入班级总人数: "))
a= [i for i in range(1,x+1)]
random.shuffle(a)
y = int(input("请输入需要人数: "))
for i in range(y):
    print(a[i],end=' ')