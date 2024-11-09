import sqlite3

def create_connection():
    conn = sqlite3.connect('expenses.db')
    return conn

def create_expenses_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        paymentmethod TEXT NOT NULL,
        paymentsrc TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_expenses_table()
