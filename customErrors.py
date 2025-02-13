''' This Module contains all the errors for the program '''


class ColumnDoesNotExistError(Exception):
    pass

def check_column_exists():

    while True:
        value_to_change = input('Enter the column you wish to access: ').lower()
        columns = ['name', 'cell number', 'email address']
        if value_to_change not in columns:
            raise ColumnDoesNotExistError('The column does not exist')
        else:
            return value_to_change
    
class EmailDoesNotExistError(Exception):
    pass 
    
def check_email_in_db(cursor, email):
    cursor.execute('SELECT email_address FROM contact_information')
    email_addresses = cursor.fetchall()
    emails_only = [email[0] for email in email_addresses]
    if email in emails_only:
        return True
    else:
        raise EmailDoesNotExistError('The Provided Eamil Does Not Exist')