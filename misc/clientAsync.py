import music
import data
import time
import socket

player = music.Player()

# Start conncection ==================================================
SERVER = "127.0.0.1"
PORT = 8080
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((SERVER, PORT))
print("Connection successful")
# Connected ==========================================================

receivedData = data.receiveData(conn)
serverTimeElapsed = receivedData[0]
print("Time elapsed :" , serverTimeElapsed)

# Start music
player.play()
# Sync music
player.seekInitialize(serverTimeElapsed)


# time.sleep(0.001)
while not(player.ended):
	# print("Loop")

	data.sendData(player.currentPos(), conn)

	receivedData = data.receiveData(conn)
	# print(receivedData[0], data.timeElapsed(timeRef))

	time.sleep(1)

conn.close()