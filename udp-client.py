import socket
target_host = "127.0.0.1"
target_port = 9997

#socket object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending some data
client.sendto("hello".encode(),(target_host,target_port))
#receiving data and address
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()