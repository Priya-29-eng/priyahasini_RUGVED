n = int(input("enter a value\n"))
fib1= 0
fib2 =1
print(fib1 , end = " ")
print(fib2, end = " ")
for i in range(n-2):
    
    fib3 = fib1 + fib2
    print(fib3, end = " " )
    fib1 = fib2
    fib2 = fib3
