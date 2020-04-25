import socket
import controller, connection

server = connection.Server()
conn = server.startServer()

app = controller.Controller(conn)
app.startPlayer()


conn.close()
print('quit')