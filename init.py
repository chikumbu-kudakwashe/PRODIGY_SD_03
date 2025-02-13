import sqlite3

with sqlite3.connect('contact_list.db') as contact_database:
    cursor = contact_database.cursor()

cursor.execute('''CREATE TABLE contact_information(
               name VARCHAR NOT NULL,
               phone_number INTEGER NOT NULL,
               email_address VARCHAR PRIMARY KEY NOT NULL
               )
''')

contact_database.commit()
