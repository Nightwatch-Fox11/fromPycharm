'''def feibo(n):
    result = [1,1]
    for i in range(n-2):
        result.append(result[-1]+result[-2])
    return result
print(feibo(10))
x1 =2
x2 = 1
x3 =9
x4 =12
print("x1={},x2={},x3={},x4={}".format(x1,x2,x3,x4))
print(2**2)'''
def fib(n):
    if n == 1or n == 0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(36))

