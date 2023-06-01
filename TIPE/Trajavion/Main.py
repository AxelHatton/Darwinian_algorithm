"""Importation modules"""
import fonctions as f
import random as r
import numpy as np
import matplotlib.pyplot as pl

"""Annonce des entrées"""
nombreAvion = 2
taille = 100                    # taille de l'espace de recherche en km²
Population = 100                # population de solutions pour chaque avion
x = [(50,50), (0,100)]          # position  en x en km
y = [(0,100),(50,50)]           # position initiale en y en km
v = [5,5]                       # vitesse en km/min
amplitudeManoeuvre = [30,30]    # angle max de la manoeuvre en degré
iter = 1000                     # nombre d'itération de l'algo évolutionnaire
rayonconflit = 5                # en km
rayoninter = 1                  # en km
pas = .1
remplacement = 10               # pourcentage de solution remplacée à chaque génération
mutation = 2                    # pourcentage de solution mutant à chaque génération
trajectoire = []

"""Programme"""
for i in range(nombreAvion):
    (trajAvion,temps) = f.generation_traj(x[i],y[i],pas,v[i],1,(1,0))
    trajectoire.append(trajAvion) #on génère les trajectoires en ligne droites
for k in range(nombreAvion): #on teste la validité des trajectoires entre elles
    traj1 = trajectoire[k]
    for l in range(nombreAvion):
        traj2 = trajectoire[l]
        if l != k:
            valide = f.conforme(traj1,traj2,rayoninter)
            if valide == False: #si la trajectoire n'est pas valide on applique l'algorithme évolutif
                """Initialisation algo évolutif"""
                tcontact = f.contact(traj1, traj2, rayonconflit)
                trajcorrige = []
                note = []
                while len(trajcorrige)<Population: #on génère 'Population' trajectoires alternatives
                    (trajAvion,temps) = f.modif_traj(traj1,tcontact,f.generation_maneuvres(1,amplitudeManoeuvre[k],pas),pas,v[k])
                    if f.conforme(trajAvion,traj2,rayoninter) == True: #on ne garde que les trajectoires conformes
                        trajcorrige.append(trajAvion)
                        note.append(temps)
                (trajcorrige,note) = f.tri(trajcorrige,note) #on finit l'initialisation par le tri des deux listes
                """Boucle"""
                for i in range(iter): #on itère la boucle un nombre prédéterminé de fois pour limiter le temps de calcul
                    for j in range(Population * remplacement / 100): # on supprime 'remplacement'% les solutions les moins efficaces
                        del trajcorrige[-1]
                    trajcorrige = f.reproduction(trajcorrige,Population)
                    trajcorrige = f.mutation(trajcorrige)
                    note = f.evaluation(trajcorrige,pas)
                    (trajcorrige, note) = f.tri(trajcorrige, note)


"""Dessin trajectoire"""
pl.subplot(1,1,1)
for i in trajectoire: #dessine les trajectoires en ligne droites
    (listex,listey) = f.extraction(i)
    pl.plot(listex, listey,'-k')
for i in trajcorrige: # dessine les trajectoires corrigées
    (listex, listey) = f.extraction(i)
    pl.plot(listex, listey, '-r')
pl.xlim(0,100)
pl.ylim(0,100)
pl.xlabel('x')
pl.ylabel('y')
pl.grid()
pl.legend()
pl.show()