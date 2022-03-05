import socket
import serial

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
ser1 = serial.Serial('/dev/ttyUSB0')
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been achieved")
    clientsocket.send(bytes("Welcome", "utf-8"))
    while True:
        msg = clientsocket.recv(1024)
        print(msg)
        ser1.write(msg)
        msg = clientsocket.recv(1024)
        print(msg)
        ser1.write(msg)

