import sqlite3
from datetime import datetime

connection = sqlite3.connect('database/forum.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS problems ('
            'problem_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'title TEXT,'
            'message TEXT,'
            'added_date DATETIME);')

sql.execute('CREATE TABLE IF NOT EXISTS answers ('
            'pr_id INTEGER,'
            'answer_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'answer_message TEXT,'
            'answer_date DATETIME);')

sql.execute('CREATE TABLE IF NOT EXISTS users ('
            'user_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'password TEXT,'
            'reg_date DATETIME);')


def add_problem_db(title, message):
    connection = sqlite3.connect('database/forum.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO problems (title, message, added_date) VALUES (?, ?, ?);', (title, message, datetime.now()))
    connection.commit()


def get_all_problems_db():
    connection = sqlite3.connect('database/forum.db')
    sql = connection.cursor()
    all_problems = sql.execute('SELECT * FROM problems ORDER BY added_date DESC;').fetchall()
    return all_problems


def add_answer_to_problem_db(problem_id, answer_message):
    connection = sqlite3.connect('database/forum.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO answers (pr_id, answer_message, answer_date) VALUES (?, ?, ?);', (problem_id, answer_message, datetime.now()))
    connection.commit()


def register_user(name, password):
    connection = sqlite3.connect('database/forum.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO users (name, password, reg_date) VALUES (?, ?, ?);', (name, password, datetime.now()))
    connection.commit()


def check_password(name, password):
    connection = sqlite3.connect('database/forum.db')
    sql = connection.cursor()
    user = sql.execute('SELECT * FROM users WHERE name=? AND password=?;', (name, password))
    return user.fetchone()
