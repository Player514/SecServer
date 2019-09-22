import socket
import time
import crypto



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

sharedPrime = 6231   # p
sharedBase = 1236      # g
 
aliceSecret = 785     # a
NotTimeout = True
if NotTimeout:
	x = 0
	client.send((str(sharedPrime) +  " " + str(sharedBase) + " " + str((sharedBase**aliceSecret) % sharedPrime)).encode())

	from_server = client.recv(4096)
	data = from_server.decode().split()
	BobShare = int(data[0])
	SharedSecret = (BobShare ** aliceSecret) % sharedPrime
	print(SharedSecret)
	mac = crypto.hmac.new(25) # default is MD5
	client.send("I am CLIENT\n".encode())

	from_server = client.recv(4096)
	print(from_server.decode())
	
	client.send("I am CLIENTdoe\n".encode())

	from_server = client.recv(4096)
	print(from_server.decode())
#	time.sleep(1)
#	if(x > 200000000):
#		NotTimeout = False


client.close()
