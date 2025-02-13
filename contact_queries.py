import sqlite3

''' Checks if the database exists and creates a new one if not '''
def connect_db():
    try:
        contact_list = sqlite3.connect('contact_list.db')  # Open connection
        cursor = contact_list.cursor()
        
        cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='contact_information' ''')

        # If table does not exist, create it
        if cursor.fetchone() is None:
            cursor.execute('''
                CREATE TABLE contact_information(
                    name TEXT NOT NULL,
                    phone_number INTEGER NOT NULL,
                    email_address TEXT PRIMARY KEY NOT NULL
                )
            ''')
            contact_list.commit()  # Commit changes

    except sqlite3.Error as err:
        print(f'Database Connection Error: {err}')
        return None
    
    return contact_list  # Return the connection object

''' Veiwing the Contact List '''
def view_contact_list(cursor: sqlite3.Cursor):
    """Fetches and displays all contacts from the contact_information table."""

    query = 'SELECT * FROM contact_information'
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("No contacts found.")
        return

    # Fetch column names from cursor.description
    column_names = [description[0] for description in cursor.description]

    # Convert each row to a dictionary and print it
    for row in rows:
        contact_dict = dict(zip(column_names, row))  # Zip column names with row values
        print(contact_dict)

    
''' Updating a contact '''
def edit_contact(cursor: sqlite3.Cursor, email: str, value_to_change: str, new_value):
    '''
    Updates a specific column in the contact_information table for a given email.

    Args:
        cursor (sqlite3.Cursor): The database cursor to execute SQL queries.
        email (str): The email address (primary key) identifying the record.
        value_to_change (str): The column to be updated.
        new_value: The new value to be set in the specified column.
    '''

    query = f'UPDATE contact_information SET {value_to_change} = ? WHERE email_address = ?'
    cursor.execute(query, (new_value, email))

    
def delete_contact(cursor: sqlite3.Cursor, email):
    query = 'DELETE FROM contact_information WHERE email_address = ?'
    cursor.execute(query, (email,))

def add_new_contact(cursor: sqlite3.Cursor, name, phone_number, email):
    query = "INSERT INTO contact_information VALUES (?, ?, ?)"
    cursor.execute(query, (name, phone_number, email))
    

    

        