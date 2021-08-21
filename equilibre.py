import random

def algorithmeUn(lst):
    """ Construit un arbre dont chaque nouvelle feuille est placée au bout de la branche droite. """
    if lst == []:
        return lst
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return [lst[1], lst[0]]
    else:
        return [algorithmeUn(lst[1:]), lst[0]]

def algorithmeDeux(lst):
    """ Construit un arbre dont chaque nouvelle feuille est placée au bout de la branche gauche. """
    if lst == []:
        return lst
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return [lst[0], lst[1]]
    else:
        return [lst[0], algorithmeDeux(lst[1:])]

def algorithmeTrois(lst) :
    """ Construit un arbre aléatoire. """
    if lst == []:
        return lst
    elif len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        if random.randint(0, 1) == 0:
            return lst
        else:
            return lst[::-1]
    else:
        b = random.randint(0, len(lst) - 1)
        
        if random.randint(0, 1) == 0:
            return [algorithmeTrois(lst[:b] + lst[b+1:]), lst[b]]
        else:
            return [lst[b], algorithmeTrois(lst[:b] + lst[b+1:])]

def algorithmeQuatre(lst):
    """ Construit un arbre avec un écart minimum entre les deux branches principales. """
    if lst == []:
        return lst
    elif len(lst) == 1:
        return lst[0]
    else:
        res = ecartMini(lst)
        
        return [algorithmeUn(res[0]), algorithmeDeux(res[1])]

# --- FONCTIONS AUXILIAIRES --- #
def insererD(T, i):
    j = i
    
    while j > 0 and T[j - 1] < T[j]:
        T[j - 1], T[j] = T[j], T[j - 1]
        j = j - 1

def triInsertionD(T):
    """ Tri par insertion. """
    for i in range(1, len(T)):
        insererD(T, i)
    
    return T

def ecartMini(res):
    lst = triInsertionD(res)
    gauche = []
    poig = 0
    droite = []
    poid = 0
    
    for i in range(len(lst)):
        if poig >= poid:
            droite.append(lst[i])
            poid = poid + lst[i]
        else:
            gauche.append(lst[i])
            poig = poig + lst[i]
    
    return [gauche, droite]
