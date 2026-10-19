
regular_ticket:float = 12.50
student_ticket:float = 10.0
senior_ticket:float = 8.0

print("Movie tickets:")
print("======================")
print("Regular ticket - ", regular_ticket, "$")
print("Student ticket - ", student_ticket, "$")
print("Senior ticket - ", senior_ticket, "$")
print("======================")

print()

customer_name = input("Name: ")
customer_age = int(input("Age: "))
customer_ticket = input("Which ticket would you like? ")
num_tickets = int(input("How many tickets would you like to buy? "))
print()



def ticket_information (customer_name, customer_age, num_tickets, customer_ticket):

        print(" ************* Movie Ticket Booth *************")
        print("Name:", customer_name)
        print("Age:", customer_age)


        if customer_ticket == "regular":
            print("Ticket type: regular")
        elif customer_ticket == "student":
            print("Ticket type: student")
        else:
            print("Ticket type: senior")

        print("Number of tickets:", num_tickets)


def receipt_information(customer_ticket, num_tickets):
    print(" ************* Receipt *************")
    print("Customer - ", customer_name )
    print("Ticket type - ", customer_ticket)

    print("Tickets - ", num_tickets)
    print("Total - $ ")



ticket_information(customer_name, customer_age, num_tickets, customer_ticket)