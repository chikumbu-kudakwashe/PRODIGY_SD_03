from email_validator import validate_email, EmailNotValidError
from contact_queries import *
from customErrors import *

''' Checks if the email is valid '''
def is_valid_email():
    """
    Asks the user to enter an email address and validates it.
    
    Returns:
        str: A valid email address entered by the user.
    """
    while True:
        email = input('Enter email address: ')
        try:
            validate_email(email, check_deliverability=True)  # Validate email
            return email  # Return if valid
        except EmailNotValidError as err:
            print(f'The email "{email}" is invalid: {str(err)}. Please try again.')

def get_option() -> int:

    options = '''
1. Add New Contact
2. View Contacts
3. Edit Existing Contact
4. Delete Contact
5. Back
6. Exit
'''     
    try:
        user_option = int(input(f'Select an option {options}: '))
        return user_option
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        return get_option()

def main():
    user_option = get_option()
    database = connect_db() #database connection
    cursor = database.cursor() #cursor to execute sql queries

    if user_option == 1:
        while True:  
            """Prompt user for a valid name"""
            name = input('Enter name: ').strip().capitalize()
            if name:
                break
            print("Invalid input. Name cannot be empty.")
        
        while True:  
            """Prompt user for a valid phone number"""
            phone_number = input('Enter phone number (without spaces or special characters): +').strip()
            if phone_number.isdigit() and 7 <= len(phone_number) <= 15:
                break
            print("Invalid phone number. Enter digits only, 7-15 characters.")

        email = is_valid_email()
        #appends the contact to the database
        add_new_contact(cursor, name, phone_number, email)
        database.commit()  # Save changes

        print(f"\nContact {name} added successfully!")
    
    elif user_option == 2:
        view_contact_list(cursor)

    elif user_option == 3:
        value_to_change = check_column_exists()
        email = is_valid_email()
        if value_to_change == 'email address':
            new_value = is_valid_email()
        elif value_to_change == 'phone number':
            while True:  
                """Prompt user for a valid phone number"""
                new_value = input('Enter phone number (without spaces or special characters): +').strip()
                if phone_number.isdigit() and 7 <= len(phone_number) <= 15:
                    break
                print("\nInvalid phone number. Enter digits only, 7-15 characters.")
        else: 
            new_value = input('Enter the name: ')

        edit_contact(cursor, email, value_to_change, new_value)
        database.commit()
        print('\nRecord updated successfully!')

    elif user_option == 4:
        email = is_valid_email()
        delete_contact(cursor, email)
        print('\nContact Deleted Successfully!')

    elif user_option == 5:
        main()

    else:
        exit()           


if __name__ == '__main__':
    main()