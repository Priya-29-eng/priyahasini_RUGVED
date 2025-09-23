# Define the function
def triple_and(a, b, c):
    if a != "" and a != "0" and b != "" and b != "0" and c != "" and c != "0":
        return True
    else:
        return False

a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")


print(triple_and(a, b, c))
