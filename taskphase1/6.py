str = input("enter a string\n")
n = len(str)
ispal = 1
for i in range(n):
    if (str[i] != str[n-i-1]):
        ispal = 0
        break
if(ispal==1):
    print("palindrome")
else:
    print("not a palindrome")