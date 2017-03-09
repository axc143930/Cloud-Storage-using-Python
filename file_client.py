import socket
import sys
import threading
import random


class chatApp:
	def __init__(self):	
		self.host = socket.gethostname() # localhost replaced by IP address of host in case of remote system
		self.port = 12429 #port
		self.s = socket.socket() #create socket
		self.s.connect((self.host,self.port)) # connect to server
    print "connecting from",self.host,self.port 

	def run(self): # run method
		while True:
			flag = 0 # flag which is set when file is not found
			print "Upload or Download?" # choice to upload or download file
			k1 = raw_input()
			print "Name of the file?" # name of file to upload or download
			k2 = raw_input()
			print "Username" # username or name of the client
			k3 = raw_input()
			send_name = k1+","+k2+","+k3
			self.s.send(send_name) # details of file,client and upload/download sent to server
			if send_name == "close,close,close": # end process and close socket if all three inputs say "close"
				self.s.close()
				break
			elif send_name.split(",")[0] == "download": 
				file = open("copy_"+send_name.split(",")[1],"w") # create a file into which the downloaded data is copied
				while True: #continuously receive data
					k = self.s.recv(1024) # receive 1024 bytes each iteration of the loop
					if k == "file not found": # if file is not found on server, server sends file not found
						flag = 1 # set flag
						break
					elif k == "done": # server sends a done signal to notify that file to be sent has been finished 
						flag = 0
						break
					else:
						file.write(k) # write received data to file in each iteration
						continue
				if flag == 0:
					print "received",send_name
				else:
					print "file not found"
				continue
			elif send_name.split(",")[0] == "upload":
				file = open(send_name.split(",")[1],"r") # send the name of file to be uploaded to server
				ack = self.s.recv(1) # server sends acknowledgement after receiving the file name
				if ack == "1": # start sending data when acknowledgement is received
					self.s.send(file.read()) # send data in file to server
					self.s.send("done") # send done signal to notify server that file data to be send has been finished
					print "sent ", send_name
				else:
					continue
			else:
				print "Invalid command"
				


c = chatApp()
print "connected"
c.run()
