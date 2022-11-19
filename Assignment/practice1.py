def Palindrome(x):
    i = 0
    j = int(len(x)/2)
    bool = True
    while j > i:
        if(x[i] != x[len(x)-i-1]):
          bool = False
          break
        i+=1
    return bool


x = input("Enter a number: ")
if(Palindrome(x)):
    print("The number is palindrome")
else:
    print("The number not is palindrome")
