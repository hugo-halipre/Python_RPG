

from _sauvegarde_ import *
from aide_jeu import *
from game import *


def sauvegarde(player):
    if player.nom == "zeph":
        player.race = "elfe"
        player.force = 8
        player.parade = 0.5
        player.max_pv = 120
        player.pv = player.max_pv
        player.bourse = 20000
        player.metier = "aventurier"
        for _ in range(20):
            objet.append("fruit démoniaque")
        for _ in range(7):
            objet.append("potion de vie")
        for i in range(20):
            objet.append(objet_possible[11+i])
            objet_bonus(player,objet_possible[11+i])

    if  player.nom == "Vava":
        player.race = "elfe"
        player.force = 8
        player.parade = 0.5
        player.max_pv = 120
        player.pv = player.max_pv
        player.metier = " "
    
    if  player.nom == "zephyr":
        player.race = "elfe"
        player.force = 8
        player.parade = 0.5
        player.max_pv = 120
        player.pv = player.max_pv
        player.metier = " "
        player.bourse = 2000
    
    if player.nom == "|Dieu|":
        reponse = input("mot de passe : ")
        if reponse == mot_de_passe:
            player.nom = "zephyr"
            player.force = 10000
            player.parade = 0.5
            player.max_pv = 100000
            player.pv = player.max_pv
            player.bourse = 1000000000
#            player.metier = "aventurier"
#            player.sauvegarde = 2
#            for i in range(len(objet_possible)):
#                objet.append(objet_possible[i])
#                objet_bonus(player,objet_possible[i])
#            for elt in succes_exite:
#                succes.append(elt)
            
        else:
            print("\033[31m\033[1mimposteur... OUSTE !\033[0m")
            player.nom = "Imposteur"
            player.race = "slime"
            player.force = 1
            player.parade = 1
            player.max_pv = 1
            player.pv = 1
            player.bourse = 0
            player.metier = "Tricheur !"



