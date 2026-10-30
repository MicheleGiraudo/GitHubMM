import socket
from libreria import AlphaBot

IP_PORT = ("0.0.0.0", 13000)
BUFFER_SIZE = 4096

def command_alphabot(a, c):
    if c.upper() == "F":
        a.forward()
    elif c.upper() == "B":
        a.backward()
    elif c.upper() == "R":
        a.right()
    elif c.upper() == "L":
        a.left()
    elif c.upper() == "STOP":
        a.stop()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(IP_PORT)
    print("Server attivo...")  
    s.listen()
    print("Server in attesa di connessione...") 
    connection, address = s.accept()
    print(f"Client connesso: {address}")
    
    alphabot = AlphaBot()

    while True:
        datas = connection.recv(BUFFER_SIZE)
        print(f"Ricevuto {datas.decode()}")
        command = datas.decode()
        if command.upper() == "EXIT":
            connection.sendall("Chiusura del server".encode())
            break
        else:
            command_alphabot(alphabot, command)

    connection.close()
    s.close()

if __name__=="__main__":
    main()