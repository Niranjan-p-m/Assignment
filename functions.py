def add(*integers):
    res=0
    for i in integers:
        res += i
    return res

def sub(*integers):
    res=0
    for i in integers:
        res -= i
    return res

def fact(number):
    res=1
    for i in range(1,number+1):
        res *= i
    return res

def fun(op,a,b):
    if op == 'add' :
        return a+b
    elif op == 'sub':
        return b-a
    elif op == 'mul':
        return a*b
    elif op == 'div':
        return b/a
    else:
        return 'Not a valid operation'




def fibonacci(n):
    a=0
    b=1
    if n<0:
        print('Enter the valid number')
    elif n==0:
        return 0
    elif n ==1:
        return 1
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b


print(add(1,2,3))
print(sub(6,3,1))
print(fact(6))
print(fibonacci(9))
print(fun('add',1,2))