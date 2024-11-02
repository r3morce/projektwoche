# =================================================================
# PYTHON GRUNDLAGEN: SCHLEIFEN
# =================================================================
# In dieser Lektion lernen wir Schleifen kennen. Mit Schleifen können
# wir Anweisungen mehrmals ausführen lassen, ohne sie immer wieder
# neu schreiben zu müssen.

# -----------------------------------------------------------------
# 1. ERSTE SCHLEIFE
# -----------------------------------------------------------------
# Die for-in Schleife mit range() ist wie ein Countdown: Sie zählt
# von einer Startzahl bis zu einer Endzahl
print("Erste Schleife läuft...")  # Unsere erste Schleife!
for i in range(3):
    print("Durchlauf Nummer", i)
# Hinweis: Beim Programmieren fängt das Zählen bei 0 an. 

# TODO: Kommentiere die folgenden Zeilen ein und beobachte, wie die
# Schleife verschiedene Zahlen ausgibt
# print("\nZähle bis 5:")
# for zahl in range(5):
#     print("Aktuelle Zahl:", zahl + 1)
# Weil das Programm beim 0 anfängt zu zählen, addieren wir 1,
# so dass Normalos das auch verstehen

# -----------------------------------------------------------------
# 2. STARTPUNKT FESTLEGEN
# -----------------------------------------------------------------
# Mit range(start, ende) können wir den Startpunkt bestimmen
# TODO: Kommentiere die folgenden Zeilen ein und beobachte die Ausgabe
# print("\nZähle von 1 bis 3:")
# for n in range(1, 4):
#     print("Level", n)

# -----------------------------------------------------------------
# 3. TEXT WIEDERHOLEN
# -----------------------------------------------------------------
# Schleifen können auch verwendet werden, um Text zu wiederholen
# TODO: Kommentiere die folgenden Zeilen ein und sieh dir an, wie
# der Text mehrmals ausgegeben wird
# print("\nSpiele Sound-Effekt:")
# for _ in range(3):
#     print("*bling*")

# -----------------------------------------------------------------
# 4. ÜBER TEXT ITERIEREN
# -----------------------------------------------------------------
# Mit einer for-Schleife können wir auch über Text gehen
# TODO: Kommentiere die folgenden Zeilen ein und beobachte, wie
# jeder Buchstabe einzeln ausgegeben wird
# spieler_name = "Alex"
# print("\nBuchstabiere Namen:")
# for buchstabe in spieler_name:
#     print(buchstabe)

# -----------------------------------------------------------------
# 5. EINRÜCKUNG BEACHTEN
# -----------------------------------------------------------------
# Alles was zur Schleife gehört, muss eingerückt sein
# TODO: Kommentiere die folgenden Zeilen ein und beobachte den
# Unterschied zwischen eingerücktem und nicht eingerücktem Code
# print("\nEinrückung testen:")
# for i in range(3):
#     print("Dieser Text ist eingerückt")
# print("Dieser Text ist nicht eingerückt")

# -----------------------------------------------------------------
# ÜBUNGSAUFGABEN
# -----------------------------------------------------------------
# 1. Schreibe eine Schleife, die einen "Countdown" von 5 bis 1 macht
#    und am Ende "Start!" ausgibt

# 2. Erstelle eine Schleife, die 3-mal nach einer Eingabe fragt
#    (z.B. "Gib eine Zahl ein:") und die Eingabe ausgibt

# 3. Schreibe ein kleines Programm, das einen eingegebenen Namen
#    buchstabiert und vor jeden Buchstaben einen Strich macht
#    (z.B. "Sam" wird zu "- S", "- a", "- m")