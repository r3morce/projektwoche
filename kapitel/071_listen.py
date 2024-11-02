# =================================================================
# PYTHON GRUNDLAGEN: LISTEN
# =================================================================
# In dieser Lektion lernen wir Listen kennen. Listen sind wie 
# digitale Behälter, in denen wir mehrere Werte speichern können.
# Zum Beispiel alle Highscores oder die Namen aller Spielfiguren.

# -----------------------------------------------------------------
# 1. ERSTE LISTE ERSTELLEN
# -----------------------------------------------------------------
farben = ["rot", "grün", "blau"]  # Unsere erste Liste!
print("Verfügbare Farben:", farben)

# TODO: Kommentiere die folgenden Zeilen ein und beobachte,
# wie verschiedene Werte in einer Liste gespeichert werden können
# highscores = [100, 95, 85, 70]
# print("Die besten Punktzahlen:", highscores)

# -----------------------------------------------------------------
# 2. AUF LISTENELEMENTE ZUGREIFEN
# -----------------------------------------------------------------
# Mit einem Index (Position) können wir einzelne Elemente abrufen
# Der Index beginnt bei 0!
# TODO: Kommentiere die folgenden Zeilen ein und beobachte den Zugriff
# charaktere = ["Magier", "Krieger", "Bogenschütze"]
# print("Erster Charakter:", charaktere[0])
# print("Zweiter Charakter:", charaktere[1])
# print("Letzter Charakter:", charaktere[2])

# -----------------------------------------------------------------
# 3. LISTEN VERÄNDERN
# -----------------------------------------------------------------
# Listen sind veränderbar - wir können Elemente hinzufügen und ändern
# TODO: Kommentiere die folgenden Zeilen ein und beobachte die Änderungen
# inventar = ["Schwert", "Schild", "Trank"]
# print("Ursprüngliches Inventar:", inventar)
# inventar.append("Bogen")  # Ein Element hinzufügen
# print("Inventar nach Fund:", inventar)
# inventar[2] = "Super-Trank"  # Ein Element ändern
# print("Inventar nach Upgrade:", inventar)

# -----------------------------------------------------------------
# 4. LISTEN DURCHLAUFEN
# -----------------------------------------------------------------
# Mit einer for-Schleife können wir alle Elemente durchgehen
# TODO: Kommentiere die folgenden Zeilen ein und beobachte die Ausgabe
# level_zeiten = [45, 33, 50, 25]
# print("\nZeiten für jedes Level:")
# for zeit in level_zeiten:
#     print("Level geschafft in", zeit, "Sekunden")

# -----------------------------------------------------------------
# 5. LISTENLÄNGE UND WEITERE FUNKTIONEN
# -----------------------------------------------------------------
# Listen haben viele nützliche eingebaute Funktionen
# TODO: Kommentiere die folgenden Zeilen ein und teste die Funktionen
# team = ["Spiderman", "Moon Knight", "Colossus"]
# print("\nTeammitglieder:", len(team))  # Anzahl der Elemente
# team.sort()  # Liste alphabetisch sortieren
# print("Sortierte Liste:", team)
# team.reverse()  # Liste umdrehen
# print("Umgedrehte Liste:", team)

# -----------------------------------------------------------------
# ÜBUNGSAUFGABEN
# -----------------------------------------------------------------
# 1. Erstelle eine Liste mit mindestens 3 Hobbys und gib das erste
#    und letzte Hobby aus
#
# 2. Erstelle eine Liste mit 5 Zahlen, füge eine neue Zahl hinzu
#    und ändere dann eine bestehende Zahl
#
# 3. Erstelle eine Liste mit Spielernamen. Lass den Benutzer einen
#    neuen Namen eingeben und füge diesen zur Liste hinzu.
#    Gib dann alle Namen der Reihe nach aus.