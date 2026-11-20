import socket
from libreria import AlphaBot

IP_PORT = ("0.0.0.0", 10000)
BUFFER_SIZE = 4096

def command_alphabot(a, c):
    if c == "W":
        a.forward()
    elif c == "S":
        a.backward()
    elif c == "D":
        a.right()
    elif c == "A":
        a.left()
    elif c == "STOP":
        a.stop()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # riavvio senza "Address already in use"
    s.bind(IP_PORT)
    s.listen()
    print("Server in attesa di connessione...")
    connection, address = s.accept()
    connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    print(f"Client connesso: {address}")

    alphabot = AlphaBot()
    buffer = ""
    running = True

    try:
        while running:
            datas = connection.recv(BUFFER_SIZE)
            if not datas:  # il client ha chiuso la connessione
                break
            buffer += datas.decode()

            # estrae tutti i comandi completi (terminati da \n)
            while "\n" in buffer:
                command, buffer = buffer.split("\n", 1)
                command = command.strip().upper()
                print(f"Ricevuto {command}")
                if command == "EXIT":
                    running = False
                    break
                command_alphabot(alphabot, command)
    finally:
        alphabot.cleanup()  # ferma sempre i motori, anche in caso di errore
        connection.close()
        s.close()

if __name__ == "__main__":
    main()