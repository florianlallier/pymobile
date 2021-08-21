import parseur
import equilibre
import generateur
import tkinter
import math
import os
import random

def interface(liste, arbre):
    """ Interface graphique. """

    def action(abr):
        """ Affiche le mobile et enregistre l'arbre dans un fichier. """
        canevas.delete(tkinter.ALL)
        afficheMobile(abr, 700, 40, 200)
        parseur.ecritureArbre(abr)

    def afficheMobile(list, x, y, l):
        """ Affiche le mobile. """
        if list == []: # racine seule
            canevas.create_line(x, y, x, y + 40) # tige (x1, y1, x2, y2)
        elif type(list) == int: # on dessine une feuille
            canevas.create_line(x, y, x, y + 40) # tige bis (x1, y1, x2, y2)
            try:
                canevas.create_oval(x - 2 * math.sqrt(list), y + 40, x + 2 * math.sqrt(list), y + 40 + 2 * 2 * math.sqrt(list), outline = 'black', fil = ['red', 'yellow', 'green', 'blue'][random.randrange(4)]) # dessine le cercle par rapport au rectangle circonscrit
            except ValueError:
                print("Erreur dans le fichier arbre.txt : poids négatif présent.")
        elif len(list) == 1: # arbre avec une seule feuille
            afficheMobile(list[0], x, y, l)
        else: # arbre avec deux feuilles ou plus
            if l > 50:
                l = l - 15
            p1 = sommeListe(list[0])
            p2 = sommeListe(list[1])
            l1 = (p2 * l) / (p1 + p2)
            canevas.create_line(x, y, x, y + 40) # tige (x1, y1, x2, y2)
            canevas.create_line(x - l1, y + 40, x + (l - l1), y + 40) # barre horizontale (x1, y1, x2, y2)
            afficheMobile(list[0], x - l1, y + 40, l)
            afficheMobile(list[1], x + (l - l1), y + 40, l)

    def sommeListe(list):
        """ Calcule la somme des éléments d'une liste à N dimensions. """
        if type(list) == int:
            return list
        else:
            return sommeListe(list[0]) + sommeListe(list[1])

    def l1():
        """ Affiche le mobile avec l'algorithme 1 à partir de la liste. """
        action(equilibre.algorithmeUn(liste))

    def l2():
        """ Affiche le mobile avec l'algorithme 2 à partir de la liste. """
        action(equilibre.algorithmeDeux(liste))

    def l3():
        """ Affiche le mobile avec l'algorithme 3 à partir de la liste. """
        action(equilibre.algorithmeTrois(liste))

    def l4():
        """ Affiche le mobile avec l'algorithme 4 à partir de la liste. """
        action(equilibre.algorithmeQuatre(liste))

    def a1():
        """ Affiche le mobile à partir de l'arbre. """
        action(arbre)

    def g1():
        """ Affiche un mobile avec l'algorithme 1 à partir d'une liste aléatoire. """
        action(equilibre.algorithmeUn(generateur.generateurA()))

    def g2():
        """ Affiche un mobile avec l'algorithme 2 à partir d'une liste aléatoire. """
        action(equilibre.algorithmeDeux(generateur.generateurA()))

    def g3():
        """ Affiche un mobile avec l'algorithme 3 à partir d'une liste aléatoire. """
        action(equilibre.algorithmeTrois(generateur.generateurA()))

    def g4():
        """ Affiche un mobile avec l'algorithme 4 à partir d'une liste aléatoire. """
        action(equilibre.algorithmeQuatre(generateur.generateurA()))

    def g5():
        """ Affiche un mobile à partir d'un poids aléatoire. """
        action(generateur.generateurB())

    def g6():
        """ Affiche un mobile sans poids. """
        action(generateur.generateurC())

    def editerListe():
        """ Ouvre le fichier liste.txt dans une fenêtre Emacs. """
        os.system("emacs fichiers/liste.txt")
        fenetre.destroy()
        os.system("./pymobile.py")

    def editerArbre():
        """ Ouvre le fichier arbre.txt dans une fenêtre Emacs. """
        os.system("emacs fichiers/arbre.txt")
        fenetre.destroy()
        os.system("./pymobile.py")

    def consulterSauvegarde():
        """ Ouvre le fichier sauvegarde.txt dans une fenêtre Emacs. """
        os.system("emacs fichiers/sauvegarde.txt")

    # Fenêtre :
    fenetre = tkinter.Tk()
    fenetre.title("Pymobile")
    fenetre.geometry("%dx%d+0+0" % (fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))
    
    # Canevas :
    h = tkinter.Scrollbar(fenetre, orient = "horizontal")
    v = tkinter.Scrollbar(fenetre, orient = "vertical")
    canevas = tkinter.Canvas(fenetre, width = fenetre.winfo_screenwidth(), height = fenetre.winfo_screenheight(), bg = "white", scrollregion = (0, 0, 10000, 10000), yscrollcommand = v.set, xscrollcommand = h.set)
    h['command'] = canevas.xview
    v['command'] = canevas.yview
    canevas.grid(column = 0, row = 0, sticky = ("n", "w", "e", "s"))
    h.grid(column = 0, row = 1, sticky = ("w", "e"))
    v.grid(column = 1, row = 0, sticky = ("n", "s"))
    fenetre.grid_columnconfigure(0, weight = 1)
    fenetre.grid_rowconfigure(0, weight = 1)
    
    # Barre de menu :
    barre = tkinter.Menu(fenetre, activebackground = '#77B5FE')
    barrePymobile = tkinter.Menu(barre, tearoff = 0, activebackground = '#77B5FE')
    barrePymobile.add_command(label = "Effacer", command = lambda: canevas.delete(tkinter.ALL))
    barrePymobile.add_separator()
    barrePymobile.add_command(label = "Quitter", command = fenetre.quit)
    barre.add_cascade(label = "Pymobile", menu = barrePymobile)
    barreListe = tkinter.Menu(barre, tearoff = 0, activebackground = '#77B5FE')
    barreListe.add_command(label = "Éditer le fichier liste.txt", command = editerListe)
    barreListe.add_separator()
    barreListe.add_command(label = "Tracer le mobile (algorithme 1)", command = l1)
    barreListe.add_command(label = "Tracer le mobile (algorithme 2)", command = l2)
    barreListe.add_command(label = "Tracer le mobile (algorithme 3)", command = l3)
    barreListe.add_command(label = "Tracer le mobile (algorithme 4)", command = l4)
    barre.add_cascade(label = "Liste", menu = barreListe)
    barreArbre = tkinter.Menu(barre, tearoff = 0, activebackground = '#77B5FE')
    barreArbre.add_command(label = "Consulter le fichier sauvegarde.txt", command = consulterSauvegarde)
    barreArbre.add_separator()
    barreArbre.add_command(label = "Éditer le fichier arbre.txt", command = editerArbre)
    barreArbre.add_separator()
    barreArbre.add_command(label = "Tracer le mobile", command = a1)
    barre.add_cascade(label = "Arbre", menu = barreArbre)
    barreGenerateur = tkinter.Menu(barre, tearoff = 0, activebackground = '#77B5FE')
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur A (algorithme 1)", command = g1)
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur A (algorithme 2)", command = g2)
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur A (algorithme 3)", command = g3)
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur A (algorithme 4)", command = g4)
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur B", command = g5)
    barreGenerateur.add_command(label = "Tracer un mobile avec le générateur C", command = g6)
    barre.add_cascade(label = "Générateur", menu = barreGenerateur)
    fenetre.config(menu = barre)
    
    # Démarrage du réceptionnaire d'événements :
    fenetre.mainloop()
