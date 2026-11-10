from time import sleep
from game import *

###########################################################################################################################################################################################################
#
#
#                                                                          Lieux spéciaux avec une mécanique différente
#
#
###########################################################################################################################################################################################################


def ancienne_capital_nain(player):
    print("Vous arrivez a l'entrée de l'ancienne capitale des nain, Umbralis...")
    print("Depuis la grande guerre entre les nains et les elfes,\nla capitale est désormée un lieu de guerre entre les 2 races qui ce dispute ce territoire")
    sleep(5)
    print("Ça sent le nain, l'odeur du métal et de la sueur...")
    sleep(5)
    choix = " "
    while choix != "explorer" and choix != "continuer":
        print("Vous trouvez une porte entrouverte. Soit vous entrez (mais vous ferez peut-être du bruit), soit vous continuez votre traversée.")
        choix = input("Que faire ?\n  - explorer\n  - continuer\n")
    if choix == "explorer":
        print("Vous decidez d'explorer...")
        sleep(3)
        print("Vous trouvez un coffre au tresors !")
        sleep(1)
        print("vous obtenez : ","\033[31mfruit démoniaque\033[0m")
        print("vous obtenez : ","\033[31mstatue héroique\033[0m")
        print("vous obtenez : ","\033[31m3 potion de vie\033[0m")
        print("Vous y trouvez \033[93m150\033[0m🪙  !")
        sleep(5)
        for _ in range(3):
            objet.append("potion de vie")
        objet.append("fruit démoniaque")
        objet.append("statue héroique")
        player.bourse += 50
        player.fiche_joueur()
        sleep(1)
        print("C'était une bonne idée !")
    else:
        print("Vous continuez votre chemin")
    sleep(5)
    print("Des nains déchus rodent dans les parages !")
    sleep(3)
    monstre = "nain"
    for _ in range(5):
        combat(monstre,player,type = 'déchus')
        sleep(1)
    print("Il y a un monstre qui bloque la porte pour sortir de l'ancienne capital ")
    print("C'est un Général orc ! ")
    monstre = "Général orc" 
    sleep(3)
    combat(monstre,player,type = "|Boss|", nom_monstre = "gardien de la porte")
    print("Après bien des épreuves, nous sommes sortis de l'ancienne capitale des nains, Umbralis.")
    sleep(2)


def terre_brulee(player):
    monstre = "crinière cendrée"
    for _ in range(10):
        combat(monstre,player)
        sleep(1)
    print("Après un long combat, vous en êtes sorti victorieux")
    print("Vous obtenez la cape cendrée !")
    objet.append("cape cendrée")
    objet_bonus(player,"cape cendrée")
    sleep(2)


def forêt_noire(player):
    monstre = "arbre corrompu"
    for _ in range(10):
        combat(monstre,player)
        sleep(1)
    print("Après un long combat, vous en êtes sorti victorieux")
    print("Vous obtenez la rose corrompu !")
    objet.append("rose corrompu")
    objet_bonus(player,"rose corrompu")
    sleep(2)


def montagne_du_nord(player):
    monstre = "yeti"
    for _ in range(10):
        combat(monstre,player)
        sleep(1)
    print("Après un long combat, vous en êtes sorti victorieux")
    print("Vous obtenez des poils de pied !")
    objet.append("poil de pied")
    objet_bonus(player,"poil de pied")
    sleep(2)

    