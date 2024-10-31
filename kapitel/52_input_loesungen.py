# 52_input_loesungen.py
# ====================
# THEMA: Lösungen zu den Input-Aufgaben
# ====================

# Lösung 1: Steckbrief-Generator
print("=== Steckbrief ===")
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
hobby = input("Was ist dein Hobby? ")
farbe = input("Was ist deine Lieblingsfarbe? ")

print("\n=== Dein Steckbrief ===")
print("Name:", name)
print("Alter:", alter)
print("Hobby:", hobby)
print("Lieblingsfarbe:", farbe)
print()

# Lösung 2: Punkterechner
print("=== Punkterechner ===")
punkte1 = int(input("Punkte in Level 1: "))
punkte2 = int(input("Punkte in Level 2: "))

gesamt = punkte1 + punkte2
durchschnitt = gesamt / 2

print("Gesamtpunktzahl:", gesamt)
print("Durchschnitt:", durchschnitt)
print()

# Lösung 3: Temperaturumrechner
print("=== Temperaturumrechner ===")
celsius = float(input("Temperatur in Celsius: "))
fahrenheit = celsius * 9/5 + 32

print(celsius, "°C sind", fahrenheit, "°F")
