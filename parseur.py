def lectureListe():
    """ Lit un fichier et de créer une liste d'entiers correspondant aux poids indiqués. """
    fichier = open("fichiers/liste.txt", "r") # ouverture du fichier en lecture
    liste = []
    
    try:
        for i in fichier.readlines(): # pour chaque ligne du fichier
            poids = eval(i.strip("\n")) # supprime "\n"
            
            if type(poids) == int and poids >= 0:
                liste.append(poids)
            elif type(poids) == int and poids < 0:
                print("Erreur dans le fichier liste.txt : poids négatif présent.")
            else:
                print("Erreur dans le fichier liste.txt : poids non entier présent.")
    except NameError:
        print("Erreur dans le fichier liste.txt : poids inconnu présent.")
    except SyntaxError:
        print("Erreur dans le fichier liste.txt : nombre d'espace incorrect.")
        
    fichier.close() # fermeture du fichier
    
    return liste

def lectureArbre():
    """ Lit un fichier et de créer une liste correspondant à l'arbre indiqué. """
    fichier = open("fichiers/arbre.txt", "r") # ouverture du fichier en lecture
    arbre = []
    
    try:
        arbre = eval((fichier.readline()).strip("\n"))
    except NameError:
        print("Erreur dans le fichier arbre.txt : poids inconnu présent.")
    
    fichier.close() # fermeture du fichier
    
    return arbre

def ecritureArbre(arbre):
    """ Écrit dans un fichier une liste correspondant à un arbre. """
    fichier = open("fichiers/sauvegarde.txt", "w") # ouverture du fichier en écriture
    
    fichier.write(str(arbre) + "\n")
    fichier.close() # fermeture du fichier
