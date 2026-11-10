###########################################################################################################################################################################################################
#
#
#                                                                                   scénario pour aventurier
#
#
###########################################################################################################################################################################################################

from game import *
from jour_random import *
from scenario_elfe import *
from scenario_humain import *
from scenario_nain import *

###########################################################################################################################################################################################################


def senario_aventurier(player,jour):
    niveau_aventurier = 1
    player.metier = metier_aventurier[niveau_aventurier]
    if player.sauvegarde == 1:
        print("Vous êtes un aventurier maintenant, un aventurier",player.race," !")
        print("Rendez-vous à la célèbre Guilde des Aventuriers ! De nouveaux contrats nous y attendent, et qui sait, peut-être une légende à écrire. Préparez vos lames, l'heure est venue de répondre à l'appel.")
        print("Une fois le formulaire rempli et votre inscription enregistrée.")    
        print("Vous êtes désormais un aventurier de rang D !")
        player.fiche_joueur()
        print("maintenant, il est temps de faire une nouvelle routine !")
        jour+=1
        jour_general(player,jour)
        jour+=1
        monstre = "orc"
        print("C'est le jour",jour,"! ")
        jour_aventurier_general(player,niveau_aventurier,monstre)
        sleep(2)
        print("Vous avez reussi votre première journée !")
        sleep(2)
        print("Bonus de 1ère journée : +\033[93m20\033[0m🪙")
        player.bourse += 20
        print("Vous avez maintenant : \033[93m",player.bourse,"\033[0m🪙")
        player.fiche_joueur()
        jour+=1
        for _ in range(5):
            jour_general(player,jour)
            jour+=1
            monstre = "gobelin"
            print("C'est le jour",jour,"! ")
            jour_aventurier_general(player,niveau_aventurier, monstre)
            jour+=1
        while player.force < 50 :
            jour_general(player,jour)
            jour+=1
            print("C'est le jour",jour,"! ")
            jour_aventurier_general(player,niveau_aventurier, monstre)
            jour+=1
        print("il y a eu beaucoup d'apparition de gobelin ces temps-ci...")
        sleep(2)
        print("La guilde vous envoies menée l'enquête, ils suspectent un nid de gobelin !")
        print("Vous vous préparez avant d'y allez.")
        boutique(player)
        print("Vous vous reposez avant d'allez enquéter.")
        if player.pv < player.max_pv and player.bourse >=10:
            player.bourse -= 10
            player.pv = player.max_pv
            print("Vous payer \033[93m10\033[0m🪙  et avez \033[92m",player.pv,"\033[0m !")
            print("Il vous reste \033[93m",player.bourse,"\033[0m🪙")
        sleep(4)
        jour+= 1
        print("C'est le jour",jour,"!\n")
        sleep(2)
        jour_aventurier_nid(player,niveau_aventurier,monstre)
        print("Vous avez battu le général gobelin et vous prenez son trésor")
        print("Vous trouvez un collier de général gobelin !")
        print("Vous gagnez \033[32m10\033[0m pv max et \033[91m5\033[0m points de forces.")
        objet.append("collier de général gobelin")
        objet_bonus(player,"collier de général gobelin")
        print("vous obtenez : ","\033[31mcollier de général gobelin\033[0m")
        player.fiche_joueur()
        monstre = " "
        jour+=1
        if niveau_aventurier+1 <=5:
            niveau_aventurier += 1
            player.metier = metier_aventurier[niveau_aventurier]
            print("Vous montez de rang !")
            print("Vous êtes maintenant au rang ",metier_aventurier[niveau_aventurier],"!")
            sleep(2)
        print("Vous pouvez maintenant accedez aux \033[1m\033[35mDonjons\033[0m :")
        sleep(1)
        print(" - objet \033[1m\033[35mUnique\033[0m")
        print(" - mort non comptée")
        print(" - vie mise au maximum au début ")
        print("    ⚠️ (Uniquement dans le donjon)")
        sleep(2)
        player.fiche_joueur()
        for _ in range(2):
            jour_general(player,jour)
            for _ in range(2):
                jour_aventurier_general(player,niveau_aventurier,monstre)
        print("Vous pouvez continuer l'aventure où tentez un donjon.")
        donjon(player)
        sleep(2)
        player.sauvegarde+=1
    if player.race == "elfe":
        senario_aventurier_elfe(player,niveau_aventurier,jour)
    elif player.race == "humain":
        senario_aventurier_humain(player,jour)
    else:
        senario_aventurier_nain(player,jour)
    for _ in range(5):
        jour_general(player,jour)
        for _ in range(2):
            jour_aventurier_general(player,niveau_aventurier,monstre)
            jour+=1
    print("Dans 10 jours, une expédition est prévu, vous et d'autres aventuriers partiront pour tuer le Drangon du chaos !")
    for _ in range(5):
        jour_general(player,jour)
        for _ in range(2):
            jour_aventurier_general(player,niveau_aventurier,monstre)
            jour+=1
    print("Il est temps...")
    
    print("Vous partez affronter le Dragon du chaos !")
    sleep(1)
    print("")
    if nom_monstre == " ":
        nom_monstre = str(monstre) + " " + type
    enemis = Personnage(nom_monstre,monstre)
    enemis.fiche_monstre()
    while enemis.est_mort() == False:
        sleep(1)
        tour_monstre(enemis,player)
        player.fiche_joueur(False)
        if player.est_mort():
            if ... :
                pass
            else:
                mort()
                fin_jeu(player)
                sys.exit()
        tour_joueur(enemis,player,0,0)
        enemis.fiche_monstre()
    print("Vous avez vaincu votre adversaire !")

    recompense_combat(player,monstre)
    print("Bravo, vous avez reussi a terasser le grand dragon du chaos !")
    print("Après tant d'épreuve ... il est temps de partir a la retraite...")
    sleep(2)
        
    