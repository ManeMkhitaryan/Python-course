def divisors(num):
    arr = []
    for i in range(1,num//2+1):
        if(num % i == 0):
            arr.append(i)
    return arr
print(divisors(28))
