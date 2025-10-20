#glouton.py
import time
import csv
import sys

BUDGET = 500000

debut = time.time()
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
            
            # Ignorer les actions avec cout <= 0
            if cout > 0:
                ratio = profit / cout
                actions.append([nom, cout, profit, ratio])

# Trier les actions par ratio (du plus rentable au moins rentable)
actions_triees = []
while actions:
    meilleur_index = 0
    meilleur_ratio = actions[0][3]
    
    i = 0
    nb_actions = 0
    for a in actions:
        nb_actions += 1
    
    while i < nb_actions:
        if actions[i][3] > meilleur_ratio:
            meilleur_ratio = actions[i][3]
            meilleur_index = i
        i += 1
    
    actions_triees.append(actions[meilleur_index])
    actions.pop(meilleur_index)

# Prendre les actions une par une tant qu'on ne dépasse pas le budget
cout_total = 0
profit_total = 0
actions_choisies = []

for action in actions_triees:
    nom = action[0]
    cout = action[1]
    profit = action[2]
    
    # Si on peut acheter cette action
    if cout_total + cout <= BUDGET:
        cout_total += cout
        profit_total += profit
        actions_choisies.append(nom)

fin = time.time()
temps_execution = fin - debut

# Afficher résultat
nb_achats = 0
for a in actions_choisies:
    nb_achats += 1

print("Temps d'exécution:", round(temps_execution, 4), "secondes")
print("Actions achetées:", nb_achats)
print("Coût total:", cout_total)
print("Profit total:", profit_total)
print("Liste des actions:", actions_choisies)
