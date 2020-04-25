import socket
import time
import threading

LOCALHOST = "127.0.0.1"
PORT = 8080


class Data():
    def __init__(self, conn):
        self.cmd = ''
        self.conn = conn
        self.sendOn = True
        self.recvOn = False

    def sendData(self, cmd=' ', timeElapsed=0):
        outTime = str(timeElapsed)
        self.cmd = cmd[0]
        out_data = self.cmd + outTime
        print(out_data)
        self.conn.sendall(bytes(out_data, 'UTF-8'))

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

    # def check(self):
    #     time.sleep(2)
    #     if(self.value != ''):
    #         return
    #     print(' ')

    def startRecv(self):
        self.threadRecv = threading.Thread(target=self.receiveData)
        self.threadRecv.start()

    def stopRecv(self):
        self.threadRecv.join()
        self.sendOn = False



class Server():
    def __init__(self, address=(LOCALHOST, PORT)):
        self.address = address
        self.connected = False
        self.clientConns = []
        self.clientAddrs = []
        self.clientThreads = []

    def startServer(self):
        print(self.address)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(5)
        print("Server started")
        print("Waiting for client request..")
        while True:
            try:
                client = self.server.accept() # clientConnection,clientAddress = client
                if(any(client[1] in self.clientAddrs)):
                    print("Connected client :", client[1])

                else:
                    self.clientConns.append(client[0])
                    self.clientAddrs.append(client[1])
            except Exception as e:
                print(e)
        print("Closing")


SERVER = "127.0.0.1"
PORT = 8080
class Client():
    def __init__(self, address=(SERVER, PORT)):
        self.address = address
        self.connected = False

    def connectServer(self):
        print(self.address)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = self.address[0].split('.')
        addr = addr[0] + '.' + addr[1] + '.' + addr[2] + '.'
        for ping in range(1, 10):
            try:
                address = addr + str(ping)
                conn.connect((address, self.address[1]))
                print("Connection successful")
                self.connected = True
                return conn
            except:
                print("Cannot find a server. Try again or start a server.")
                return None


# IP = socket.gethostbyname(socket.gethostname())
# PORT = 12344
IP = "127.0.0.1"
PORT = 8080


class Connect(Server, Client):
    def __init__(self):
        self.choice = 'N'
        Server.__init__(self)
        Client.__init__(self)

    def hostOrJoin(self):
        while ((self.choice != 'J') or (self.choice != 'H')):
            value = input("Host or Join?\n").upper()
            if(value == 'J'):
                Client((IP, PORT)).connectServer()
                if(self.conn):
                    self.choice = value
                    break
            elif(value == 'H'):
                Server((IP, PORT)).startServer()
                self.choice = value
                break
            else:
                print("Enter a valid choice.")
            print(self.choice)
            time.sleep(1/60)
    pass
