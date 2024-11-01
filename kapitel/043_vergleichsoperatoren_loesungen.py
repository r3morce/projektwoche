# =================================================================
# PYTHON GRUNDLAGEN: VERGLEICHSOPERATOREN - LÖSUNGEN
# =================================================================

# Lösung 1: Spielerpunkte vergleichen
spieler1_punkte = 150
spieler2_punkte = 100
print("\n=== Punktevergleich ===")
print("Spieler 1:", spieler1_punkte)
print("Spieler 2:", spieler2_punkte)
print("Gleiche Punktzahl?", spieler1_punkte == spieler2_punkte)
print("Spieler 1 hat mehr Punkte?", spieler1_punkte > spieler2_punkte)
print("Spieler 2 hat mehr Punkte?", spieler1_punkte < spieler2_punkte)

# Lösung 2: Mindestlevel für Quest überprüfen
spieler_level = 4
mindest_level = 5
print("\n=== Quest-Überprüfung ===")
print("Spieler Level:", spieler_level)
print("Benötigtes Level:", mindest_level)
print("Quest kann gestartet werden?", spieler_level >= mindest_level)