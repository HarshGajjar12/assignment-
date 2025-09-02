import sqlite3

# Practical Example 21
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT)")
print("Table created.")

# Practical Example 22
cursor.execute("INSERT INTO student (name) VALUES ('Vishal')")
conn.commit()
cursor.execute("SELECT * FROM student")
print(cursor.fetchall())
conn.close()
