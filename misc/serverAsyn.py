import music
import data
import time
import socket

player = music.Player()
# ==============================================================================
# Start music
player.play()

# Start connection ===================================================
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")
clientConnection,clientAddress = server.accept()
print("Connected client :" , clientAddress)
# Connected ==========================================================

while not(player.ended):
	# print(player)

	data.sendData(player.currentPos(), clientConnection)

	receivedData = data.receiveData(clientConnection)
	# player.end()
	time.sleep(1)

# print(data.sendData(player.currentPos(), clientConnection))
player.stop()
print("Client disconnected....")
clientConnection.close()