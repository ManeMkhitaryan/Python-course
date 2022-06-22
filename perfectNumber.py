def perfectNumber(num):
    sum = 0
    for i in range (1,num//2+1):
        if(num % i == 0):
            sum = sum + i # sum = 1  # sum = 1 + 2 = 3   
            print(sum)
    return sum == num
print(perfectNumber(28))
