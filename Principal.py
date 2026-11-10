###########################################################################################################################################################################################################
#
#
#                                                                                   Programme principal
#
#
###########################################################################################################################################################################################################

from game import *
from _sauvegarde_ import *
from aide_jeu import *
from jour_random import *
from scenario_aventurier import *
from scenario_chevalier import *
from scenario_mercenaire import *


def principal():
    """utilise les fonctions afin de créer le jeu"""
    jour = 1
    bienvenue()
    print("\nBonjour cher Joueur !")
    joueur = " "
    while len(joueur) < 3:
        joueur = input("Quel sera votre nom ? (3 lettres minimum)\n")
    if joueur not in nom_sauvegarde:
        print("Voici les races possibles : \n")
        print(" __________________________________________________________")
        print("|                                                          |")
        print("|       - Elfe      pv : 120 | force :  8 | parade : 0.5   |")
        print("|       - Nain      pv : 100 | force : 10 | parade : 1.0   |")
        print("|       - Humain    pv : 100 | force : 12 | parade : 0.5   |")
        print("|__________________________________________________________|\n")
        race_joueur = input("Quelle sera votre race ?\nAttention, le choix de la race aura une incidence sur le jeu !\n")
        race_joueur = race_joueur.lower()
        while race_joueur not in races:
            race_joueur = input("Quelle sera votre race ?\n")
        player = Personnage(name = joueur,race = race_joueur)
    else:
        player = Personnage(name = joueur,race = races[0])
        sauvegarde(player)
    if player.sauvegarde == 0:
        print("Bonjour" ,player.nom,"vous êtes un",player.race,"!\n")
        player.fiche_joueur()
        # | TEST |
        #jour_aventurier_donjon(player)
        #senario_aventurier(player,jour)
        print("Bonjour",player.nom,"\nVous vivez dans le royaume humain, au centre du continent.\nC'est le jour",jour,"!")
        sleep(1)
        jour_1(player)
        jour += 1
        while player.force < 25 :
            jour_general(player,jour)
            jour += 1
        while player.metier == " ":
            print("C'est le jour",jour,"! ")
            jour_metier(player)
            jour += 1
        player.sauvegarde += 1
    if player.metier == metier_possibles[0]:
        succes_exite.append("Aventurier rang S")
        senario_aventurier(player,jour)
        if player.metier == "aventurier (S)":
            succes_obtient()
            succes.append("Aventurier rang S")
    elif player.metier == metier_possibles[1]:
        succes_exite.append("Chevalier Saint")
        senario_mercenaire(player,jour)
    else:
        succes_exite.append("Assasin")
        senario_chevalier(player,jour)
    # FIN DU JEU 
    succes_obtient()
    print("Vous avez fini l'aventure !")
    succes.append("Aventure finie")
    if len(donjon_liste_fini) != len(donjon_liste):
            print("Allez, un dernière essaie pour finir les donjons !")
            donjon(player)
    fin_jeu(player)


###########################################################################################################################################################################################################


principal()


###########################################################################################################################################################################################################