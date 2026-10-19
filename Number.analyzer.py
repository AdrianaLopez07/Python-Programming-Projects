

starting_number = int(input("Enter your first number: "))
ending_number = int(input("Enter your last number: "))

print()
print("=============== Number Analyzer ================")





def analyze_numbers(starting_number, ending_number):

    even_count = 0
    odd_count = 0

    for number in range(starting_number, ending_number + 1):

        if number % 2 == 0:
            print(number, " - Even")
            even_count +=1
        else:
            print(number, " - Odd")
            odd_count +=1
    print()
    print("================================================")
    print("Total even numbers : ", even_count)
    print("Total odd numbers : ", odd_count)



analyze_numbers(starting_number, ending_number)

print("================================================")

input("Press enter to exit...")