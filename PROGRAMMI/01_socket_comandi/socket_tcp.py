import socket
from libreria import AlphaBot

IP_PORT = ("0.0.0.0", 10000)
BUFFER_SIZE = 4096

# comandi per il movimento WASD
def command_alphabot(a, c):
    if c.upper() == "W":
        a.forward()
    elif c.upper() == "S":
        a.backward()
    elif c.upper() == "D":
        a.right()
    elif c.upper() == "A":
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
        command = datas.decode().upper()
        # se è stato ricevuto EXIT o sono stati inviati dati vuoti (no byte) chiude tutto
        if command == "EXIT" or not datas:
            connection.sendall("Chiusura del server".encode())
            break
        command_alphabot(alphabot, command)

    alphabot.cleanup()
    connection.close()
    s.close()

if __name__=="__main__":
    main()