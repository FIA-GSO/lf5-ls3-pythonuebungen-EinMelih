# Aufgabe 2: Streichholzspiel
# Das so genannte Nim-Spiel ist ein Spiel für zwei Personen, bei dem abwechselnd eine Anzahl von Gegenständen (z.B. Streichhölzer) weggenommen wird. Gewonnen hat derjenige, der den letzten Gegenstand nehmen muss.

# Hintergrund: The Nimatron is a computer that allows one to play the game Nim. It was first presented in April 1940 at the 1939 New York World's Fair purely as a form of entertainment. (Quelle: https://en.wikipedia.org/wiki/Nimatron)

# Implementieren Sie das Streichholzspiel in folgender Variante als PAP/ in Python.

# Es sind 31 Streichhölzer gegeben. Die Spieler A (Computer) und B (Mensch) nehmen abwechselnd mindestens ein und höchstens sechs Streichhölzer. Spieler A (Computer) fängt an. Wer das letzte Streichholz nehmen muss, hat verloren.

# Algorithmus:

# PYTHON nimmt 2 Streichhölzer
# MENSCH nimmt beliebig 1 bis 6 Streichhölzer.
#PYTHON nimmt eine ergänzende Anzahl, so dass insgesamt 7 entnommen werden.
# Schritte 2 und 3 werden wiederholt bis nur noch ein Streichholz übrigbleibt.
# Dieses Streichholz muss Spieler B nehmen, der dadurch verliert.
# Optionale Varianten: - Der menschliche Spieler darf die Anzahl der Streichhölzer für den Start festlegen. - Der Computerspieler legt die Anzahl der Streichhölzer für den Start zufällig fest.

def streichholz_spiel():
    while True:
        value_streichholz = 31
        print ("Willkommen zum Streichholzspiel dein Ziel ist es nicht das letzte Streichholz nehmen zu müssen.")
        print ("Erster Zug Spieler A")
        value_streichholz -= 2
        print ("Spieler A hat 2 Streichhölzer gezogen!")
        print ("Verbleibende Streichhölzer:", value_streichholz)
        turn_player_b = int(input("Geben sie eine Zahl von 1 - 6 ein\n:"))
        value_streichholz -= turn_player_b
        print ("Verbleibende Streichhölzer:", value_streichholz)
        
        break
    
streichholz_spiel()