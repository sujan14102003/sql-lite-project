import sqlite3

# Function to create a new contact
def create_contact(conn, name, cell, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, cell, email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    print(f"Contact {name} added successfully.")

# Function to display all contacts
def display_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Cell#: {contact[2]}, E-mail: {contact[3]}")

# Connect to the SQLite database (or create if not exists)
conn = sqlite3.connect('contacts.db')

# Create a table to store contacts if not exists
conn.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cell TEXT NOT NULL,
        email TEXT
    )
''')

# Insert 5 rows of data
contacts_data = [
    ("Sujan", "1928374650", "Sujan@gmail.com"),
    ("Vignesh", "9807654321", "vignesh@gmail.com"),
    ("Shakti", "6574839201", "shakti@gmail.com"),
    ("Shetty", "7890654321", "shettyl@gmail.com"),
    ("Patil", "6543217890", "patil@gmail.com")
]

for contact_data in contacts_data:
    create_contact(conn, *contact_data)

# Display all contacts
display_contacts(conn)

# Close the database connection
conn.close()