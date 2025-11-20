# Basic HTTP server
# Includes CRUD operations for a database

import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
    ''')
    conn.commit()
    conn.close()

def create_user(name, email, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    ''', (name, email, password))
    conn.commit()
    conn.close()

def get_user(email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE email = ?
    ''', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(email, name, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET name = ?, password = ? WHERE email = ?
    ''', (name, password, email))
    conn.commit()
    conn.close()

def delete_user(email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''      
        DELETE FROM users WHERE email = ?
    ''', (email,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users
    ''')
    users = cursor.fetchall()
    conn.close()
    return users