# Countdown
def countDown(x):
    count=[]
    for x in range(x,-1,-1):
        count.append(x)
    return count
print(countDown(5))

# Print and Return
def printReturn(y):
    print(y[0])
    return y[1]
print (printReturn([3,4]))

# First Plus Length 
def plusLength(z):
    sum=z[0]+len(z)
    return sum
print(plusLength([1,2,3,4,5]))

#Values Greater than Second
def greaterThan(v):
    new_list=[]
    for i in range(len(v)):
        if len(v) < 2:
            return False
        elif v[i] > v[1]:
            new_list.append(v[i])
    return new_list
print(greaterThan([5,2,3,2,1,4]))

#This Length, That Value 
def lengthValue(c,b):
    new_list_two=[]
    for i in range(c):
        new_list_two.append(b)
    return new_list_two
print(lengthValue(4,7))


