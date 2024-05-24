
# Print all integers from 0 to 150.
for x in range (151):
    print(x)
# Print all the multiples of 5 from 5 to 1,000
for y in range(5,1001,5):
    print(y)
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for z in range(1,101):
    if(z%5==0):
        print("coding")
    else:
        print("Coding Dojo")
# Add odd integers from 0 to 500,000, and print the final sum.
total_sum = 0
for i in range(1, 500001, 2):
    total_sum += i
print(total_sum) 
#  Print positive numbers starting at 2018, counting down by fours.
for m in range(2018,0,-4):
    print(m)
# Flexible Counter
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if (i%mult==0):
        print(i)
        