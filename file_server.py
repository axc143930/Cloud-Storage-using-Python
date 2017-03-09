import socket
import sys
import threading
import os

class chatApp:
	def __init__(self,port):
		self.host = socket.gethostname()# name of local host
		self.port = port # port number
		self.s  = socket.socket()
		self.s.bind((self.host,self.port)) # bind the host to the port
                		
	def run(self): #run method
		while True:
      self.s.listen(5) # start listening for any client request
      self.c,self.addr = self.s.accept() # accept client's request
      print "Got Connection from",self.addr
      while True:
        file_name = self.c.recv(40) # receive file information,client name and upload/download choice from client
				if file_name == "close,close,close": # if all three parameters then the client socket closes and the server starts listening again
					break
				elif file_name.split(",")[0] == "download": # will send file to client
					try: # check if file exists and send "file not found"
						k = open(file_name.split(",")[2]+"/"+file_name.split(",")[1],"r") # create file object
					except IOError:
						self.c.send("file not found")
						continue
					self.c.send(k.read()) # send the file to client
					self.c.send("done") # send done signal when the file is sent completely
					print "sent", file_name
					continue
				elif file_name.split(",")[0] == "upload": # will receive file from client
					if not os.path.exists(file_name.split(",")[2]): # if client does not have a dedicated folder, create a folder in local disk
						os.mkdir(file_name.split(",")[2])
					file = open(file_name.split(",")[2]+"/"+file_name.split(",")[1],"w") # open file in write mode
					self.c.send("1") # send acknowledgement to client on receiving of which the client will start sending the file
					while True:
						k = self.c.recv(1024) #receive 1024 bytes continously while loop is running
						if k == "done": # break the process if done signal is received
							print "received", file_name
							break
						else:
							file.write(k) # write data to file
							continue
					continue	
			continue



#create 3 servers on different ports 
s1 = chatApp(12429)
s2 = chatApp(12345)
s3 = chatApp(12346)

#create threads for each server
t1 = threading.Thread(target=s1.run)
t2 = threading.Thread(target=s2.run)
t3 = threading.Thread(target=s3.run)

#start threads to run the servers parallelly
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()



