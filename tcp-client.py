import socket
target_host = "127.0.0.1"
target_port = 9998

# socket object
print(f"[*] Creating the socket....")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecting to the server
print(f"[*] Connecting to the server....")
client.connect((target_host,target_port))

#sending some data
# client.send(b"GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")
print(f"[*] Sending data....")
message = "Hello brother!Are you here?"
print(f"[*] Sending message : {message}")
client.send(message.encode('utf-8'))


#recieving some data
print(f"[*] Waiting for the response....")
response = client.recv(4096)
print(f"[*] rCIEVED: {response.decode('utf-8')}")

print(f"[*] cLOSING the connection....")
client.close()