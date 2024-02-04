<h1 align = "center"> Customer Identity Book (CIB) </h1>

This Python script implements a virtual Customer Identity Book (CIB) using a console-based menu that determines the action based on the user's choice. The system permits users to perform various operations, add and remove customers, search for customers, update customer details, see all customers' details, and sort customers according to their last names.

Customer data are saved only during the program runtime. Customers are not saved externally once the termination has been completed.

## Code Structure

The structure of the CIB code consists of several main parts:

**Functions:**
- **‘display_menu()’** - function to display the menu.
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
- **‘is_customers_empty()’** - checks if the list of customers is empty, and returns **True** if the list is empty, **False** otherwise. This function developed in the second stage.
    ```
    # Function to check if customers list is empty
    def is_customers_empty():
        return not customers
    ```
- **‘sort_ascending()’** and **‘sort_descending()’** - implement the bubble sort algorithm to sort a list of customers based on their **‘Last_name’** attribute in ascending and descending order, respectively. In the first stage, it was planned one sorting function, however, changes applied to provide ascending and descending order sorting in the second stage. Although it is not the most efficient sorting algorithm for large datasets, however, it is understandable and easy to implement (Lopez, 2022).
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
-	**‘validate_email()’** - function to validate an email input.
  
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
-	 **‘validate_phone_number()’** - function to validate a phone number input.
  
        ```
        # Function to validate phone number
        def validate_phone_number(phone_number):
            #Check if the phone number is composed only of digits and has a length of 9
            return phone_number.isdigit() and len(phone_number) == 9
        ```
-	 **‘validate_birth_date()’** - function to validate a birth date input.
  
        ```
        # Function to validate birth date
        def validate_birth_date(birth_date):
            #Check if the birth date is composed only of digits and has a length of 8
            return birth_date.isdigit() and len(birth_date) == 8
        ```
-	 **‘validate_id_number ()’** - function to validate an ID number input.
  
        ```
        # Function to validate ID number
        def validate_id_number(id_number):
            #Check if the ID number is composed only of digits and has a length 
            of 6
            return id_number.isdigit() and len(id_number) == 6
        ```

 <br>
 
**Customer Object:**
- **Customer Object Definition:** a dictionary named ‘Customer‘ is defined with properties such as Last_name, First_name, Birth_date, Address, Id_number, E_mail, and Phone_number.
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
- **Initialization:** an empty list named ‘customers‘ is created to store customer objects.
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

    ```
        while True:  
        # Display the menu
        display_menu()
        # Prompt user for menu choice
        choice = input("\nEnter your choice (0-7): ")
    ```

The main features of the script responsible for overall functioning are as follows:
- **Add New Customers:** the function asks the user to enter the customer’s details (as shown below). After hitting enter, the contact is saved and the confirmation prompt prints.
    ```
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
        customer["Birth_date"] = int(input("Birth Date: "))
        customer["Address"] = input("Address: ")
        customer["Id_number"] = int(input("ID Number: "))
        customer["E_mail"] = input("E-mail: ")
        customer["Phone_number"] = int(input("Phone Number: "))
        # Append the customer details to the list of customers
        customers.append(customer)
        # Display a success message with a check mark symbol
        print("\nCustomer details saved successfully \N{check mark}")
    ```
> All the features below apply the function that first checks whether the customers is empty or not, if True, the user is asked to add a new contact and try again.
- **Remove Customers:** user can remove customers based on their Last_name from the customer list, it deletes the key:value pair of that particular customer from customers.
    ```
        elif choice == '2':
            # Calls function to check if customers list is empty
            if is_customers_empty():
                # Display a message if the customers list is empty
                print("No customers to remove. Please add a new customer and 
                try again.")
            else:
                # Remove Customers
                # Prompt the user to enter the Last Name of the customer to 
                remove
                remove_last_name = input("Enter the Last Name of the customer 
                to remove: ")
                # Create a list of customers with matching Last Names (case-
                insensitive)
                removed_contacts = [customer for customer in customers if 
                customer["Last_name"].lower() == remove_last_name.lower()]
                # Check if there are matching customers to remove
            if removed_contacts:
                # Iterate through the list of matching customers and remove 
                them
                for removed_contact in removed_contacts:
                    customers.remove(removed_contact)
                # Display a success message
                print("Customers with Last Name '{}' removed 
                successfully.".format(remove_last_name))
            else:
                # Display a message if no customers were found with the 
                specified Last Name
                print("No customers found with Last Name 
                '{}'.".format(remove_last_name))
    ```
-	**Search Customers:** user can search customers based on their Last_name from the customer list by iterating through each customer in the list to see if the input is a part of the customer’s last name. If a match is found, it displays the details relevant to the customer such as the full name and ID number. Otherwise, it notifies the user that the name is not found.
    ```
        # User input to search customer by the Last Name
        elif choice == '3':
            # Calls function to check if customers list is empty
            if is_customers_empty():
                # Inform the user if the customers list is empty
                print("No customers to search. Please add a new customer and 
                try again.")
            else:
                # Search Customers
                # Prompt user to enter the customer's Last Name for search
                search_term = input("\nEnter customer Last Name: ")
                # Displaying the search result header
                print("Search result:")
                # Initializes a variable to keep track of whether a match is 
                found during the search
                found = False
                # Iterate through each customer to find a match
                for customer in customers:
                    # Check if the search term is present in either First Name 
                    or Last Name (case-insensitive)
                    if search_term.lower() in customer["Last_name"].lower():
                        # Display relevant details for the found customer
                        print("Name: {} {}, ID Number: 
                        {}".format(customer["First_name"], 
                        customer["Last_name"], customer["Id_number"]))
                        # Indicate that a match has been found
                        found = True
                # Inform the user if no match is found
                if not found:
                    print("Name not found")
    ```
-	**Update Customers Details:** user can update customers based on their **Last_name** from the customer list. The program prints customer details and asks to update information. Otherwise prints error message.
    ```
        # User input to update customer details
        elif choice == '4':
            # Calls function to check if customers list is empty
            if is_customers_empty():
                print("No customers to update. Please add a new customer and  
                try again.")
            else:
                # Update Customer Details
                # Prompt user to enter the Last Name of the customer to update
                update_last_name = input("\nEnter the Last Name of the customer 
                to update: ")            
                # Create a list of customers matching the entered Last Name
                update_customers = [customer for customer in customers if 
                customer["Last_name"].lower() == update_last_name.lower()]
                if update_customers:
                    # Display customer details for the user to choose from
                    for customer in update_customers:
                        print("\nUpdate Customer Details for:\n")
                        # Display header for customer details
                        print("\nID\t\t\tName\t\t\tBirth 
                        date\t\t\tAddress\t\t\tID Number\t\t\tE-mail\t\t\tPhone 
                        Number\n")
                        # Display current customer details
                        print("{}\t\t\t{} 
                        {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                            customers.index(customer) + 1, 
                            customer["Last_name"], customer["First_name"], 
                            customer["Birth_date"], customer["Address"], 
                            customer["Id_number"], customer["E_mail"], 
                            customer["Phone_number"]
                        ))
                        # Prompt user for updated information
                        print("\nPlease enter the following details to update: 
                        ")
                        customer["Last_name"] = input("Last Name: ")
                        customer["First_name"] = input("First Name: ")
                        customer["Birth_date"] = int(input("Birth Date: "))
                        customer["Address"] = input("Address: ")
                        customer["Id_number"] = int(input("ID Number: "))
                        customer["E_mail"] = input("E-mail: ")
                        customer["Phone_number"] = int(input("Phone Number: "))
                        # Display a success message
                        print("\nCustomer details updated successfully.")
                else:
                    # Inform the user if no customers are found with the 
                    entered Last Name
                    print("\nNo customers found with Last Name 
                    '{}'.".format(update_last_name))
    ```
-	**Show All Customers:** user can view and display all saved customers.
    ```
        # User input to show all customers details
        elif choice == '5':
            # Calls function to check if customers list is empty
            if is_customers_empty():
                print("No customers to show. Please add a new customer and try 
                again.")
            else:
                # Show all customers details
                print("\nID\t\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID 
                Number\t\t\tE-mail\t\t\tPhone Number\n")
            # Iterate through each customer and display their details
            for idx, customer in enumerate(customers, 1):
                print("{}\t\t\t{} 
                {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(idx, 
                customer["Last_name"], customer["First_name"], 
                customer["Birth_date"], customer["Address"], 
                customer["Id_number"], customer["E_mail"], 
                customer["Phone_number"]
            ))
    ```
-	**Sort Customers:** user can sort a list of customers in ascending and descending order based on their Last_name, calling functions. Both sorting options provided as a two separate features (No. 6 and 7). 
    ```
        # User input to sort customers (ascending)
        elif choice == '6':
            # Calls function to check if customers list is empty
            if is_customers_empty():
                print("No customers to show. Please add a new customer and try 
                again.")
            else:
                # Sort customers details based on Last_Name (ascending)
                sort_ascending(customers)
                # Print success message after sorting
                print("\nCustomers sorted successfully based on Last_Name 
                (ascending).")
                # Print header for the sorted customer details
                print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID 
                Number\t\t\tE-mail\t\t\tPhone Number\n")
                # Iterate through sorted customers and print their details
                for idx, customer in enumerate(customers, 1):
                    print("{}\t\t{} 
                    {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                        idx, customer["Last_name"], customer["First_name"], 
                        customer["Birth_date"], customer["Address"], 
                        customer["Id_number"], customer["E_mail"], 
                        customer["Phone_number"]
                ))
    ```
    Descending sorting option:
```
    # User input to sort customers (descending)
    elif choice == '7':
                # Calls function to check if customers list is empty
        if is_customers_empty():
            print("No customers to show. Please add a new customer and try 
            again.")
        else:
            # Sort customers details based on Last_Name (descending)
            sort_descending(customers)
            # Print success message after sorting
            print("\nCustomers sorted successfully based on Last_Name 
            (descending).")
            # Print header for the sorted customer details
            print("\nID\t\tName\t\t\tBirth date\t\t\tAddress\t\t\tID 
            Number\t\t\tE-mail\t\t\tPhone Number\n")
            # Iterate through sorted customers and print their details
            for idx, customer in enumerate(customers, 1):
                print("{}\t\t{} 
                {}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(
                    idx, customer["Last_name"], customer["First_name"], 
                    customer["Birth_date"], customer["Address"], 
                    customer["Id_number"], customer["E_mail"],  
                    customer["Phone_number"]
            ))
```
 	
-	**Quit:** The software ends the program's execution by breaking out of the loop and printing a message to the user informing them that the programme has ended.
    ```
        # User input to exit the program
        elif choice == '0':
            # Quit message
            print("Program Exited\n")
            # Exit the loop to end the program
            Break
    ```
<br>
<be>

## Validation
This code validates the accuracy of the data entered by the user. These validations were implemented while collecting and updating customer information to ensure the accuracy of the stored data. If none of the validation conditions are met, users are prompted to re-enter the information. Implementation examples of email, phone number, birth date, and ID number validations are provided in the main loop:
    ```
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
            email = input("Invalid email format. Please enter a valid email 
            address: ")
        customer["E_mail"] = email
        # Validate phone number format using the is_valid_phone_number function
        phone_number = input("Phone Number (9-digit): ")
        while not validate_phone_number(phone_number):
            print("Invalid phone number format. Please enter a valid 9-digit 
            phone number.")
            phone_number = input("Phone Number (9-digit): ")
        customer["Phone_number"] = int(phone_number)
        # Append the customer object to the list
        customers.append(customer)
    ```
<br>
<be>

## Conclusion
The described code illustrates a customer management system with an interface based on menu selection. It allows users to perform various operations, such as adding customers, removing customers, searching for customers, updating customer details, showing all customer details, and sorting customers according to their last name in ascending and descending order. Input validation functions that verify whether the information provided by the user, such as email addresses, phone numbers, birth dates, and ID numbers, meets certain criteria are implemented in the system.

    
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

