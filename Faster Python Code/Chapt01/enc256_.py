from login_ import salt

from random import shuffle, choice
from hashlib import sha256

salt256 = salt.encode('utf-8')

import string

def geneate_salt():
	letters = list(string.ascii_letters + "#$%&")
	[shuffle(letters) for _ in range(30)]
	return ''.join([choice(letters) for _ in 
			 range(30)])



def encrypt_passwd2(passwd):
	return sha256(passwd.encode('utf-8') + salt256).hexdigest()

# print(len(salt))
salt = geneate_salt()
# print(salt)
# print(salt)
# print(encrypt_passwd2('Jaci1995'))


salt256 = salt.encode('utf-8')
encrypted = sha256('Jaci1995'.encode('utf-8') + 
				   salt256, usedforsecurity=True).hexdigest()
# print(encrypted)

# decrypted = sha256('Jaci1995'.)

print(help(sha256))


























