##########################################################
# Student: Andrius Busilas
# Assignment 1 Part 2 of 3
# Project: Customer Identity Book (CIB) 

# Github: https://github.com/busilas 
# Repo: https://github.com/busilas/cib

# Course: Launching into Computer Science November 2023
# School: University of Essex
# Date: February, 2024
##########################################################


##########################################################
# FUNCTIONS
##########################################################

# Function to display the menu
def display_menu():
    print("\nMain Menu\n")
    print("1 ) Add Customers")
    print("2 ) Remove Customers")
    print("3 ) Search Customers")
    print("4 ) Update Customer Details")
    print("5 ) Show All Customers Details")
    print("6 ) Sort Customers (Ascending)")
    print("7 ) Sort Customers (Descending)")
    print("0 ) Quit")

# Function to check if customers list is empty
def is_customers_empty():
    return not customers

# Function to sort customers in ascending order based on Last_name
def sort_ascending(customers):
    # Get the number of customers in the list
    n = len(customers)
    # Outer loop: Iterate through all elements in the list
    for i in range(n - 1):
        # Inner loop: Iterate through the unsorted part of the list
        for j in range(0, n - i - 1):
            # Compare Last_Name for adjacent customers and swap if necessary
            if customers[j]["Last_name"] > customers[j + 1]["Last_name"]:
                # Swap the positions of the customers
                customers[j], customers[j + 1] = customers[j + 1], customers[j]

# Function to sort customers in descending order based on Last_name
def sort_descending(customers):
    # Get the number of customers in the list
    n = len(customers)
    # Outer loop: Iterate through all elements in the list
    for i in range(n - 1):
        # Inner loop: Iterate through the unsorted part of the list
        for j in range(0, n - i - 1):
            # Compare Last_Name for adjacent customers and swap if necessary
            if customers[j]["Last_name"] < customers[j + 1]["Last_name"]:
                # Swap the positions of the customers
                customers[j], customers[j + 1] = customers[j + 1], customers[j]

# Function to validate email
def validate_email(email):
    # Check if the email has the correct structure
    if '@' in email and '.' in email:
        # Split the email into local part and domain part
        local_part, domain_part = email.split('@')
        # Check if the local and domain parts are not empty
        if local_part and domain_part:
            # Check if the domain part has at least one dot (.)
            if '.' in domain_part:
                return True
    # If any condition fails, the email is considered invalid
    return False

# Function to validate phone number
def validate_phone_number(phone_number):
    # Check if the phone number is composed only of digits and has a length of 9
    return phone_number.isdigit() and len(phone_number) == 9

# Function to validate birth date
def validate_birth_date(birth_date):
    # Check if the birth date is composed only of digits and has a length of 8
    return birth_date.isdigit() and len(birth_date) == 8

# Function to validate ID number
def validate_id_number(id_number):
    # Check if the ID number is composed only of digits and has a length of 6
    return id_number.isdigit() and len(id_number) == 6

##########################################################
# CUSTOMER OBJECT
##########################################################

# Define the Customer object with properties
Customer = {
    "Last_name": None,
    "First_name": None,
    "Birth_date": None,
    "Address": None,
    "Id_number": None,
    "E_mail": None,
    "Phone_number": None
}

# Initialize an empty list to store customer objects
customers = []

##########################################################
# DATA COLLECTION
##########################################################

# Set the number of iterations to 5
num = 2

# Loop to gather customer information from user input
for i in range(num):
    # Create a new customer object
    customer = Customer.copy()
    # Prompt user for customer information
    print("\nPlease enter the following details: ")
    customer["Last_name"] = input("Last Name: ")
    customer["First_name"] = input("First Name: ")
    # Validate birth date format using the validate_birth_date function
    birth_date = input("Birth Date (YYYYMMDD): ")
    while not validate_birth_date(birth_date):
        print("Invalid birth date format. Please enter YYYYMMDD.")
        birth_date = input("Birth Date (YYYYMMDD): ")
    customer["Birth_date"] = int(birth_date)
    customer["Address"] = input("Address: ")
    # Validate ID Number format using the validate_id_number function
    id_number = input("ID Number (min 6-digits): ")
    while not validate_id_number(id_number):
        print("Invalid ID Number format. Please enter min 6 digits.")
        id_number = input("ID Number (min 6-digits): ")
    customer["Id_number"] = int(id_number)
    # Validate email format using the validate_email function
    email = input("Email: ")
    while not validate_email(email):
        email = input("Invalid email format. Please enter a valid email address: ")
    customer["E_mail"] = email
    # Validate phone number format using the validate_phone_number function
    phone_number = input("Phone Number (9-digit): ")
    while not validate_phone_number(phone_number):
        print("Invalid phone number format. Please enter a valid 9-digit phone number.")
        phone_number = input("Phone Number (9-digit): ")
    customer["Phone_number"] = int(phone_number)
    # Append the customer object to the list
    customers.append(customer)

# Show collected customers details
# Display header for the collected data
print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
# Loop to print customer details
for idx, customer in enumerate(customers, 1):
    print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
        idx, customer["Last_name"], customer["First_name"], customer["Birth_date"],
        customer["Address"], customer["Id_number"], customer["E_mail"], customer["Phone_number"]
    ))

##########################################################
# MAIN LOOP
##########################################################
    
# Main loop for code execution
while True:
    # Display the menu
    display_menu()
    # Prompt user for menu choice
    choice = input("\nEnter your choice (0-7): ")

    # User input to add customer
    if choice == '1':
        # Add Customers
        # Create a copy of the Customer template to store user input
        customer = Customer.copy()
        # Prompt the user to enter the following details
        print("\nPlease enter the following details: ")
        # Collect user input for customer details
        customer["Last_name"] = input("Last Name: ")
        customer["First_name"] = input("First Name: ")
        # Validate birth date format using the validate_birth_date function
        birth_date = input("Birth Date (YYYYMMDD): ")
        while not validate_birth_date(birth_date):
            print("Invalid birth date format. Please enter YYYYMMDD.")
            birth_date = input("Birth Date (YYYYMMDD): ")
        customer["Birth_date"] = int(birth_date)
        customer["Address"] = input("Address: ")
        # Validate ID Number format using the validate_id_number function
        id_number = input("ID Number (min 6-digits): ")
        while not validate_id_number(id_number):
            print("Invalid ID Number format. Please enter min 6 digits.")
            id_number = input("ID Number (min 6-digits): ")
        customer["Id_number"] = int(id_number)
        # Validate email format using the validate_email function
        email = input("Email: ")
        while not validate_email(email):
            email = input("Invalid email format. Please enter a valid email address: ")
        customer["E_mail"] = email
        # Validate phone number format using the validate_phone_number function
        phone_number = input("Phone Number (9-digit): ")
        while not validate_phone_number(phone_number):
            print("Invalid phone number format. Please enter a valid 9-digit phone number.")
        phone_number = input("Phone Number (9-digit): ")
        customer["Phone_number"] = int(phone_number)
        # Append the customer details to the list of customers
        customers.append(customer)
        # Display a success message with a check mark symbol
        print("\nCustomer details saved successfully \N{check mark}")

    # User input to remove customer
    elif choice == '2':
        # Calls function to check if customers list is empty
        if is_customers_empty():
            # Display a message if the customers list is empty
            print("No customers to remove. Please add a new customer and try again.")
        else:
            # Remove Customers
            # Prompt the user to enter the Last Name of the customer to remove
            remove_last_name = input("Enter the Last Name of the customer to remove: ")
            # Create a list of customers with matching Last Names (case-insensitive)
            removed_contacts = [customer for customer in customers if customer["Last_name"].lower() == remove_last_name.lower()]
            # Check if there are matching customers to remove
            if removed_contacts:
                # Iterate through the list of matching customers and remove them
                for removed_contact in removed_contacts:
                    customers.remove(removed_contact)
                # Display a success message
                print("Customers with Last Name '{}' removed successfully.".format(remove_last_name))
            else:
                # Display a message if no customers were found with the specified Last Name
                print("No customers found with Last Name '{}'.".format(remove_last_name))

    # User input to search customer by the Last Name
    elif choice == '3':
        # Calls function to check if customers list is empty
        if is_customers_empty():
            # Inform the user if the customers list is empty
            print("No customers to search. Please add a new customer and try again.")
        else:
            # Search Customers
            # Prompt user to enter the customer's Last Name for search
            search_term = input("\nEnter customer Last Name: ")
            # Displaying the search result header
            print("Search result:")
            # Initializes a variable to keep track of whether a match is found during the search
            found = False
            # Iterate through each customer to find a match
            for customer in customers:
                # Check if the search term is present in either First Name or Last Name (case-insensitive)
                if search_term.lower() in customer["Last_name"].lower():
                    # Display relevant details for the found customer
                    print("Name: {} {}, ID Number: {}".format(customer["First_name"], customer["Last_name"], customer["Id_number"]))
                    # Indicate that a match has been found
                    found = True
            # Inform the user if no match is found
            if not found:
                print("Name not found")

    # User input to update customer details
    elif choice == '4':
        # Calls function to check if customers list is empty
        if is_customers_empty():
            print("No customers to update. Please add a new customer and try again.")
        else:
            # Update Customer Details
            # Prompt user to enter the Last Name of the customer to update
            update_last_name = input("\nEnter the Last Name of the customer to update: ")            
            # Create a list of customers matching the entered Last Name
            update_customers = [customer for customer in customers if customer["Last_name"].lower() == update_last_name.lower()]
            if update_customers:
                # Display customer details for the user to choose from
                for customer in update_customers:
                    print("\nUpdate Customer Details for:\n")
                    # Display header for customer details
                    print("\nID\t\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
                    # Display current customer details
                    print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                        customers.index(customer) + 1, customer["Last_name"], customer["First_name"], 
                        customer["Birth_date"], customer["Address"], customer["Id_number"], customer["E_mail"], 
                        customer["Phone_number"]
                    ))

                    # Prompt user for updated information
                    print("\nPlease enter the following details to update: ")
                    customer["Last_name"] = input("Last Name: ")
                    customer["First_name"] = input("First Name: ")
                    # Validate birth date format using the validate_birth_date function
                    birth_date = input("Birth Date (YYYYMMDD): ")
                    while not validate_birth_date(birth_date):
                        print("Invalid birth date format. Please enter YYYYMMDD.")
                        birth_date = input("Birth Date (YYYYMMDD): ")
                    customer["Birth_date"] = int(birth_date)
                    customer["Address"] = input("Address: ")
                    # Validate ID Number format using the validate_id_number function
                    id_number = input("ID Number (min 6-digits): ")
                    while not validate_id_number(id_number):
                        print("Invalid ID Number format. Please enter min 6 digits.")
                        id_number = input("ID Number (min 6-digits): ")
                    customer["Id_number"] = int(id_number)
                    # Validate email format using the validate_email function
                    email = input("Email: ")
                    while not validate_email(email):
                        email = input("Invalid email format. Please enter a valid email address: ")
                    customer["E_mail"] = email
                    # Validate phone number format using the validate_phone_number function
                    phone_number = input("Phone Number (9-digit): ")
                    while not validate_phone_number(phone_number):
                        print("Invalid phone number format. Please enter a valid 9-digit phone number.")
                    phone_number = input("Phone Number (9-digit): ")
                    customer["Phone_number"] = int(phone_number)
                    # Display a success message
                    print("\nCustomer details updated successfully.")
            else:
                # Inform the user if no customers are found with the entered Last Name
                print("\nNo customers found with Last Name '{}'.".format(update_last_name))

    # User input to show all customers details
    elif choice == '5':
        # Calls function to check if customers list is empty
        if is_customers_empty():
            print("No customers to show. Please add a new customer and try again.")
        else:
            # Show all customers details
            print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
        # Iterate through each customer and display their details
        for idx, customer in enumerate(customers, 1):
            print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(idx, customer["Last_name"], 
            customer["First_name"], customer["Birth_date"], customer["Address"], customer["Id_number"], customer["E_mail"], 
            customer["Phone_number"]
        ))
            
    # User input to sort customers (ascending)
    elif choice == '6':
        # Calls function to check if customers list is empty
        if is_customers_empty():
            print("No customers to show. Please add a new customer and try again.")
        else:
            # Sort customers details based on Last_Name (ascending)
            sort_ascending(customers)
            # Print success message after sorting
            print("\nCustomers sorted successfully based on Last_Name (ascending).")
            # Print header for the sorted customer details
            print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
            # Iterate through sorted customers and print their details
            for idx, customer in enumerate(customers, 1):
                print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                    idx, customer["Last_name"], customer["First_name"], customer["Birth_date"],
                    customer["Address"], customer["Id_number"], customer["E_mail"], customer["Phone_number"]
            ))

    # User input to sort customers (descending)
    elif choice == '7':
                # Calls function to check if customers list is empty
        if is_customers_empty():
            print("No customers to show. Please add a new customer and try again.")
        else:
            # Sort customers details based on Last_Name (descending)
            sort_descending(customers)
            # Print success message after sorting
            print("\nCustomers sorted successfully based on Last_Name (descending).")
            # Print header for the sorted customer details
            print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
            # Iterate through sorted customers and print their details
            for idx, customer in enumerate(customers, 1):
                print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                    idx, customer["Last_name"], customer["First_name"], customer["Birth_date"],
                    customer["Address"], customer["Id_number"], customer["E_mail"], customer["Phone_number"]
            ))

    # User input to exit the program
    elif choice == '0':
        # Quit
        print("Program Exited\n")
        # Exit the loop to end the program
        break

    else:
        print("Invalid choice. Please enter a number between 0 and 7.")
