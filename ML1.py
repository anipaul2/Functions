number = int(input("Enter a number: "))
print("The multiplication table of: ", number)
for i in range(1, 11):
    print(number, "x", i, "=", number*i)