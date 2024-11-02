# =================================================================
# PYTHON GRUNDLAGEN: SCHLEIFEN - LÖSUNGEN
# =================================================================

# Lösung 1: Countdown
print("=== Countdown ===")
for i in range(5, 0, -1):
    print(i)
print("Start!")

# Lösung 2: Mehrfache Eingabe
print("\n=== Zahlen eingeben ===")
for i in range(3):
    zahl = input("Gib eine Zahl ein: ")
    print("Eingegebene Zahl:", zahl)

# Lösung 3: Namen buchstabieren
print("\n=== Namen buchstabieren ===")
name = input("Gib einen Namen ein: ")
for buchstabe in name:
    print("-", buchstabe)