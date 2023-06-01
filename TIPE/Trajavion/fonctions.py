import random as r
import numpy as np
import matplotlib.pyplot as pl

def generation_manoeuvres(pop, Amp, pas): #ça marche
    result = []
    for i in range(pop):
        deltat = r.uniform(1,5)
        deltat = (deltat//pas)*pas
        angle = r.uniform(-Amp, Amp)*np.pi/180
        tup = (deltat, angle)
        result.append(tup)
    return(result)

def generation_traj(posx,posy, pas, v, tman, man): #ça marche
    """génère une trajectoire """
    (xi,xf) = posx
    (yi,yf) = posy
    pos = (xi,yi)
    temps = 0
    tman = int(tman/pas)
    (deltat, amp) = man
    trajectoire =[pos,]
    delta = np.sqrt(((xf-xi)**2)+((yf-yi)**2))
    while delta > .1:
        if temps != tman:
            (x, y) = pos
            if (xf-x)<.01:
                angle = np.pi/2
            else:
                teta = (yf - y) / (xf - x)
                angle = np.arctan(teta)
            x = x + pas * v * np.cos(angle)
            y = y + pas * v * np.sin(angle)
            delta = np.sqrt(((xf - x) ** 2) + ((yf - y) ** 2))
            pos = (x, y)
            temps = temps + 1
            trajectoire.append(pos)
        elif temps == tman:
            taille = int(deltat/pas)
            for i in range(taille):
                x = x + pas * v * np.cos(angle+amp)
                y = y + pas * v * np.sin(angle+amp)
                temps = temps + 1
                pos = (x, y)
                trajectoire.append(pos)
    return(trajectoire,temps)

def modif_traj(traj,tman,man,pas,v):
    t = 0
    tman = int(tman / pas)
    result = []
    while t < tman:
        result.append(traj[t])
        t = t+1
    (xi,yi) = result[-1]
    (xf,yf) = traj[-1]
    (trajmod,onsenfout) = generation_traj((xi,xf),(yi,yf),pas,v,0,man)
    for i in trajmod:
        result.append(i)
    temps = len(result)*pas
    return (result,temps)

def conforme(traj1,traj2,rayoninter): #ça marche
    """Vérifie si une trajectoire est conforme (ie si les avions ne pénètrent pas leurs zones interdites respective)"""
    conf = True
    taille = min(len(traj1),len(traj2))
    for i in range(taille):
        (x1,y1) = traj1[i]
        (x2, y2) = traj2[i]
        distance = (x1-x2)**2+(y1-y2)**2
        if distance <= 2*rayoninter:
            conf = False
    return(conf)

def contact(traj1,traj2,rayonconflit):
    """Renvoie le temps de contact des zones de conflits"""
    t = 0
    taille = min(len(traj1), len(traj2))
    while t<taille:
        (x1, y1) = traj1[t]
        (x2, y2) = traj2[t]
        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if distance <= 2 * rayonconflit:
            return (t)
        t=t+1
    return(None)

def extraction(trajectoire): #ça marche
    """Extrait les positions successives en x et en y d'une trajectoire"""
    listex = []
    listey = []
    for (x, y) in trajectoire:
        listex.append(x)
        listey.append(y)
    tup = (listex,listey)
    return(tup)

def evaluation(listetraj, pas):
    note = []
    for i in range(listetraj):
        note.append(pas * len(listetraj[i]))
    return(note)

def tri(liste, note):
    """Tri les individus en fonction de leur note""" #méthode du tri à bulle
    n = len(note)
    i = n - 1
    triee = False
    while i > 0 and triee == False:
        triee = True
        for j in range(i):
            if note[j] > note[j + 1]:
                a = liste[j]
                b = note[j]
                liste[j] = liste[j + 1]
                note[j] = note[j+1]
                liste[j + 1] = a
                note[j+1] = b
                triee = False
        i = i - 1
    return (liste,note)

def reproduction(traj,pop):
    while len(traj)<pop: #trouver méthode de reproduction

def mutation(traj): #trouver méthode de mutation