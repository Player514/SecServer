import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
DontClose = True
bobSecret = 523
B = 0
while DontClose:
	conn, addr = serv.accept()
	from_client = ''
	while True:

		data = conn.recv(4096)
		if not data: break
		from_client = data.decode()
		data = from_client.split()
		sharedPrime = int(data[0])
		sharedBase = int(data[1])
		AliceShare = int(data[2])
		B = (sharedBase ** bobSecret) % sharedPrime

		conn.send(str(B).encode())
		
		SharedSecret = (AliceShare**bobSecret) % sharedPrime
		print(SharedSecret)
		
		data = conn.recv(4096)
		if not data: break
		from_client = data.decode()
		print(from_client)

		conn.send("I am SERVER\n".encode())

		data = conn.recv(4096)
		from_client = data.decode()
		print(from_client)

		conn.send("I am SERVER\n".encode())


	conn.close()
	print('client disconnected')
	DontClose = False
