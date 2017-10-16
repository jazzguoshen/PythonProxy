
from socket import *
import sys
import os
import os.path
from thread import *

cache_file=open("Dictionary.txt", "r")
cDictionary =[line.rstrip('\n') for line in cache_file]
cache_file.close()

block_file=open("Blocked.txt", "r")
bDictionary =[line.rstrip('\n') for line in block_file]
block_file.close()

bufferSize = 8192       
def main():
	port = 8001
	max_conn = 5               
	try:
		#SETUP
		serverSocket = socket(AF_INET,SOCK_STREAM)
		serverSocket.bind(('', port))

		#WAIT FOR CONNECTION
		print( 'The server is ready to listen \n')	  
		serverSocket.listen(max_conn)

	except error, (value, message):
		if serverSocket:
			serverSocket.close()
	       	print "Could not open socket:", message
	  	sys.exit(1)
               
	while 1: 
		#ACCEPT CONNECTION
		conn, addr = serverSocket.accept() #acept connection from browser
		data = conn.recv(bufferSize)  # recieve data
	
		#START THREAD FOR CONNECTION
		start_new_thread(proxy_server,(conn, data, addr)) #start thread

	#CLOSE CONNECTION 
	serverSocket.close()

def proxy_server(conn, data, addr):
	#PARSE BROWSER REQUEST
	first_line = data.split('\n')[0] 
	url = first_line.split(' ')[1]
	http_pos = url.find("://")	
	
if(http_pos == -1):   
              	 	temp = url		 
	else:
               		temp = url[(http_pos+3):] 	

	port_pos = temp.find(":")
	webserver_pos = temp.find("/") 
		
	if webserver_pos == -1:
		webserver_pos = len(temp) 

	webserver = ""
	port = -1
	if(port_pos == -1 or webserver_pos < port_pos): 
		port = 80
		webserver = temp[:webserver_pos] 		
	else:
		port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
		webserver = temp[:port_pos]	
	print(webserver) 	
	print(port) 	
	print(conn) 	
	print(addr)
	print('\n')

	try:
		#SEND REQUEST
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((webserver, port))
		s.send(data) 
		while 1:

			#CHECK IF SITE SHOULD BE BLOCKED
			if webserver in bDictionary : 
				print("Site Blocked!")
				break
			#CHECK IF REPLY HAS BEEN CACHED PREVIOUSLY
			if webserver in cDictionary :
				cache=open(webserver+".txt", "r")
				#print("Cache Exists")
				reply=cache.read()
							
			else:
			    	#RECIEVE REPLY AND CACHE 
				reply = s.recv(bufferSize)
				cache_file=open(webserver+".txt", "w")
				cache_file.write(reply)
				cDictionary.append(webserver)
				
				temp=open("Dictionary.txt", "a")
				temp.write(webserver)	
				temp.write("\n")
				temp.close()									
		    
			if (len(reply) > 0): #if reply exisits				
		        		conn.send(reply) #send reply back to client
			else:		        				
				break				
		s.close()						
		conn.close()	
	except error, (value, message):
		if s:
			s.close()
		if conn:
			conn.close()
		sys.exit(1)

if __name__ == '__main__':
    main()
