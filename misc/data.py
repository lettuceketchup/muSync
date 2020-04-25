import time
import socket
import threading
import sys




class Data():
	def __init__(self, conn):
		self.cmd = ''
		self.conn = conn
		self.sendOn = True
		self.recvOn = False

	def sendData(self, cmd, timeElapsed=0):
		outTime = str(timeElapsed)
		self.cmd = cmd[0]
		out_data = self.cmd + outTime
		print(out_data)
		self.conn.sendall(bytes(out_data,'UTF-8'))
		time.sleep(1/60)

	def receiveData(self):
		self.recvOn = True
		while True:
			in_data = self.conn.recv(1024).decode()
			self.cmd = str(in_data[0])
			self.timeElapsed = float(in_data[1:])

			if (self.cmd == 'q'):
				self.recvOn = False
				return
			print(self.cmd, self.timeElapsed)
	
	def startRecv(self):
		self.thread = threading.Thread(target=self.receiveData)
		self.thread.start()

	def stopRecv(self):
		self.thread.join()
		self.sendOn = False
		print('thread joined')

	def endConn(self):	
		self.stopRecv()	
		self.on = False
		print("===========Should end===========")




LOCALHOST = "127.0.0.1"
PORT = 8080
class Server():
	def __init__(self, host=LOCALHOST, port=PORT):
		self.host = host
		self.port = port

	def startServer(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((self.host, self.port))
		self.server.listen(1)
		print("Server started")
		print("Waiting for client request..")
		clientConnection,clientAddress = self.server.accept()
		print("Connected client :" , clientAddress)
		return clientConnection

SERVER = "127.0.0.1"
PORT = 8080
class Client():
	def __init__(self, server=SERVER, port=PORT):
		self.server = server
		self.port = port
	
	def connectServer(self):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((self.server, self.port))
		print("Connection successful")
		return conn