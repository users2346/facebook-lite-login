import sqlite3

# Connect (or create if it doesn't exist)
conn = sqlite3.connect('logins.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Save and close
conn.commit()
conn.close()

print("✅ Database and table created!")