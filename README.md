# Cloud-Storage-using-Python
Cloud storage application to upload and download files 

1. Server Client model to store and download files on the cloud. 

2. On running the server, client connects with it and requests upload/download, file name and client name from the client.

3. Client sends this data to server.
  1. If Upload:
      On upload request, Server creates a folder for that paticular client if it does not already exist and creates a blank document with       the received file name in that folder. Server continously receives the data from client and writes it to the file.
  2. If Download:
      On download request, the server goes to the client's folder to read the reqested file. Once the file is read, it is sent to the           client. The client continouslty reads the data sent from server and writes it to the a blank file in its local disk.

4. Three servers run in parallel and all the three servers contain the same data. 

5. Since there can be any number of cilents, the client chooses the server which is free at the moment and downloads or uploads the data     from it. 
