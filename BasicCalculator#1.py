
userName = input("Enter your name: ")
userNumber1 = int(input("Enter your first number: "))
userNumber2 = int(input("Enter your second number: "))

subtractedNumber = userNumber1 - userNumber2
addedNumber = userNumber1 + userNumber2
multipliedNumber = userNumber1 * userNumber2
dividedNumber = userNumber1 / userNumber2

print()
print("=== Results ===")
print("Name:", userName)
print("Subtracted:", subtractedNumber)
print("Added:", addedNumber)
print("Multiplied:", multipliedNumber)
print("Divided:", dividedNumber)

print()
input("Press Enter to exit...")