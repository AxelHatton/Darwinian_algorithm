import random as r


def generation_aleat(P, a, b): #ça semble fonctionner
    """Génère P individus de manière aléatoire"""
    liste = []
    for i in range(P):
        a = r.uniform(a, b)
        b = r.uniform(a, b)
        c = r.uniform(a, b)
        j = (a, b, c)
        liste.append(j)
    return (liste)


def evaluation(liste): #ça semble fonctionner
    """Note les performance de chaque individu"""
    note = []
    taille = len(liste)
    for i in range(taille):
        (a, b, c) = liste[i]
        j = abs(4-(a+2*b-3*c))
        j = j+abs(11-(a+3*b-c))
        j = j+abs(13-(2*a+5*b-5*c))
        j = j+abs(18-(a+4*b+c))
        note.append(j)
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


def reproduction(liste): #ça semble marcher
    """Génère 50% d'enfants supplémentaires à partir des 50% meilleures solutions"""
    n = len(liste)
    n = n//2
    for i in range(n):
        (a,b,c) = liste[2*i]
        (d,e,f) = liste[2*i+1]
        (g,h,i) = ((a+d)/2,(b+e)/2,(c+f)/2)
        (j,k,l) = ((a-2*d)/2,(b-2*e)/2,(c-2*f)/2)
        x = (g,h,i)
        y = (j,k,l)
        liste.append(x)
        liste.append(y)
    return(liste)


def mutation(liste, n): #ça fonctionne
    """Fait muter n enfants"""
    taille = len(liste)
    for i in range(n):
        a = r.random()
        b = r.random()
        c = r.random()
        a = a-.5
        b = b-.5
        c = c-.5
        (d,e,f) = liste[taille-i-1]
        d = d+a
        e = e+b
        f = f+c
        liste[taille-i-1] = (d,e,f)
    return(liste)