import fonctions as f
import time as l

liste = f.generation_aleat(100, -100, 100)  # on génère la population de départ
note = f.evaluation(liste)  # on initialise la note
(liste,note) = f.tri(liste, note)  # on tri la liste de départ
z = 0

t0 = l.time()
while note[69] > 0.01:  # on itère jusqu'à ce que 70% des individus aient une note <= à 0.01
    for i in range(50): #on supprime les 50% les moins bons
        taille = len(liste)
        del liste[taille-1]
    liste = f.reproduction(liste) #on fait se reproduire les solutions restantes
    liste = f.mutation(liste,10) #on fait muter les solutions enfant
    note = f.evaluation(liste) #on note la liste
    (liste,note) = f.tri(liste,note) #on ordonne la liste en fontion de sa note
    z = z+1
t1 = l.time()
t = t1-t0

print(t)
print(liste[0])
print(z)
