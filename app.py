import socket
import time
import controller
import connection
import player


class App(connection.Connect, player.Player):
    def __init__(self):
        connection.Connect.__init__(self)
        player.Player.__init__(self)
        self.p = player.Player()

    def playStart(self):
        self.p.startPlayer()

    def quit(self):
        self.conn.close()


app = App()
app.hostOrJoin()
app.playStart()

print('quit')
