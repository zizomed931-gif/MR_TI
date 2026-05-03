import sqlite3

def save_result(data):
    conn = sqlite3.connect('database/mrti_results.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS scans (target TEXT, ip TEXT, vulns TEXT)')
    cursor.execute('INSERT INTO scans VALUES (?, ?, ?)', (data['target'], data['ip'], data['vulns']))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect('database/mrti_results.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scans')
    rows = cursor.fetchall()
    conn.close()
    return rows
