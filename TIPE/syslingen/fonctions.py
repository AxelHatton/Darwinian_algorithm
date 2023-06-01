import random as r
import time as l


def generation_aleat(P, n, a, b): #ça marche
    """Génère P individus de manière aléatoire"""
    liste = []
    for i in range(P):
        sol = (r.uniform(a,b),)
        for j in range(n-1):
            c = (r.uniform(a,b),)
            sol = sol + c
        liste.append(sol)
    return liste


def evaluation(liste, matrice, resultat): #ça marche
    """Note les performance de chaque individu"""
    note = []
    tailliste = len(liste)
    tailmat = len(matrice)
    for i in range(tailliste):
        r = liste[i]
        result = 0
        for j in range(tailmat):
            sol = 0
            u = matrice[j]
            q = resultat[j]
            for k in range(len(u)):
                sol = sol+u[k]*r[k]
            sol = abs(sol-q)
            result = result+sol
        result = abs(result)
        note.append(result)
    return note


def tri(liste, note): #ça marche
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


def reproduction(liste, n): #ça marche
    """Génère n enfants supplémentaires à partir des n meilleures solutions"""
    m = n//2
    for i in range(m):
        x = []
        y = []
        a = liste[2*i]
        b = liste[2*i+1]
        taille = len(a)
        for j in range(taille):
            c = (a[j] + b[j]) / 2
            x.append(c)
            d = (a[j]-2*b[j])/2
            y.append(d)
        liste.append(x)
        liste.append(y)


def mutation(liste, n, taux, amp): #ça marche
    """Fait muter la population d'enfants avec une proba de taux et une amplitude de amp"""
    m = len(liste)
    o = len(liste[0])
    for i in range(n):
        aleat = r.random()
        if aleat <= taux:
            v = liste[m-i-1]
            for j in range(o):
                v = liste[m-i-1]
                a = r.random()
                a = (a-.5)*2*amp
                v[j] = v[j]+a


def resolsyslin(matrice, resultat, P, a, b, n, taux, amp, eps): #A tester
    """Résout un système repréenté par matrice et résultats grâce à un algorithme évolutif\nP est la population utilisé\na et b sont les bornes de l'espace de recherche\nn est le nombre d'individu remplacé à chaque génération\ntaux est le taux de mutation chez les solutions enfants et amp est l'amplitude de la mutation\neps est la précision attendu de la solution"""
    m = len(matrice[0])
    liste = generation_aleat(P, m, a, b) # on initialise la population
    note = evaluation(liste,matrice,resultat)  # on initialise la note
    tri(liste, note)  # on tri la liste de départ
    while note[0] > eps: # on itère tant que le premier terme est supérieur à la limite
        for i in range(n): # on supprime les n moins bonnes solutions
            elementSupr = liste.pop()
        reproduction(liste, n) # on ajoute n solutions enfants
        mutation(liste,n,taux,amp) # que l'on mute
        note = evaluation(liste,matrice,resultat) # puis on note
        tri(liste, note) # et on trie
    return liste[0]


save = open('resultats.txt', 'a')
save.close()
z = 10
matrice = [[1, 2, -3], [1, 3, -1], [2, 5, -5], [1, 4, 1]]
resultat = [4, 11, 13, 18]
for P in [400, 500]:
    for n in [200,250,300]:
        for amp in [.25]:
            for tau in [.25, .5, .75, 1]:
                with open ('resultats.txt', 'a') as save:
                    headline = str('P={}; enfant={}; amplitude={}; taux={}\n').format(P, n, amp, tau)
                    save.write(headline)
                save.close()
                t = 0
                for i in range(z):
                    t0 = l.time()
                    print(resolsyslin(matrice, resultat, P, -50, 50, n, tau, amp, 0.01))
                    t1 = l.time()
                    dt = t1 - t0
                    with open('resultats.txt', 'a') as save:
                        tempIntermediaire = str('t{}={}\n').format(i, dt)
                        save.write(tempIntermediaire)
                    save.close()
                    t = t + dt
                t = t / z
                with open('resultats.txt', 'a') as save:
                    tempFinal = str('temps final moyen = {}\n').format(t)
                    save.write(tempFinal)
                save.close()
