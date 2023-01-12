def sum(n):
    if n==0:
        return n
    else:
        return(n + sum(n-1))
x=int(input('Please input your number :'))
print(sum(x))

    
