import socket
import keyboard

IP_PORT = ("192.168.1.129", 13000)  #ip alphabot
BUFFER_SIZE = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(IP_PORT)
    print("Connessione effettuata!")

    print("Premi F, B, L, R per muoverti.")
    

    while True:
        if keyboard.is_pressed("f"):
            s.sendall("F")
        elif keyboard.is_pressed("b"):
            s.sendall("B")
        elif keyboard.is_pressed("l"):
            s.sendall("L")
        elif keyboard.is_pressed("r"):
            s.sendall("R")
        else:
            s.sendall("STOP")
        

    s.close()


if __name__ == "__main__":
    main()