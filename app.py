import socket, time
import controller, connection, player

# IP = socket.gethostbyname(socket.gethostname())
# PORT = 12344
IP = "127.0.0.1"
PORT = 8080

class App(player.Player):
    def __init__(self):
        player.Player.__init__(self)
        self.player = player.Player()
        self.choice = 'N'

    def hostOrJoin(self):
        while ((self.choice!='J') or (self.choice!='H')):
            value = input("Host or Join?\n").upper()
            if(value == 'J'):
                self.conn = connection.Client((IP, PORT)).connectServer()
                if(self.conn):
                    self.choice = value
                    break
            elif(value == 'H'):
                self.conn = connection.Server((IP, PORT)).startServer()
                self.choice = value
                break
            else:
                print("Enter a valid choice.")
            print(self.choice)
            time.sleep(1/60)

    def play(self):
        controller.Controller(self.conn, player).startPlayer()

    def quit(self):
        self.conn.close()

app = App()
app.hostOrJoin()
app.play()

print('quit')