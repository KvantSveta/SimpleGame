#!/usr/bin/python3.3

__author__ = 'j.d.'

from socket import *

myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(2)

while True:
	connection, address = sockobj.accept()

	print('Server connected by', address)

	while True:
		data = connection.recv(1024)
		if not data:
			break
		print(data)
	connection.close()
	'''
	while True:
		data = connection.recv(1024)
		if not data:
			break
		connection.send(b'Echo => ' + data)
	connection.close()
	'''