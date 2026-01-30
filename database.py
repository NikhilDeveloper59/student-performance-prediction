import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_hours REAL,
            attendance REAL,
            previous_score REAL,
            assignments REAL,
            sleep_hours REAL,
            predicted_score REAL,
            result TEXT,
            grade TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_record(data):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO records 
        (study_hours, attendance, previous_score, assignments, sleep_hours, predicted_score, result, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
