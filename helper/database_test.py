"""database test
with this py file you can create a new sqlite database
in the used format and test the database connection.
"""
import sqlite3

# Connect to the database
conn = sqlite3.connect("database.sqlite")

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("CREATE TABLE patients (id INTEGER PRIMARY KEY, vname TEXT, nname Text, email TEXT)")

# Insert some data
c.execute("INSERT INTO patients VALUES (1, 'John', 'Doe', 'john.doe@example.com')")
c.execute("INSERT INTO patients VALUES (2, 'Jane', 'Doe', 'jane.doe@example.com')")
c.execute("INSERT INTO patients VALUES (3, 'John', 'wrap', 'john.doe@example.com')")
c.execute("INSERT INTO patients VALUES (4, 'mc', 'key', 'jane.doe@example.com')")
c.execute("INSERT INTO patients VALUES (11, 'ronald', 'regon', 'rr@example.com')")

# commit the changes
conn.commit()

# test
print(c.lastrowid)

# close the connection
conn.close()