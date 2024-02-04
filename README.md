<h1 align = "center"> Customer Identity Book (CIB) </h1>

This Python script implements a virtual Customer Identity Book (CIB) using a console-based menu that determines the action based on the user's choice. The system permits users to perform various operations, add and remove customers, search for customers, update customer details, see all customers' details, and sort customers according to their last names.

Customer data are saved only during the program runtime. Customers are not saved externally once the termination has been completed.

## Code Structure

The structure of the CIB code consists of several main parts:

**Functions:**
- ‘display_menu()’ - function to display the menu.
```
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
```
- ‘is_customers_empty()’ - checks if the list of customers is empty, and returns True if the list is empty, False otherwise. This function developed in the second stage.
```
# Function to check if customers list is empty
def is_customers_empty():
    return not customers
```
- ‘sort_ascending()’ and ‘sort_descending()’ - implement the bubble sort algorithm to sort a list of customers based on their ‘Last_name’ attribute in ascending and descending order, respectively. In the first stage, it was planned one sorting function, however, changes applied to provide ascending and descending order sorting in the second stage. Although it is not the most efficient sorting algorithm for large datasets, however, it is understandable and easy to implement (Lopez, 2022).
```
# Function to sort customers in ascending order based on Last_name
def sort_ascending(customers):
    # Get the number of customers in the list
    n = len(customers)
    # Outer loop: Iterate through all elements in the list
    for i in range(n - 1):
        # Inner loop: Iterate through the unsorted part of the list
        for j in range(0, n - i - 1):
            # Compare Last_Name for adjacent customers and swap if 
            necessary
            if customers[j]["Last_name"] > customers[j + 
            1]["Last_name"]:
                # Swap the positions of the customers
                customers[j], customers[j + 1] = customers[j + 1], 
                customers[j]
```
```
# Function to sort customers in descending order based on Last_name
def sort_descending(customers):
    # Get the number of customers in the list
    n = len(customers)
    # Outer loop: Iterate through all elements in the list
    for i in range(n - 1):
        # Inner loop: Iterate through the unsorted part of the list
        for j in range(0, n - i - 1):
            # Compare Last_Name for adjacent customers and swap if 
            necessary
            if customers[j]["Last_name"] < customers[j + 
            1]["Last_name"]:
                # Swap the positions of the customers
                customers[j], customers[j + 1] = customers[j + 1], 
                customers[j]
```
-	‘validate_email()’ - function to validate an email input.
```
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
```
-	 ‘validate_phone_number()’ - function to validate a phone number input.
```
# Function to validate phone number
def validate_phone_number(phone_number):
    # Check if the phone number is composed only of digits and has a length of 9
    return phone_number.isdigit() and len(phone_number) == 9
```
-	 ‘validate_birth_date()’ - function to validate a birth date input.
```
# Function to validate birth date
def validate_birth_date(birth_date):
    # Check if the birth date is composed only of digits and has a length of 8
    return birth_date.isdigit() and len(birth_date) == 8
```
-	 ‘validate_id_number ()’ - function to validate an ID number input.
```
# Function to validate ID number
def validate_id_number(id_number):
    # Check if the ID number is composed only of digits and has a length 
    of 6
    return id_number.isdigit() and len(id_number) == 6
```

 <br>
 
**Customer Object:**
- Customer Object Definition: a dictionary named ‘Customer‘ is defined with properties such as Last_name, First_name, Birth_date, Address, Id_number, E_mail, and Phone_number.
```
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
```
- Initialization: an empty list named ‘customers‘ is created to store customer objects.
```
# Initialize an empty list to store customer objects
customers = []
```
 <br>
 
**Data Collection:**
- Data Collection: a loop is used to gather customer information from user input. It iterates a number of times specified by the variable ‘num’, according to the assignment’s requirements. 
```
    # Prompt user for customer information
    customer["Last_name"] = input("Last Name: ")
    customer["First_name"] = input("First Name: ")
    customer["Birth_date"] = int(input("Birth Date: "))
    customer["Address"] = input("Address: ")
    customer["Id_number"] = int(input("ID Number: "))
    customer["E_mail"] = input("E-mail: ")
    customer["Phone_number"] = int(input("Phone Number: "))
    # Append the customer object to the list
    customers.append(customer)
```
- Display Collected Data: after data collection, the program displays a header for the collected data and then prints each customer's details in tabular format using a loop. 
```
# Show collected customers details
# Display header for the collected data
print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone Number\n")
# Loop to print customer details
for idx, customer in enumerate(customers, 1):
    print("{}\t\t{} {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
        idx, customer["Last_name"], customer["First_name"], 
        customer["Birth_date"], customer["Address"], 
        customer["Id_number"], customer["E_mail"], 
        customer["Phone_number"]
    ))
```
- Main Loop: the main loop for the code execution, where the user interacts with the menu and performs operations (details are provided in the section – Application Features).

 <br>
<br>

## Application Features

The function begins with a while True loop that prompts a user’s choice of action based on selection statements. After every iteration, the user is presented with a menu to select an option. Depending on the user's choice, a program performs various operations.

## • Data Collection:

-	

## Features

- Add new customers to the virtual CIB.
- Remove existing customers from the virtual CIB.
- Search for customers based on different criteria.
- Update customer details such as name, contact information, etc.
- View all customers' details in the virtual CIB.
- Sort customers according to their last names.

## Usage

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/customer-identity-book.git

