num = input("Enter a number: ")

i = 0
n = len(num)

while i + 1 < n and num[i] < num[i + 1]:
    i = i + 1

if i == 0 or i == n - 1:
    print("Not a hill number")
else:
    while i + 1 < n and num[i] > num[i + 1]:
        i =  i + 1

    if i == n - 1:
        print("Hill number")
    else:
        print("Not a hill number")
