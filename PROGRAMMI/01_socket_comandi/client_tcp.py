import socket
from pynput import keyboard

IP_PORT = ("192.168.0.215", 10000)  #ip alphabot
BUFFER_SIZE = 4096

COMANDI = {"w": "W", "s": "S", "a":"A", "d":"D"} # comandi tastiera come i giochi

tasto_attivo = None  # Il tasto che sta venendo premuto al momento

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(IP_PORT)
print("Connessione effettuata!")
print("Tieni premuto W, S, A, D per muoverti. ESC per uscire.")

def premuto(tasto):
    global tasto_attivo
    c = getattr(tasto, "char", None)
    if c in COMANDI and tasto_attivo != c:
        tasto_attivo = c
        s.sendall(COMANDI[c].encode())

def rilasciato(tasto):
    global tasto_attivo
    #se il tasto rilasciato è esc manda EXIT per far chiudere il server
    if tasto == keyboard.Key.esc:
        s.sendall("EXIT".encode())
        return False
    c = getattr(tasto, "char", None)
    #se viene rilasciato il tasto che stava pilotando l'alphabot invia STOP per fermare
    if c == tasto_attivo:
        tasto_attivo = None
        s.sendall("STOP".encode())

def main():
    #imposta l'ascoltatore sulla tastiera che chiama premuto e rilasciato
    with keyboard.Listener(on_press=premuto, on_release=rilasciato) as listener:
        listener.join()

    s.close()


if __name__ == "__main__":
    main()