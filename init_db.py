import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#user
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

#course
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
)
""")

#result
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_username TEXT NOT NULL,
    course_name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and users table created successfully.")
