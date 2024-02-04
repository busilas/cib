# Customer Identity Book (CIB)

This Python script implements a virtual Customer Identity Book (CIB) using a console-based menu that determines the action based on the user's choice. The system permits users to perform various operations, add and remove customers, search for customers, update customer details, see all customers' details, and sort customers according to their last names.

Customer data are saved only during the program runtime. Customers are not saved externally once the termination has been completed.

# Code Structure

The structure of the CIB code consists of several main parts:

 ## • Functions: 
 
 -	‘display_menu()’ - function to display the menu.

```bash
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



![image](https://github.com/busilas/cib/assets/24510366/b991d6b9-1fd1-4564-9df4-58afb8b8ff3c)

-	‘is_customers_empty()’ - checks if the list of customers is empty, and returns True if the list is empty, False otherwise. This function developed in the second stage.
  
![image](https://github.com/busilas/cib/assets/24510366/db560ffd-dac9-4956-a6c1-f89796483f2d)

-	‘sort_ascending()’ and ‘sort_descending()’ - implement the bubble sort algorithm to sort a list of customers based on their ‘Last_name’ attribute in ascending and descending order, respectively. In the first stage, it was planned one sorting function, however, changes applied to provide ascending and descending order sorting in the second stage. Although it is not the most efficient sorting algorithm for large datasets, however, it is understandable and easy to implement (Lopez, 2022).
  
![image](https://github.com/busilas/cib/assets/24510366/ee07e50e-d1f0-4fa8-a6b3-db8d0e7a387e)
![image](https://github.com/busilas/cib/assets/24510366/26a9d633-a383-4366-b1f1-d907b50d6bc6)

-	‘validate_email()’ - function to validate an email input.
  
![image](https://github.com/busilas/cib/assets/24510366/1af0cce0-6a1b-4501-add4-ada080b1851c)
![image](https://github.com/busilas/cib/assets/24510366/bf9fa36a-015e-4fc2-8960-0eb71cff82f4)

-	‘validate_phone_number()’ - function to validate a phone number input.
  
![image](https://github.com/busilas/cib/assets/24510366/a8b08ae4-22fd-46a7-bba8-7481df116e75)

-	‘validate_birth_date()’ - function to validate a birth date input.
  
![image](https://github.com/busilas/cib/assets/24510366/e913bfbb-d043-4832-9631-4a7ee73e6cec)

-	‘validate_id_number ()’ - function to validate an ID number input.
  
![image](https://github.com/busilas/cib/assets/24510366/7ae3f1d8-fc86-4167-8ef7-c7318efedbf0)

## • Customer Object:

-	Customer Object Definition: a dictionary named ‘Customer‘ is defined with properties such as Last_name, First_name, Birth_date, Address, Id_number, E_mail, and Phone_number.
  
![image](https://github.com/busilas/cib/assets/24510366/c33d558c-51e5-4ce2-8d57-6333e98684d0)

-	Initialization: an empty list named ‘customers‘ is created to store customer objects.
  
![image](https://github.com/busilas/cib/assets/24510366/e6b9f67b-4ee8-4bc6-a744-84618b7ba181)

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

