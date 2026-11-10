from time import sleep
from game import *
from jour_random import *
from lieu_event import *
from ASCII_art import *


###########################################################################################################################################################################################################
#
#
#                                                                                   scénarios métier si elfe
#
#
###########################################################################################################################################################################################################


def senario_aventurier_elfe(player,niveau_aventurier,jour):
    if player.sauvegarde == 2:
        print("Une lettre est arrivez ce matin...")
        sleep(2)
        print("Une nouvelle des plus terrible...")
        sleep(2)
        print("La grande forêt du royaume des elfes, ainsi que quelques villages, ont été brûlés par le feu du Roi des dragons...")
        sleep(2)
        print("Les elfes ont fait une demande d'aide aux humains et aux nains. Aucun ne souhaite se confronter au dragon.")
        reponse = input("Allez vous les aidez ?\n")
        reponse = reponse.lower()
        while reponse not in choix_reponse:
            reponse = input("Allez vous les aidez ?\n")
        if reponse == "non" or reponse == "n":
            print("Vous trouvez ça dangereux, vous restez où vous êtes")
            jour_general(player,jour)
            jour+= 1
            print("C'est le jour",jour,"! ")
            jour_aventurier_general(player,niveau_aventurier)
            sleep(3)
            print("Vous vous reveillez en hâte !")
            sleep(1)
            print("LE DRAGON EST LA !!!")
            sleep(3)
            monstre = "Dragon"
            dragon()
            combat(monstre,player,"|Sbire|")
            monstre = " "
            print("VOUS AVEZ BATTU LE DRAGON !!!")
            succes_obtient()
            succes.append("Dragon éliminé")
            print("Vous vous préparez a partir aider les elfes")
            sleep(1)
            print("les humains vous sont reconnaissant, ils vous donnent \033[93m1000\033[0m🪙  en cadeau pour votre courage !")
            player.bourse += 1000
            print("Vous avez maintenant\033[93m",player.bourse,"\033[0m🪙")
            print("La guilde des aventurier aussi vous félicite, vous gagnez un rang !")
            niveau_aventurier += 1
            player.metier = metier_aventurier[niveau_aventurier]
            print("Vous montez de rang !")
            print("Vous êtes maintenant au rang ",metier_aventurier[niveau_aventurier],"!")

        print("Vous partez les aidez !")
        sleep(2)
        print("Vous passez par les plaines pour rejoindre l'ancienne capitale des nains et enfin arriver au royaume elfe.")
        sleep(3)
        ancienne_capital_nain(player)
        jour += 1
        print("Vous avez passé une journée à traverser la capitale.")
        print("C'est le jour",jour)
        print("Pendant votre périple, un dragon est parti vers le royaume humain. Il a réduit en cendres une grande partie du royaume.")
        sleep(3)
        player.sauvegarde+=1
    if player.sauvegarde == 3:
        print("Vous arrivez enfin au royaume des elfes")
        print("Vous voyez le désastre que le dragon a fait au royaume...")
        print("les boutiques sont encores intactes :")
        reponse = " "
        while reponse not in choix_reponse:
            reponse = input("Avez vous des objets a vendre ?\n")
            reponse = reponse.lower()
            if reponse == "oui" or reponse == "o":
                vente(player)
        print("Vous avez \033[93m",player.bourse,"\033[0m🪙  , êtes vous une âme charitable ?")
        reponse = -1
        while reponse < 0 or reponse > player.bourse:
            reponse = input("Combien voulez vous donnez ?\n")
            try:
                argent_donne = int(reponse)
                reponse = int(reponse)
            except ValueError:
                print("Savez vous ce qu'est un nombre au moins ?")
                if "Nombre = lettre" not in succes:
                    succes.append("Nombre = lettre")
                    succes_obtient()
                reponse = -1
        donne_argent_ville(player,argent_donne,objet)
        player.fiche_joueur()
        sleep(3)
        if argent_donne >= 1000:
            print("Vous pouvez tentez votre chance dans un donjon grace au seigneur !")
            donjon(player)
        sleep(2)
        print("Maintenant que vous avez reussi a rebatir la ville, il y a des monstres au alentour qui rodes, a vous de jouer !")
        sleep(3)
        for _ in range(5):
            jour+=1
            jour_general(player,jour)
            for _ in range(2):
                jour+=1
                print("C'est le jour",jour,"! ")
                jour_aventurier_general(player,niveau_aventurier)
        print("il y a eu beaucoup d'orc au alentour de la ville")
        sleep(2)
        print("Ils y a une sucpition d'un nid d'orc !")
        print("Il faut ce préparez avant d'y allez")
        boutique(player)
        print("Vous vous reposez avant d'y allez")
        if player.pv < player.max_pv and player.bourse >=10:
            player.bourse -= 10
            player.pv = player.max_pv
            print("Vous payer \033[93m10\033[0m🪙  et avez \033[92m",player.pv,"\033[0m !")
            print("Il vous reste \033[93m",player.bourse,"\033[0m🪙")
        sleep(4)
        jour+= 1
        print("C'est le jour",jour,"!\n")
        sleep(2)
        monstre = "orc"
        jour_aventurier_nid(player,niveau_aventurier,monstre)
        print("Vous avez battu le général orc et vous prenez son trésor")
        print("Vous trouvez une massue de général orc !")
        print("Vous gagnez \033[32m10\033[0m pv max et \033[91m5\033[0m points de forces.")
        objet.append("massue de général orc")
        objet_bonus(player,"massue de général orc")
        print("vous obtenez : ","\033[31mmassue de général orc\033[0m")
        player.fiche_joueur()
        while player.bourse <= 700 or player.force < 100:
            jour+=1
            print("C'est le jour",jour,"! ")
            jour_aventurier_general(player,niveau_aventurier)
            for _ in range(2):
                jour+=1
                jour_general(player,jour)
        sleep(1)
        print("maintenant la ville est reconstruite, protégée et plus aucun monstre ne la menace.")
        niveau_aventurier += 1
        player.metier = metier_aventurier[niveau_aventurier]
        print("Vous montez de rang !")
        print("Vous êtes maintenant au rang ",metier_aventurier[niveau_aventurier],"!")
        print("Vous pouvez tentez votre chance dans le donjon si vous voulez")
        donjon(player)
        sleep(2)
        while player.bourse < 700 or player.force < 100 :
            jour+=1
            jour_general(player,jour)
            for _ in range(2):
                jour+=1
                print("C'est le jour",jour,"! ")
                jour_aventurier_general(player,niveau_aventurier, monstre)
        sleep(5)
        player.sauvegarde+=1
    if player.sauvegarde == 4:
        print("Des mouvements suspects ont étez signalez. Un dragon aurait élu domicile au sommet d'une montagne")
        print("Pour l'instant il n'as pas l'air de vouloir semé la destruction")
        reponse = " "
        while reponse not in choix_reponse:
            reponse = input("Allez vous allez le pourfendre ?\n")
            reponse = reponse.lower()
        if reponse == "oui" or reponse == "o":
            tuer_dragon(player,niveau_aventurier,jour)
        else:
            pas_tuer_dragon(player,niveau_aventurier,jour)
        print("La guilde a reconnu vos actions, le dragon n'est plus une menace grâce à vous, vous montez de rang !")
        niveau_aventurier += 1
        player.metier = metier_aventurier[niveau_aventurier]
        print("Vous êtes maintenant au rang ",metier_aventurier[niveau_aventurier],"!")
        print("Vous reprennez votre vie normal...")
        sleep(3)
        for _ in range(5):
            jour+=1
            print("C'est le jour",jour,"!")
            jour_aventurier_general(player,niveau_aventurier, monstre)
            for _ in range(2):
                jour+=1
                jour_general(player,jour)
        player.sauvegarde+=1
    if player.sauvegarde == 5:
        print("Il est tant de partir pour une expédition mandatée par la guilde")
        print("vous avez le choix entre plusieurs éxpéditions possibles :")
        print(" - 1   Terre brulée")
        print(" - 2   Forêt noire")
        print(" - 3   Montagne du nord")
        reponse = " "
        reponse_expedition = ["Terre brulée","Forêt noire","Montagne du nord"]
        while reponse not in reponse_expedition:
            reponse = input("Ou allez vous ?").lower()
            if reponse == "terre brulée":
                terre_brulee(player)
                print("D'autres aventurier ce sont occupées de la montagne du nord... ")
                print("Vous partez donc demain pour la forêt noire.")
                player.auberge()
                jour+=1
                forêt_noire(player)
            if reponse == "forêt noire":
                forêt_noire(player)
                print("D'autres aventurier ce sont occupées de la terre brulée... ")
                print("Vous partez donc demain pour la montagne du nord.")
                jour+=1
                player.auberge()
                montagne_du_nord(player)
            if reponse == "montagne du nord":
                montagne_du_nord(player)
                print("D'autres aventurier ce sont occupées de la forêt noire... ")
                print("Vous partez donc demain pour la terre brulée.")
                jour+=1
                player.auberge()
                terre_brulee(player)
        if niveau_aventurier+1 <=5:
            niveau_aventurier += 1
            player.metier = metier_aventurier[niveau_aventurier]
            print("Vous montez de rang !")
            print("Vous êtes maintenant au rang ",metier_aventurier[niveau_aventurier],"!")
            sleep(2)
        print("il est temps de vous reposez")
        jour+=1
        player.auberge()
        donjon(player)


        

        
            

################################################################################################################################################


def donne_argent_ville(player,argent_donne,objet):
    if argent_donne == 0:
        print("Vous ne donnez rien...")
    elif argent_donne > 0 and argent_donne < 250:
        print("Vous permettez de rebattir une partie de la ville !")
        print("les villagois vous donnent en remerciment :")
        sleep(1)
        print(" - 5 potions de vie")
        for _ in range(5):
            objet.append("potion de vie")
    elif argent_donne >= 250 and argent_donne < 500:
        print("Vous permettez la ville !")
        print("les villagois vous donnent en remerciment :")
        sleep(1)
        print(" - 5 potions de vie")
        print(" - 5 potions de puissance")
        for _ in range(5):
            objet.append("potion de vie")
            objet.append("potion de puissance")
    elif argent_donne >= 500 and argent_donne < 1000:
        print("Vous permettez de rebattir la ville et de renforcer les déffences !")
        print("les villagois et quelques soldats vous donnent en remerciment :")
        sleep(1)
        print(" - 10 potions de vie")
        print(" - 10 potions de puissance")
        print(" - 1 fruit démoniaque")
        for _ in range(10):
            objet.append("potion de vie")
            objet.append("potion de puissance")
        objet.append("fruit démoniaque")
    elif argent_donne >= 1000 :
        print("Vous permettez une reconstruction totale de la ville et même sont expansion !")
        print("Le seigneur vous donne en remerciment :")
        sleep(1)
        print(" - 10 potions de vie")
        print(" - 10 potions de puissance")
        print(" - 1 fruit démoniaque")
        print(" - \033[1m\033[35ml'orbe elfique\033[0m ")
        for _ in range(10):
            objet.append("potion de vie")
            objet.append("potion de puissance")
        objet.append("fruit démoniaque")
        objet.append("orbe elfique")
        objet_bonus(player,"orbe elfique")
        succes_obtient()
        succes.append("Âme charitable")
    player.bourse -= argent_donne
        
    
def tuer_dragon(player,niveau_aventurier,jour):
    monstre = " "
    print("Vous partez pour le tuer")
    for _ in range(5):
        jour+=1
        print("C'est le jour",jour,"! ")
        jour_aventurier_general(player,niveau_aventurier, monstre)
    print("Vous arrivez au pied de la montage")
    sleep(2)
    print("Au sommet ce trouve le dragon")
    sleep(5)
    print("Vous entrez dans son antre...")
    sleep(2)
    print("C'est une dragonne qui porte en elle un bébé dragon !")
    reponse = " "
    while reponse not in choix_reponse:
        reponse = input("Allez vous les tuez ?\n")
        reponse = reponse.lower()
        if reponse == "oui" or reponse == "o":
            combat_dragon(player)
        else:
            combat_dragon(player,False)
    sleep(3)
            

def pas_tuer_dragon(player,niveau_aventurier,jour):
    monstre = " "
    print("Vous decidez de ne pas tuer le dragon")
    for _ in range(5):
        jour+=1
        jour_general(player,jour)
        for _ in range(2):
            jour+=1
            print("C'est le jour",jour,"! ")
            jour_aventurier_general(player,niveau_aventurier, monstre)
    sleep(3)
    print("Le dragon vient detruire les villages alentour !")
    print("Il y a aussi un dragon assez jeune !")
    sleep(3)
    combat(monstre,player,type = "mère", nom_monstre = "Dragon de la montagne")
    combat(monstre,player,type = "enfant", nom_monstre = "Dragon de la montagne")
    print("Vous avez essuiez des dégats mais vous avez reussi a survivre ")
    sleep(3)
    print("Vous obtenez un coeur démoniaque pour votre cruauté au combat malgré votre héroisme")
    print("Vous gagnez \033[91m100\033[0m points de force")
    objet.append("coeur démoniaque")
    objet_bonus(player,"coeur démoniaque")


def combat_dragon(player,bebe_dragon = True):
    monstre = "Dragon"
    if bebe_dragon:
        combat(monstre,player,type = "enceinte", nom_monstre = "Dragon de la montagne")
        sleep(3)
        print("Ces dur mais vous tuez le bébé dragon...")
        print("Vous obtenez un coeur démoniaque pour votre cruauté")
        print("Vous gagnez \033[91m100\033[0m points de force")
        objet.append("coeur démoniaque")
        objet_bonus(player,"coeur démoniaque")
        sleep(3)
    else:
        print("Vous decidez finalement de ne pas les tuez")
        sleep(3)
        print("Le dragon vous remarque et vous est reconnaissant de ne pas mettre fin a la vie de son enfant")
        print("Vous obtenez un coeur angelique pour votre bonté")
        print("Vous gagnez \033[92m100\033[0m pv max")
        objet.append("coeur angelique")
        objet_bonus(player,"coeur angelique")
        sleep(3)
        