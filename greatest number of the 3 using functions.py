x=int(input('please enter your first number:'))
y=int(input('please enter your second number:'))
z=int(input('please enter your third number:'))
def greatest_number(max1,max2,max3):
    if max1>max2:
        if max1>max3:    
            return max1
        else:
            return max3
    else:
        if max3>max2:
            return max3
        else:
            return max2
m=greatest_number(x,y,z)
print("The greatest number is:",m)
            



