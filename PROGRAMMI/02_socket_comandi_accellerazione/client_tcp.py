import socket
from pynput import keyboard

IP_PORT = ("192.168.0.215", 10000)  # ip alphabot
COMANDI = {
    "w": "W",
    "s": "S",
    "a": "A",
    "d": "D",
    keyboard.Key.up: "ACCELERA",
    keyboard.Key.down: "RALLENTA"
    }

tasto_attivo = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # invia subito, senza attese
s.connect(IP_PORT)
print("Connessione effettuata!")
print("Tieni premuto W, S, A, D per muoverti.")
print("Schiaccia freccia su per accelerare, schiaccia freccia giu per rallentare.") 
print("Premi ESC per uscire.")
def invia(msg):
    s.sendall((msg + "\n").encode())  # \n = fine comando

def premuto(tasto):
    global tasto_attivo
    c = getattr(tasto, "char", None)
    if c is not None:
        c = c.lower()  # funziona anche con Caps Lock / Shift
    if c in COMANDI and tasto_attivo != c:
        tasto_attivo = c
        invia(COMANDI[c])

def rilasciato(tasto):
    global tasto_attivo
    if tasto == keyboard.Key.esc:
        invia("EXIT")
        return False
    c = getattr(tasto, "char", None)
    if tasto = keyboard.Key.up:
        invia(COMANDI[tasto])
    if tasto = keyboard.Key.down:
        invia(COMANDI[tasto])
    if c is not None:
        c = c.lower()
    if c is not None and c == tasto_attivo:
        tasto_attivo = None
        invia("STOP")

def main():
    with keyboard.Listener(on_press=premuto, on_release=rilasciato) as listener:
        listener.join()
    s.close()

if __name__ == "__main__":
    main()