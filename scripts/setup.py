import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('./database/budget_db.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY AUTOINCREMENT, amount FLOAT)')
    print("Budget table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, color TEXT, max_amount FLOAT)')
    print("Categories table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date date, amount FLOAT, category TEXT, description TEXT)')
    print("Expenses table created successfully")

    categories_data =  [
            ("Lebensmittel", "#3B82F6", 0.00),
            ("Transport", "#8B5CF6", 0.00),
            ("Wohnen", "#10B981", 0.00),
            ("Gesundheit", "#EF4444", 0.00),
            ("Shopping", "#EC4899", 0.00),
            ("Reisen", "#06B6D4", 0.00),
            ("Unterhaltung", "#F97316", 0.00),
            ("Sonstiges", "#CACFD7", 0.00),
        ]
    # cursor to manipulate database
    cursor = conn.cursor()
    # Prepared statement with placeholders
    insert_query = "INSERT INTO categories (name, color, max_amount) VALUES (?, ?, ?)"
    # Execute multiple inserts safely
    cursor.executemany(insert_query, categories_data)

    # Commit changes
    conn.commit()