import time
import socket

class Data():
	def __init__(self, conn):
		self.cmd = ''
		self.conn = conn
		self.sendOn = True
		self.recvOn = False

	def sendData(self, cmd = ' ' , timeElapsed=0):
		outTime = str(timeElapsed)
		self.cmd = cmd[0]
		out_data = self.cmd + outTime
		print(out_data)
		self.conn.sendall(bytes(out_data,'UTF-8'))

	def receiveData(self):
		self.recvOn = True
		while True:
			in_data = self.conn.recv(1024).decode()
			if(not in_data):
				continue
			self.cmd = str(in_data[0])
			self.timeElapsed = float(in_data[1:])

			if (self.cmd == 'q'):
				self.recvOn = False
				return
			print(self.cmd, self.timeElapsed)


LOCALHOST = "127.0.0.1"
PORT = 8080
class Server():
	def __init__(self, address=(LOCALHOST, PORT)):
		self.address = address

	def startServer(self):
		print(self.address)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(self.address)
		self.server.listen(1)
		print("Server started")
		print("Waiting for client request..")
		clientConnection,clientAddress = self.server.accept()
		print("Connected client :" , clientAddress)
		return clientConnection

SERVER = "127.0.0.1"
PORT = 8080
class Client():
	def __init__(self, address=(SERVER, PORT)):
		self.address = address
	
	def connectServer(self):
		print(self.address)
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			conn.connect(self.address)
			print("Connection successful")
			return conn
		except:
			print("Cannot find a server. Try again or start a server.")
			return None

class Connect():
	pass