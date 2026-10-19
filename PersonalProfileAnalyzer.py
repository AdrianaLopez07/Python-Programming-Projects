
userName = input("What is your name? ")
userAge = int(input("How old are you? "))
userNumber = int(input("What is your favorite number(it may be negative/positive)? "))
isStudent = (input("Are you a student? "))

print()

print("=== Profile Report ===")

print("Name:", userName)

if userAge >= 65:
    print("You are a senior.")
elif userAge >=18:
    print("You are an adult.")
elif userAge >=13:
    print("You are a teenager.")
else:
    print("You are a child.")

if userNumber >0:
    print("Your favorite number is positive.")
elif userNumber <0:
    print("Your favorite number is negative.")
else:
    print("Your favorite number is zero.")


if userNumber % 2 == 0:
    print("Your favorite number is even.")
else:
    print("Your favorite number is odd.")


if isStudent == "yes" or isStudent == "Yes":
    print("You are a student.")
elif isStudent =="no" or isStudent == "No":
    print("You are not a student.")


print()

if userAge >= 65:
    print("Experience is your advantage! *^____^*")
elif userAge >=30:
    print("Keep building toward your goals! ( •̀ ω •́ )✧")
elif userAge >=18:
    print("You're in an exciting stage of life! ヾ(￣▽￣)")
else:
    print("You have plenty of time to explore your future! (*^▽^*)")

print("======================")

print()

input("Press enter to exit...")






