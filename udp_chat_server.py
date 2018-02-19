import socket
import time

host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0) #выключаем блокировку

quitting = False
print("Server started...")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        
        if addr not in clients:
            clients.append(addr)
  
        if "Quit" in str(data.decode('utf-8')):
            quitting = True
   
        print (time.ctime(time.time()) + str(addr) + ":: " + str(data.decode('utf-8')))

        if addr == clients[0]:
            s.sendto(data, clients[1])
        else:
            s.sendto(data, clients[0])
            
    except:
        pass
    
s.close()
            
