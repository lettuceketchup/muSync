import time
import socket
import requests

def rtt(conn):
	t1 = time.time()
	r = requests.get(conn)
	t2 = time.time()

	tim = str(t2-t1) 

	print("Time in seconds :" + tim) 