number = None
count = 0
numbers =[]

print("Enter a number: ")

number = int(input())
count = count + 1
numbers.append(number)

if number % 2 == 0:
    print("This number is even!")
    print()
    if count == 1:
        print("You entered 1 number.")
    else:
        print(f"You entered {count} numbers.")
else:
    print("This number is odd!")
    print()
    if count == 1:
        print("You entered 1 number.")
    else:
        print(f"You entered {count} numbers.")
