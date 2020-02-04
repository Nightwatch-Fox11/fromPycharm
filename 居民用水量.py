x = float(input('请输入用水量: '))
if x <=15:
    y = 4*x/3
else:
    y = 2.5*x-17.5
print("{:.2f}".format(y))