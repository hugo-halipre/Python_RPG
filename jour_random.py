###########################################################################################################################################################################################################
#
#
#                                                                                 différents jours
#
#
###########################################################################################################################################################################################################

from time import sleep
from game import *

###########################################################################################################################################################################################################


def jour_1(player):
    """
    fonction qui lance le tout premier jour du jeux
    :param player: (class)
    """
    reponse = input("\n\nLe jour se lève, qu'allez-vous faire aujourd'hui ?\n 	- Combat ? --> Action fortement recomandée !\n")
    while reponse.lower() not in actions_possibles[:2]:
        print("")
        reponse = input("Qu'allez-vous faire ?\n 	- Combat ? --> Action fortement recommandée !\n")
    if reponse.lower() == "combat" or reponse.lower() == "c":
        monstre = 'slime'
        combat(monstre,player)
    print("Aller, on avance un peu...")
    sleep(2)
    print("Ohhhhh ! un gobelin ! Mais il y a aussi des plantes Rare...")
    reponse = input("Qu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?  --> Action fortement recomandée !\n")
    while reponse.lower() not in actions_possibles[:4]:
        reponse = input("Qu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?  --> Action fortement recomandée !\n")
    if reponse.lower() == "combat" or reponse.lower() == "c":
        monstre = 'gobelin'
        combat(monstre,player)
    elif reponse.lower() == "collecte" or reponse.lower() == "co":
        print("Vous décidez de vous concentrer sur la ceuillette et oubliez le gobelin")
        player.bourse = player.bourse + 50
        print("\nEn revendant votre butin vous rapporte beaucoup, vous gagnez \033[33m50\033[0m🪙  !\n")
    sleep(2)
    print("\nVous vous en êtes bien sorti pour un premier jour, maintenant direction une auberge...")
    sleep(2)
    print("Après plusieurs heures de recherche, vous trouvez enfin une auberge...")
    player.auberge()
    print("Allez, c'était une journée bien chargée... Demain sera peut-être plus tranquille ...")
    sleep(2)
    print("\n...zzzzzzzzzzzzzzzzzzzzzZZZZZZZZZZZZZ ATCHOUM !!! ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
 
    
def jour_general(player,jour):
    """
    fonction qui lance le jour de base
    :param player: (class)
    :param objet_achat: (tab)
    :param objet_achat_prix: (tab)
    """
    force_attaque = player.force
    print("C'est le jour",jour,"! ")
    for _ in range(2):
        sleep(1)
        reponse = " "
        while reponse.lower() not in actions_possibles[:6]:
            reponse = input("\nQu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?\n 	- Repos ?\n ")
        if reponse.lower() == 'combat' or reponse.lower() == 'c':
            monstre = choix_monstre(force_attaque)
            combat(monstre,player)
        elif reponse.lower() == 'collecte' or reponse.lower() == 'co':
            collecte(player)
        elif reponse.lower() == 'repos' or reponse.lower() == 'r':
            repos(player)
    sleep(1)
    reponse = " "
    while reponse.lower() not in actions_possibles:
        reponse = input("Qu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?\n 	- Repos ?\n 	- Shopping ?\n ")
    if reponse.lower() == 'combat' or reponse.lower() == 'c':
        monstre = choix_monstre(force_attaque)
        combat(monstre,player)
    elif reponse.lower() == 'collecte' or reponse.lower() == 'co':
        collecte(player)
    elif reponse.lower() == 'repos' or reponse.lower() == 'r':
        repos(player)
    elif reponse.lower() == 'shopping' or reponse.lower() == 's':
        boutique(player)
    print("retournons à l'auberge...")
    player.auberge()
   

def jour_metier(player):
    """
    fonction qui lance le jour du choix du métier
    :param player: (class)
    """
    force_attaque = player.force
    reponse = input("\n\nLe jour se lève, qu'allez-vous faire aujourd'hui ?\n 	- Combat ?\n 	- Collecte ?\n 	- Repos?\n")
    while reponse.lower() not in actions_possibles[:6]:
        reponse = input("Qu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?\n 	- repos?\n")
    if reponse.lower() == 'combat' or reponse.lower() == 'c':
        monstre = choix_monstre(force_attaque)
        combat(monstre,player)
    elif reponse.lower() == 'collecte' or reponse.lower() == 'co':
        collecte(player)
    elif reponse.lower() == 'repos' or reponse.lower() == 'r':
        repos(player)
    print("Ce serai bien de choisir un métier nan ?")
    metier = " "
    reponse = " "
    while metier not in metier_possibles:
        metier = input("Vous pouvez choisir entre 3 metiers :\n	- Aventurier \n	- Mercenaire\n	- Chevalier --> -100 🪙\n ")
        metier = metier.lower()
        while reponse not in choix_reponse:
            reponse = input("C'est un choix irréversible... êtes vous sur ?\n")
            reponse = reponse.lower()
    if reponse == "oui" or reponse == "o":
        if metier.lower() == 'aventurier':
            player.metier = 'aventurier'
        elif metier.lower() == 'mercenaire':
            player.metier = 'mercenaire'
        elif metier.lower() == 'chevalier':
            player.metier = 'chevalier'
            print("Vous payer 100 🪙 pour devenir Chevalier")
            player.bourse -= 100
    print("Vous êtes désormais un ",metier," !\n")
    player.fiche_joueur()
    print("allons a l'auberge maintenant... méditons sur notre choix de carrière maintenant.")
    player.auberge()


def jour_aventurier_general(player,niveau_aventurier,monstre = " "):
    force_attaque = player.force
    for _ in range(2):
        reponse = input("\n\nQu'allez-vous faire aujourd'hui ?\n 	- Combat ?\n 	- Collecte ?\n 	- Repos ?\n ")
        while reponse.lower() not in actions_possibles[:6]:
            reponse = input("Qu'allez-vous faire ?\n 	- Combat ?\n 	- Collecte ?\n 	- Repos ?\n ")
        if reponse.lower() == 'combat' or reponse.lower() == 'c':
            if monstre == " ":
                monstre = choix_monstre(force_attaque,niveau_aventurier)
            combat(monstre,player)
        elif reponse.lower() == 'collecte' or reponse.lower() == 'co':
            collecte(player)
        elif reponse.lower() == 'repos' or reponse.lower() == 'r':
            repos(player)
    print("Maintenant il est temps d'aller au combat !")
    monstre = choix_monstre(force_attaque,niveau_aventurier)
    combat(monstre,player)
    if niveau_aventurier < 4:
        print("Maintenant, directon l'auberge")
        player.auberge()
    

def jour_aventurier_nid(player,niveau_aventurier,monstre):
    for _ in range(6):
        combat(monstre,player)
    print("Vous avez fini avec tout ces ",monstre,"...")
    print("Un monstre plus fort arrive !")
    if monstre == "gobelin":
        boss = "Général gobelin"
        type = "|Boss|"
    if monstre == "orc":
        boss = "Général orc"
        type = "|Boss|"
    combat(boss,player,type)
    print("Bravo, vous avez réussi a battre tout une armée !")
    print("retournons à la guilde, c'est bien mérité")
    if ...:
        recompense_quete = randint(niveau_aventurier*10,niveau_aventurier*10+10)
        player.bourse + recompense_quete
        print("Vous avez rempli une mission, vous gagnez : ",recompense_quete,"🪙")
    if niveau_aventurier < 4:
        print("Maintenant, directon l'auberge")
        player.auberge()


def jour_aventurier_donjon(player):
    vie_depart = player.pv
    donjon = " "
    while donjon.lower() not in donjon_liste:
        print("\nliste des donjons :")
        for elt in donjon_liste:
            if elt not in donjon_liste_fini:
                print("  -",elt)
        print("")
        donjon = input("quel donjon choisisez-vous ? ")
        donjon = donjon.lower()
    creation_donjon = init_donjon(donjon)
    monstre = creation_donjon[0]
    boss = creation_donjon[1]
    objet_final = creation_donjon[3]
    type = "|Unique|"
    for _ in range(5):
        if not player.est_mort():
            combat_donjon(monstre,player,donjon)
    if not player.est_mort():
        print("Vous avez fini avec tout ces",monstre,"...")
        print("Un monstre plus fort arrive !")
        combat_donjon(boss,player,donjon,type)
        if not player.est_mort():
            print("Bravo, vous avez réussi a terminer le \033[1m\033[35mDonjon\033[0m !")
            sleep(2)
            recompense_quete = randint(gain[boss]*10,gain[boss]*10+10)
            player.bourse += recompense_quete
            print("Vous avez terminer un \033[1m\033[35mDonjon\033[0m, vous gagnez : \033[33m",recompense_quete,"\033[0m🪙 ")
            print("Vous obtenez l'objet \033[1m\033[35munique\033[0m du boss :\033[1m\033[35m",objet_final,"\033[0m")
            felicitation()
            objet.append(objet_final)
            objet_bonus(player,objet_final)
            donjon_liste_fini.append(donjon)
    else:
        print("Aïe... vous êtes mort...")
        sleep(2)
        print("\033[1m\033[97mPar les lois du donjon... TU REVIENS À LA VIE !\033[0m")
        sleep(2)
        print("C'est quand même dommage, un objet \033[1m\033[35munique\033[0m c'est bien... revenez plus tard")
    sleep(2)
    print("Vous récupérer votre vie d'avant")
    player.pv = vie_depart
    player.fiche_joueur()
    sleep(2)


def donjon(player):
    if len(donjon_liste_fini) < len(donjon_liste):
        reponse = " "
        player.fiche_joueur()
        while reponse not in choix_reponse:
            reponse = " "
            print("Rappel des règles du donjon \033[1m\033[35mDonjons\033[0m :")
            print(" - objet \033[1m\033[35mUnique\033[0m")
            print(" - mort non comptée")
            print(" - vie mise au maximum au début ")
            print("    ⚠️ (Uniquement dans le donjon)")
            reponse = input("\nVoulez vous tentez un donjon ? ")
        if reponse == "oui" or reponse == "o":
            jour_aventurier_donjon(player)
    if len(donjon_liste_fini) == len(donjon_liste):
        if "Maitre des donjons" not in succes:
            succes_obtient()
            succes.append("Maitre des donjons")
        print("Vous avez fini tout les donjons !")
        print("Il vous est donc impossible d'en refaire un.")
        print("Vous gagez \033[93m1000\033[0m🪙 en dédomagement\n")
        player.bourse += 1000
