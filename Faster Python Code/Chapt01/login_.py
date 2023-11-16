import string
import sqlite3
from hashlib import sha256
from random import shuffle, choice

salt = '$6$ZmBkxkRFj03LQOvr'

conn = sqlite3.connect('passwords.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

salt256 = salt.encode('utf-8')

def geneate_salt():
	letters = list(string.ascii_letters + "#$%&")
	[shuffle(letters) for _ in range(30)]
	return ''.join([choice(letters) for _ in 
			 range(50)])

def dictfetchall(cursor):
	cols = [col[0] for col in cursor.description]
	return [
		dict(zip(cols, row)) for row in cursor.fetchall()
	]

# query = """CREATE TABLE users (
# 	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
# 	username VARCHAR(100) UNIQUE,
# 	salt VARCHAR(100) UNIQUE
# );"""
# # query = "DROP TABLE IF EXISTS users;"
# cursor.execute(query)
# conn.commit()

# query = """CREATE TABLE passwords (
# 	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
# 	encryption_token VARCHAR(100) UNIQUE
# );"""
# # query = "DROP TABLE IF EXISTS passwords;"
# cursor.execute(query)
# conn.commit()



users = [
	(1, 'januario95', 'Jaci1995', geneate_salt()),
	(2, 'angelina', 'HerPass1234', geneate_salt()),
	(3, 'reinata', 'OnlyForHer', geneate_salt())
]
# for user in users:
# 	password_ = user[2]
# 	# print(password_)
# 	salt = user[3]
# 	salt256 = salt.encode('utf-8')
# 	print(salt256)
# 	encrypted = sha256(password_.encode('utf-8') + salt256).hexdigest()
# 	print(encrypted)

# 	query = """INSERT INTO users VALUES (?, ?, ?)"""
# 	parameters = (user[0], user[1], salt256)
# 	cursor.execute(query, parameters)

# 	query = """INSERT INTO passwords VALUES (?, ?)"""
# 	parameters = (user[0], encrypted)
# 	cursor.execute(query, parameters)

# conn.commit()


def user_passwd(username):
	query = """SELECT password FROM users
		WHERE username = ?"""
	parameter = (username,)
	cursor.execute(query, parameter)
	results = dictfetchall(cursor)
	if results:
		return results[0]['password']
	raise KeyError(username)


def get_username(username):
	query = """SELECT id FROM users
		WHERE username = ?"""
	parameter = (username,)
	cursor.execute(query, parameter)
	results = dictfetchall(cursor)

	if results:
		user_id = results[0]['id']
		query = """SELECT encryption_token FROM passwords
		WHERE id = ?"""
		parameter = (user_id,)
		cursor.execute(query, parameter)
		results = dictfetchall(cursor)
		encryption_token = results[0]['encryption_token']
		print(encryption_token)
	# else:
	# 	raise KeyError(username)

# get_username('januario95')


# username = 'januario95'
# query = """SELECT * FROM users
# 	WHERE username = ?"""
# parameter = (username,)
# cursor.execute(query, parameter)
# results = dictfetchall(cursor)
# print(results)

# query = """SELECT * FROM passwords"""
# cursor.execute(query)
# results = dictfetchall(cursor)
# print(results)






















