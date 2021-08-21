import random

def generateurA():
    """ Génère une liste contenant entre 1 et 10 poids identiques. """
    a = random.randint(1, 10)
    b = random.randint(1, 200)
    
    return [b for i in range(a)]

def generateurB():
    """ Génère une liste contenant un seul poids. """
    a = random.randint(1, 900)
    
    return [a]

def generateurC():
    """ Génère une liste vide. """
    return []
