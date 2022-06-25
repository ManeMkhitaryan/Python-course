def getMax(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        if result < arr[i]:
            result = arr[i]
    return result

def getMin(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        if result > arr[i]:
            result = arr[i]
    return result

def sum(arr):
    min = getMin(arr)
    max = getMax(arr)
    return min + max

print(sum([10,2,32,45,-6,89,2,0]))
