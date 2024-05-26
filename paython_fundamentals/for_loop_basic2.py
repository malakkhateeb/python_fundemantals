def bigSize(z):
    for i in range(len(z)):
        if z[i] > 0:
            z[i]= "big"
    return z
print (bigSize([-1, 3, 5, -5]))

# Count Positives
def count_positives(lst):
    count_positive = 0
    for num in lst:
        if num > 0:
            count_positive += 1
    lst[-1] = count_positive
    return lst

# Test cases
print(count_positives([-1, 1, 1, 1]))  # Output: [-1, 1, 1, 3]
print(count_positives([1, 6, -4, -2, -7, -2]))  # Output: [1, 6, -4, -2, -7, 2]
#Sum Total
def sumList(list):
    sum=0
    for i in list:
        sum+=i
    return sum
print(sumList([1,2,3,4]))
#Average
def avg(list):
    sum=0
    for i in list:
        sum+=i
        avg=sum/len(list)
    return avg
print(avg([1,2,3,4]))
# Length
def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))
# minimum index
def minIndex(list):
    if len(list)==0:
        return False
    else:
        min=list[0]
        for i in list:
            if i < min:
                min=i
        return min
print(minIndex([37, 2, 1, -9]))
print(minIndex([])) 
# max valu
def maxIndex(list):
    if len(list)==0:
        return False
    else:
        max=list[0]
        for i in list:
            if i >  max:
                max=i
        return max
print(maxIndex([37, 2, 1, -9]))
print(maxIndex([])) 
#Ultimate Analysis
def ultimateAna(list):
    analysis = {
        'sumTotal': sumList(list),
        'average': avg(list),
        'minimum': minIndex(list),
        'maximum':maxIndex(list),
        'length': length(list)
    }
    return analysis
print( ultimateAna([37, 2, 1, -9]))
# Reverse List
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        # Swap
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
lst = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(lst))


