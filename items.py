def items():
    print("For quitting click Enter two times")
    words = input("Insert you word here ")
    arr = []
    while words != "":
        if(words not in arr):
            arr.append(words)
        words = input()
    return arr
print(items())
