import socket
import controller, connection

client = connection.Client()
conn = client.connectServer()

app = controller.Controller(conn)
app.startPlayer()


conn.close()
print('quit')