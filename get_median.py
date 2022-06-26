data = [2,8,5,6,8,9,4,23,5,7]

def calculateMedian(data):
    MERGE_SORT(data)
    if(len(data) % 2 == 0):
        return (data[len(data)//2] + data[len(data)//2 - 1]) / 2
    else:
        return data[len(data)//2]
    
def MERGE_SORT(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n//2
    S1 = arr[:mid]
    S2 = arr[mid:]
    
    MERGE_SORT(S1)
    MERGE_SORT(S2)
    MERGE(S1,S2,arr)
    
    
def MERGE(S1,S2,arr):
    i = 0
    j = 0
    while (i+j) < len(arr):
        if(j == len(S2) or i < len(S1) and S1[i] < S2[j]):
            arr[i+j] = S1[i]
            i+= 1
        else:
            arr[i+j] = S2[j]
            j += 1
            
print(calculateMedian(data))
