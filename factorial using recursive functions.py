# factorial finder
n=int(input("Please input the number you wish to find factorial : "))
def recursive_function(n):
    if n == 1 or n == 0:
        return 1
    return n * recursive_function (n-1)
print(recursive_function(n))

#recursion is a function which calls itself.
