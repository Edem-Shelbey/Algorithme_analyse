#brute_force.py
import time
import csv
import sys

BUDGET = 500000

# Lire le fichier CSV
fichier = sys.argv[1]
actions = []

with open(fichier) as f:
    lecteur = csv.reader(f, delimiter=';')
    next(lecteur)
    
    for ligne in lecteur:
        if ligne:
            nom = ligne[0]
            cout = int(float(ligne[1]))
            pct = float(ligne[2].replace('%', ''))
            profit = int(round(cout * pct / 100))
            actions.append([nom, cout, profit])

# Compter le nombre d'actions
n = 0
for action in actions:
    n += 1

# Démarrer le chronomètre
debut = time.time()

# Tester toutes les combinaisons
max_profit = 0
max_cout = 0
max_nb = 0
meilleure_combi = 0

combi = 0
while combi < 2 ** n:
    cout_tot = 0
    profit_tot = 0
    nb = 0
    
    i = 0
    while i < n:
        if combi & (1 << i):
            cout_tot += actions[i][1]
            profit_tot += actions[i][2]
            nb += 1
        i += 1
    
    if cout_tot <= BUDGET and profit_tot > max_profit:
        max_profit = profit_tot
        max_cout = cout_tot
        max_nb = nb
        meilleure_combi = combi
    
    combi += 1

# Arrêter le chronomètre
fin = time.time()
temps_execution = fin - debut

# Récupérer la liste des actions choisies
actions_choisies = []
i = 0
while i < n:
    if meilleure_combi & (1 << i):
        actions_choisies.append(actions[i][0])
    i += 1

# Afficher résultat
print("Temps d'exécution:", round(temps_execution, 4), "secondes")
print("Actions achetées:", max_nb)
print("Coût total:", max_cout)
print("Profit total:", max_profit)
print("Liste des actions:", actions_choisies)