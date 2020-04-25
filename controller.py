import player, connection
import threading, time

class Controller(connection.Data):
    def __init__(self, conn, player):
        # player.Player.__init__(self)
        connection.Data.__init__(self, conn)
        self.data = connection.Data(conn)
        self.p = player

    def check(self):
        time.sleep(2)
        if(self.value != ''):
            return
        print(' ')

    def startRecv(self):
        self.threadRecv = threading.Thread(target=self.data.receiveData)
        self.threadRecv.start()

    def stopRecv(self):
        self.threadRecv.join()
        self.sendOn = False

    def startTakingCommands(self):
        self.threadCmd = threading.Thread(target=self.playerCommands)
        self.threadCmd.start()

    def stopTakingCommands(self):
        self.threadCmd.join()

    def playerCommands(self):
        while (not self.p.status['ended']):
            if((self.data.cmd == 'q') or (not self.data.recvOn)):
                self.data.sendData('q')
                self.p.stop()
                self.p.status['ended'] = True
            elif(self.data.cmd == 'p'):
                if(self.p.status['playing']):
                    self.p.pause()
                    self.data.cmd = ' '
                elif(self.p.status['paused']):
                    self.p.resume()
                    self.data.cmd = ' '
                else:
                    self.p.play()
                    self.data.cmd = ' '
            elif(self.data.cmd == 's'):
                self.p.stop()
                self.data.cmd = ' '
            elif(self.data.cmd == 'i'):
                self.p.seekInitialize(self.p.timeElapsed)
                self.data.cmd = ' '
            elif(self.data.cmd == 'n'):
                self.data.cmd = ' '
                pass
    
    def startPlayer(self):
        self.p = player.Player()
        self.p.play()
        self.startRecv()
        self.startTakingCommands()
        # self.data.sendData('i', self.p.timeElapsed)
        self.timeout = 1

        while self.data.sendOn:
            self.value = ''
            threading.Thread(target = self.check).start()
            self.value = input()

            if(self.p.status['ended']):
                break
            if(self.value == ''):
                continue
            
            self.data.sendData(self.value)
            print(self.p.status)
        self.stopTakingCommands()
        self.stopRecv()