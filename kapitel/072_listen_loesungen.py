# =================================================================
# PYTHON GRUNDLAGEN: LISTEN - LÖSUNGEN
# =================================================================

# Lösung 1: Hobbys Liste
hobbys = ["Gitarre", "Gaming", "Zeichnen"]
print("=== Hobbys ===")
print("Erstes Hobby:", hobbys[0])
print("Letztes Hobby:", hobbys[2])

# Lösung 2: Zahlenliste verändern
zahlen = [10, 20, 30, 40, 50]
print("\n=== Zahlenliste ===")
print("Original:", zahlen)
zahlen.append(60)
print("Nach Hinzufügen:", zahlen)
zahlen[2] = 35
print("Nach Änderung:", zahlen)

# Lösung 3: Spielerliste erweitern
spieler = ["Robin", "Sam", "Alex"]
print("\n=== Spielerliste ===")
print("Aktuelle Spieler:", spieler)
neuer_spieler = input("Gib einen neuen Spielernamen ein: ")
spieler.append(neuer_spieler)
print("\nAlle Spieler:")
for name in spieler:
    print("-", name)