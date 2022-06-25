def reverseNumber(num):
    result = 0
    while num > 0:
        remainder = num % 10
        result = result * 10 + remainder
        num //=10
    return result
print(reverseNumber(123))
