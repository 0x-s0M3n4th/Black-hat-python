import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
	print(f"[*] Creating the socket....")
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print(f"[*] The server starts listeneing.....")
	server.bind((IP,PORT)) # binding to the port and address
	server.listen(5)
	print(f'[*] Listening on {IP}:{PORT}')
	while True:
		client, address = server.accept()
		print(f'[*] Accepted conection from {address[0]}:{address[1]}')
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()
def handle_client(client_socket):
	with client_socket as sock:
		request = sock.recv(1024)
		print(f'[*] Recieved: {request.decode("utf-8")}')
		message = "Yes I am here brother!"
		print(f"[*] Sending reply: {message}")
		sock.send(message.encode("utf-8"))

if __name__ == '__main__':
	main()


