import sqlite3

def save_data(target, ip, status):
    conn = sqlite3.connect('database/mrti.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS results (target TEXT, ip TEXT, status TEXT)')
    c.execute('INSERT INTO results VALUES (?, ?, ?)', (target, ip, status))
    conn.commit()
    conn.close()
