def reverse_string():
    word = input("enter the word you'd like to reverse ")
    str = ""
    for i in word:
        str = i + str
    return str

print(reverse_string())
