###########################################################################################################################################################################################################
###########################################################################################################################################################################################################
##
##
##                                                                                       ~~  La grande aventure  ~~
##
##                                                            
##                                                                créé pour :
##                                                                          - s'amuser
##                                                                          - le kiff
##                                                                          - s'entrainer a phython
##
###########################################################################################################################################################################################################
###########################################################################################################################################################################################################


import sys
from time import sleep
from random import randint
from aide_jeu import *
from ASCII_art import *



###########################################################################################################################################################################################################
#
#
#                                                                             listes utilisées dans les fonctions du programme
#
#
###########################################################################################################################################################################################################

nom_sauvegarde = ["Vava","zeph","|Dieu|","zephyr"]

races =        ["elfe"     ,"nain"     ,"humain"     ,"gobelin"     ,"orc"     ,"gnoll"    ,"slime"     ,"golem"     ,"hobgobelin"     ,"elfe noir"     ,"scolopendre"     ,"crinière cendrée"     ,"arbre corrompu"     ,"yeti"     ,"Général gobelin"     ,"Général orc"     ,"Géant"     ,"Hydre"    ,"Dragon"      ,"Roi hobgobelin"     ,"Seigneur Boucher"     ,"Monolithe"     ,"Mégalodon"      ,"Dragon du chaos"]
gain =         {"elfe" : 5 ,"nain": 5  ,"humain": 5  ,"gobelin": 1  ,"orc": 2  ,"gnoll": 1 ,"slime": 1  ,"golem": 2  ,"hobgobelin": 2  ,"elfe noir": 3  ,"scolopendre": 3  ,"crinière cendrée": 4  ,"arbre corrompu": 4  ,"yeti": 4  ,"Général gobelin": 5  ,"Général orc": 6  ,"Géant": 9  ,"Hydre":12 ,"Dragon": 15  ,"Roi hobgobelin": 5  ,"Seigneur Boucher": 8  ,"Monolithe": 10 ,"Mégalodon": 20  ,"Dragon du chaos": 100} 
forces =       {"elfe" : 8 ,"nain": 10 ,"humain": 12 ,"gobelin": 5  ,"orc": 12 ,"gnoll": 8 ,"slime": 1  ,"golem": 15 ,"hobgobelin": 15 ,"elfe noir": 20 ,"scolopendre": 15 ,"crinière cendrée": 20 ,"arbre corrompu": 20 ,"yeti": 20 ,"Général gobelin": 30 ,"Général orc": 30 ,"Géant": 60 ,"Hydre":75 ,"Dragon": 100 ,"Roi hobgobelin": 50 ,"Seigneur Boucher": 70 ,"Monolithe": 10 ,"Mégalodon": 150 ,"Dragon du chaos": 250} 
parades =      {"elfe": 0.5,"nain": 0.5,"humain": 1.0,"gobelin": 0.5,"orc": 1.0,"gnoll": 1 ,"slime": 2.0,"golem": 0.5,"hobgobelin": 1.0,"elfe noir": 1.0,"scolopendre": 1.0,"crinière cendrée": 1.0,"arbre corrompu": 1.0,"yeti": 1.0,"Général gobelin": 2.0,"Général orc": 1.0,"Géant": 1.0,"Hydre":1.0,"Dragon": 1.0 ,"Roi hobgobelin": 1.0,"Seigneur Boucher": 2.0,"Monolithe": 0.1,"Mégalodon": 0.5 ,"Dragon du chaos": 0.1 }
point_de_vie = {"elfe": 120,"nain": 100,"humain": 100,"gobelin": 15 ,"orc": 50 ,"gnoll": 20,"slime": 5  ,"golem": 50 ,"hobgobelin": 75 ,"elfe noir": 75 ,"scolopendre": 100,"crinière cendrée": 200,"arbre corrompu": 200,"yeti": 200,"Général gobelin": 150,"Général orc": 100,"Géant": 250,"Hydre":500,"Dragon": 1000,"Roi hobgobelin": 200,"Seigneur Boucher": 400,"Monolithe": 500,"Mégalodon": 1000,"Dragon du chaos": 5000}

donjon_liste_fini = []
donjon_liste =   ["donjon gobelin"        ,"terre orcs"     ,"tombeau de géant"    ,"abysses éternel"     ,"volcan impérial"]
objet_donjon =   ["couronne du roi Cupide","croc du Boucher","Coeur de la Montagne","Écaille du Prédateur","Épée Dragonicide"]
objet_special =  ["collier de général gobelin","massue de général orc","orbe elfique","coeur démoniaque","coeur angelique","boite porte bonheur"]
objet_nom_cumulable =                                                                                                                                                                                                                   ["épée","casque","armure","bouclier","épée+","casque+","armure+","bouclier+","épée++","casque++","armure++","bouclier++","épée runique","épée ancestrale","casque runique","casque ancestrale","armure runique","armure ancestrale","bouclier runique","bouclier ancestrale","coeur démoniaque","coeur angelique","collier de général gobelin","massue de général orc","orbe elfique","boite porte bonheur","cape cendrée","rose corrompu","poil de pied","couronne du roi Cupide","croc du Boucher","Coeur de la Montagne","Écaille du Prédateur","Épée Dragonicide"]
objet_consomable =  ["potion de vie","potion de vie supérieure","potion de vie ultime","potion de sacrifice","potion de puissance","acide de slime","dague de gobelin","croc de gnoll","lame d'orc","fruit démoniaque","statue héroique"]
objet_possible =    ["potion de vie","potion de vie supérieure","potion de vie ultime","potion de sacrifice","potion de puissance","acide de slime","dague de gobelin","croc de gnoll","lame d'orc","fruit démoniaque","statue héroique","épée","casque","armure","bouclier","épée+","casque+","armure+","bouclier+","épée++","casque++","armure++","bouclier++","épée runique","épée ancestrale","casque runique","casque ancestrale","armure runique","armure ancestrale","bouclier runique","bouclier ancestrale","coeur démoniaque","coeur angelique","collier de général gobelin","massue de général orc","orbe elfique","boite porte bonheur","cape cendrée","rose corrompu","poil de pied","couronne du roi Cupide","croc du Boucher","Coeur de la Montagne","Écaille du Prédateur","Épée Dragonicide"]
boite_gacha =      ["commune"   ,"rare"    ,"mystère"    ,"épique"    ,"ultime"]
boite_gacha_prix = {"commune":50,"rare":500,"mystère":500,"épique":750,"ultime":1000}

# 0 potion de vie
# 1 potion de vie supérieure
# 2 potion de vie ultime
# 3 potion de sacrifice
# 4 potion de puissance
# 5 acide de slime
# 6 dague de gobelin
# 7 croc de gnoll
# 8 lame d'orc
# 9 fruit démoniaque
# 10 statue héroique
# 11 épée
# 12 casque
# 13 armure
# 14 bouclier
# 15 épée+
# 16 casque+
# 17 armure+
# 18 bouclier+
# 19 épée++
# 20 casque++
# 21 armure++
# 22 bouclier++
# 23 épée runique
# 24 épée ancestrale
# 25 casque runique
# 26 casque ancestrale
# 27 armure runique
# 28 armure ancestrale
# 29 bouclier runique
# 30 bouclier ancestrale
# 31 coeur démoniaque
# 32 coeur angelique
# 33 collier de général gobelin
# 34 massue de général orc
# 35 orbe elfique
# 36 boite porte bonheur
# 37 couronne du roi Cupide
# 38 croc du Boucher
# 39 Coeur de la Montagne
# 40 Écaille du Prédateur
# 41 Épée Dragonicide


marcher_noir =      ["coeur démoniaque"     ,"coeur angelique"]
marcher_noir_prix = {"coeur démoniaque":1000,"coeur angelique":1000}
objet_achat =      ["potion de vie"      ,"potion de vie supérieure"    ,"potion de vie ultime"    ,"potion de puissance"     ,"dague de gobelin"     ,"épée"      ,"casque"      ,"armure"      ,"bouclier"     ,"épée+"     ,"casque+"    ,"armure+"    ,"bouclier+"    ,"épée++"     ,"casque++"    ,"armure++"    ,"bouclier++"    ,"épée runique"    ,"casque runique"    ,"armure runique"    ,"bouclier runique"    ,"épée ancestrale"     ,"casque ancestrale"     ,"armure ancestrale"     ,"bouclier ancestrale"]
objet_achat_prix = {"potion de vie" : 20 ,"potion de vie supérieure":90 ,"potion de vie ultime":500,"potion de puissance": 30 ,"dague de gobelin":20  ,"épée": 100 ,"casque": 125 ,"armure": 125 ,"bouclier": 150,"épée+": 200,"casque+":250,"armure+":250,"bouclier+":300,"épée++": 400,"casque++":500,"armure++":500,"bouclier++":600,"épée runique":600,"casque runique":700,"armure runique":700,"bouclier runique":800,"épée ancestrale":1000,"casque ancestrale":1100,"armure ancestrale":1100,"bouclier ancestrale":1200}
objet_vente_prix = {"potion de vie" : 10 ,"potion de vie supérieure":50 ,"potion de vie ultime":250,"potion de sacrifice": 10 ,"potion de puissance":20,"acide de slime":10,"dague de gobelin":10,"croc de gnoll":20,"lame d'orc":30,"fruit démoniaque": 200,"statue héroique":200}
equipement =   ["épée","épée+","épée++","casque","casque+","casque++","armure","armure+","armure++","bouclier","bouclier+","bouclier++","épée runique","casque runique","armure runique","bouclier runique","épée ancestrale","casque ancestrale","armure ancestrale","bouclier ancestrale"]
tab_epee =     ["épée"    ,"épée+"    ,"épée++"    ,"épée runique"    ,"épée ancestrale"    ]
tab_casque =   ["casque"  ,"casque+"  ,"casque++"  ,"casque runique"  ,"casque ancestrale"  ]
tab_armure =   ["armure"  ,"armure+"  ,"armure++"  ,"armure runique"  ,"armure ancestrale"  ] 
tab_bouclier = ["bouclier","bouclier+","bouclier++","bouclier runique","bouclier ancestrale"]


objet = ["potion de vie","potion de vie","potion de vie supérieure","potion de sacrifice","potion de puissance"]


metier_possibles =["aventurier","mercenaire","chevalier"]
metier_aventurier = ["aventurier","aventurier (D)","aventurier (C)","aventurier (B)","aventurier (A)","aventurier (S)"]

metier = " "

actions_possibles =["combat","c","collecte","co","repos","r","shopping","s"]
actions_combat_possibles = ["attaquer","a","blesser","b","doper","d","objet","o","fiche joueur","f"]

succes_speciaux = ["Aventurier rang S","Chevalier Saint","Assasin"]
succes_exite = ["Aventure finie"       ,"Dragon éliminé"      ,"Maitre des donjons"       ,"Âme charitable"      ,"Destructeur d'économie"       ,"Fou de gâcha"      ,"Quitte ou double !"      ,"Nombre = lettre"      ,"Armement lourd"]
icone_succes = {"Aventure finie":"⚔️ ","Dragon éliminé":"⚔️ ","Maitre des donjons":"⚔️ ","Âme charitable":"🪙 ","Destructeur d'économie":"🪙 ", "Fou de gâcha":"📦","Quitte ou double !":"📦","Nombre = lettre":"⁉️ ","Armement lourd":"⭐","Aventurier rang S":"📜","Chevalier Saint":"📜","Assasin":"📜"}
succes = []

choix_reponse = ["oui","o","non","n"]
###########################################################################################################################################################################################################
#
#
#                                                                             Classe permettant la création des personnages
#
#
###########################################################################################################################################################################################################

class Personnage :
    "créé les mob et le joueur"
    def __init__(self,name,race):
        "crée les différents paramètres"
        self.nom = name
        self.race = race
        self.force = forces[race]
        self.parade = parades[race]
        self.max_pv = point_de_vie[race]
        self.pv = self.max_pv
        self.bourse = 100
        self.metier = metier
        self.sauvegarde = 0
    
    
    def est_mort(self):
        """verification de l'etat de l'objet (mort/vivant)"""
        return self.pv <=0
    
    
    def blesser(self,adversaire):
        """action de blesser l'adversaire
        adversaire : class(objet)
        """
        resultat = randint(0,2)
        if resultat == 0:
            adversaire.pv = adversaire.pv - int(self.force *1.5)
            if adversaire.pv < 0:
                adversaire.pv = 0
        else:
            adversaire.pv = adversaire.pv - int(self.force *adversaire.parade)
            if adversaire.pv < 0:
                adversaire.pv = 0
        
        
    def attaquer(self,adversaire):
        """action d'attaquer l'adversaire
        adversaire : class(objet)
        """
        blessure = randint(self.force//2,self.force+self.force//4)
        adversaire.pv = adversaire.pv - blessure
        if adversaire.pv < 0:
            adversaire.pv = 0
    
    
    def booster(self,vie_en_moins,force_en_plus):
        """action de dopage du joueurr
        vie_en_moins : (int)
        force_en_plus : (int)
        """
        self.pv = self.pv - 5
        self.force = self.force + 1
        vie_en_moins += 10
        force_en_plus += 1
        
        
    def contre_booster(self,vie_en_moins,force_en_plus):
        """mesure d'après dopage du joueur
        vie_en_moins : (int)
        force_en_plus : (int)
        """
        self.pv = self.pv + vie_en_moins
        self.force = self.force - force_en_plus
        
        
    def objet(self,adversaire):
        print("Voici vos objets : ")
        objet_posseder(objet,False)
        reponse = " "
        effet = 0
        while reponse.lower() not in objet :
            reponse = input("Quel objet voulez-vous utiliser ? ")
        if reponse in objet_consomable:
            nombre = 0
            nombre_possede = objet.count(reponse)
            while nombre <= 0:
                saisi_nombre = input("Combien voulez vous utilisez de "+reponse+" ?\n")
                try:
                    nombre = int(saisi_nombre)
                except ValueError:
                    print("Savez vous ce qu'est un nombre au moin ?")
                    if "Nombre = lettre" not in succes:
                        succes.append("Nombre = lettre")
                        succes_obtient()
                    nombre = 0
        if nombre > nombre_possede:
            nombre = nombre_possede
        if reponse == "potion de vie":
            for _ in range(nombre):
                self.pv = min(self.pv + 20, self.max_pv)
            print("Vous utilisez ",nombre,reponse," vous avez :\033[32m",self.pv,"\033[0m !")
        if reponse == "potion de vie supérieure":
            for _ in range(nombre):
                self.pv = min(self.pv + 100, self.max_pv)
            print("Vous utilisez ",nombre,reponse," vous avez :\033[32m",self.pv,"\033[0m !")
        if reponse == "potion de vie ultime":
            for _ in range(nombre):
                self.pv = self.max_pv
            print("Vous utilisez ",nombre,reponse," vous avez :\033[32m",self.pv,"\033[0m !")
        elif reponse == "potion de sacrifice":
            for _ in range(nombre):
                self.force += 1
                self.pv -= 10
                if self.pv < 0:
                    self.pv = 0
            if self.pv == 0:
                print("Vous mourrez d'une overdose !")
                print("\033[1mLa honte\033[0m")
                mort()
                fin_jeu(self)
                sys.exit()
            else:
                print("Vous utilisez ",nombre," potion de sacrifice, vous avez :\033[32m",self.pv,"pv\033[0m et vous avez :\033[91m",self.force,"\033[0m en force.")
        elif reponse == "potion de puissance":
            self.force += nombre
            print("Vous gagnez \033[31m",nombre,"\033[0m point de force, vous avez :\033[31m",self.force,"\033[0m")
        elif reponse == "acide de slime":
            for _ in range(nombre):
                effet += randint(2, 10)
            adversaire.pv -= effet
            print("L'adversaire perd \033[32m",effet,"\033[0m pv.")
        elif reponse == "dague de gobelin":
            adversaire.pv -= nombre * 5
            print("L'adversaire perd \033[32m",effet,"\033[0m pv.")
        elif reponse == "croc de gnoll":
            adversaire.pv -= nombre * 10
            print("L'adversaire perd \033[32m",effet,"\033[0m pv.")
        elif reponse == "lame d'orc":
            adversaire.pv -= nombre * 15
            print("L'adversaire perd \033[32m",effet,"\033[0m pv.")
        elif reponse == "fruit démoniaque":
            for _ in range(nombre):
                adversaire.pv //= 2 
            print("L'adversaire n'a plus que \033[32m",adversaire.pv,"\033[0m pv !")
        elif reponse == "statue héroique":
            for _ in range(nombre):
                effet += randint(2, 10)
            self.force += effet
        if adversaire.pv < 0:
            adversaire.pv = 0
        for _ in range(nombre):
            objet.remove(reponse)
        if len(objet) > 0:
            print("\nIl vous reste des objets :")
            objet_posseder(objet, False)
        else:
            print("\nVotre inventaire est maintenant vide.")
        
    
    def recuperer_vie(self):
        """action de repos, donne des points de vie"""
        pv_plus = randint(5,15)
        self.pv = min(self.pv + 20, self.max_pv)

        print("vous faites une petite sieste, ...")        
        print("vous avez :\033[32m",self.pv,"pv\033[0m !")
        if self.pv == self.max_pv:
            print("⚠️  Votre vie est a son maximum. ⚠️")
            
            
    def gagner_argent(self,minimum,maximum):
        """permet de gagner de l'argent"""
        argent = randint(minimum,maximum)
        if "boite porte bonheur" in objet:
            print("La chance est avec vous !")
            argent += argent//2
        self.bourse = self.bourse + argent
        print("Vous gagnez :","\033[33m",argent,"\033[0m","🪙  !")
        if self.bourse >= 10000 and "Destructeur d'économie" not in succes:
            succes_obtient()
            print("Vous avez détruit l'économie !\n")
            succes.append("Destructeur d'économie")
        
    
    def auberge(self):
        """action obligatoire(sauf exeption) de fin de journée"""
        if self.bourse -10 >= 0:
            self.bourse -=10
            print("\nVous payez l'auberge \033[33m10\033[0m🪙  , il vous reste :","\033[33m",self.bourse,"\033[0m🪙")
            pv_en_plus = int(self.max_pv/4)
            self.pv += pv_en_plus
            if self.pv > self.max_pv:
                self.pv = self.max_pv
            print("Vous récupérez \033[32m",pv_en_plus,"pv\033[0m\nvous avez :","\033[32m",self.pv,"pv\033[0m\n")
        else:
            print("Le prix de l'auberge est de \033[33m10\033[0m🪙  , Vous ne pouvez pas y dormir...")
            print("Vous êtes a la rue...")
            print("Vous perdez \033[32m10 pv\033[0m ")
            self.pv -= 10
            if self.pv < 0:
                print("Vous êtes mort dans la rue !")
                print("\033[1mLa honte\033[0m")
                mort()
                fin_jeu(self)
                sys.exit()
            else:
                print("Il vous reste\033[92m",self.pv,"pv\033[0m")

    
    def fiche_joueur(self,affiche_tout = True):
        """Affichage des caractéristiques du joueur"""
        force = self.force
        grade_race = grade(force)
        print("\n--------------------------------")
        print("        >--- JOUEUR ---<")
        print("--------------------------------")
        print(" nom  : ","\033[1m",self.nom,"\033[0m")
        print(" race : ","\033[1m",grade_race,self.race,"\033[0m")
        print("--------------------------------")
        print(" force        : ","\033[91m",self.force,"\033[0m")
        print(" parade       : ","\033[36m",self.parade,"\033[0m")
        print(" pv max       : ","\033[92m",self.max_pv,"\033[0m")
        print(" point de vie : ","\033[92m",self.pv,"\033[0m")
        print(" bourse       : ","\033[93m",self.bourse,"\033[0m🪙")
        print(" métier       : ","\033[93m",self.metier,"\033[0m")
        objet_posseder(objet,affiche_tout)
    
    
    def fiche_monstre(self):
        if self.pv < 0:
            self.pv = 0
        """Affichage des caractéristiques des monstres"""
        print("\n---------------------------------")
        print("        >--- MONSTRE ---<")
        print("---------------------------------")
        print(" nom  : ","\033[1m",self.nom,"\033[0m")
        print(" race : ","\033[1m",self.race,"\033[0m")
        print("---------------------------------")
        print(" force        : ","\033[91m",self.force,"\033[0m")
        print(" parade       : ","\033[36m",self.parade,"\033[0m")
        print(" point de vie : ","\033[92m",self.pv,"\033[0m")
        print("---------------------------------\n")
    

###########################################################################################################################################################################################################
#
#
#                                                                                       gestion des combats
#
#
###########################################################################################################################################################################################################


def combat(monstre,player,type = "sauvage", nom_monstre = " "):
    vie_en_moins = 0
    force_en_plus = 0
    print("Un enemi apparaît, un",monstre,"!")
    if nom_monstre == " ":
        nom_monstre = str(monstre) + " " + type
    enemis = Personnage(nom_monstre,monstre)
    enemis.fiche_monstre()
    while enemis.est_mort() == False:
        sleep(1)
        tour_monstre(enemis,player)
        player.fiche_joueur(False)
        if player.est_mort():
            mort()
            fin_jeu(player)
            sys.exit()
        tour_joueur(enemis,player,vie_en_moins,force_en_plus)
        enemis.fiche_monstre()
    print("Vous avez vaincu votre adversaire !")
    if vie_en_moins > 0:
        player.contre_booster(vie_en_moins,force_en_plus)
        print("L'effet du dopage est terminé, vous avez à présent :\n	-force :",player.force,"\n	-pv :",player.pv)
    recompense_combat(player,monstre)


def tour_joueur(enemis,player,vie_en_moins,force_en_plus):
    reponse = input("Quelle action faites-vous ?\n	- attaquer ?\n	- blesser ?\n	- booster ?\n	- objet?\n	- fiche joueur?\n ")
    while reponse not in actions_combat_possibles:
        reponse = input("Quelle action faites-vous ?\n	- attaquer ?\n	- blesser ?\n	- booster ?\n	- objet?\n	- fiche joueur?\n ")
    if reponse.lower() == 'attaquer' or reponse.lower() == 'a':
        print("Vous attaquez !")
        player.attaquer(enemis)
    elif reponse.lower() == 'blesser' or reponse.lower() == 'b':
        print("Vous tentez de blesser le monstre !")
        player.blesser(enemis)
    elif reponse.lower() == 'booster'or reponse.lower() == 'd':
        print("Vous vous dopez !")
        player.booster(vie_en_moins,force_en_plus)
    elif reponse.lower() == 'objet' or reponse.lower() == 'o':
        if len(objet) == 0:
            print("Vous n'avez aucun objet !")
            tour_joueur(enemis,player,vie_en_moins,force_en_plus)
        else:
            player.objet(enemis)
            if enemis.est_mort() == False:
                tour_joueur(enemis,player,vie_en_moins,force_en_plus)
    elif reponse.lower() == 'fiche joueur' or  reponse.lower() == 'f':
        player.fiche_joueur()
        tour_joueur(enemis,player,vie_en_moins,force_en_plus)


def tour_monstre(enemis,player):
    resultat = randint(1,10)
    if resultat >7:
        print("Le monstre attaque !")
        enemis.attaquer(player)
    else:
        print("Le monstre veut vous blesser !")
        enemis.blesser(player)    
        
        
def choix_monstre(force_attaque,est_aventurier = 1):
    niv_monstre = choix_monstre_puissance(force_attaque,est_aventurier)
    if niv_monstre <= 3:
        return "slime"
    elif 3 < niv_monstre <= 6:
        return "gobelin"
    elif 6 < niv_monstre <= 9:
        return "gnoll"
    elif 9 < niv_monstre <= 12:
        return "orc"
    elif 12 < niv_monstre <= 15:
        return "golem"
    elif 15 < niv_monstre <= 18:
        return "hobgobelin"
    elif 18 < niv_monstre <= 21:
        return "elfe noir"
    elif 21 < niv_monstre <= 24:
        return "scolopendre"
    elif 24 < niv_monstre <= 27:
        return "Général gobelin"
    elif 27 < niv_monstre <= 30:
        return "Général orc"
    elif 30 < niv_monstre <= 33:
        return "Roi hobgobelin"
    elif 33 < niv_monstre <= 36:
        return "Géant"
    elif 36 < niv_monstre <= 39:
        return "Géant"
    elif 39 < niv_monstre:
        return "Seigneur Boucher"
    

def choix_monstre_puissance(force_attaque,est_aventurier):
    niv_monstre = randint(-1 ,10) + est_aventurier*2-1
    if force_attaque >= 200:
        niv_monstre += 20
    elif force_attaque >= 100:
        niv_monstre += 15
    elif force_attaque >= 50:
        niv_monstre += 10
    elif force_attaque >= 25:
        niv_monstre += 5
    return niv_monstre


def recompense_combat(player,monstre):
    min = gain[monstre] * 10
    max = min + 10
    player.gagner_argent(min,max)
    print("Vous avez :\033[93m",player.bourse,"\033[0m🪙")
    gagner_objet(player,monstre)
    

###########################################################################################################################################################################################################
#
#
#                                                                                        création des Donjons 
#
#
###########################################################################################################################################################################################################


def combat_donjon(monstre,player,donjon,type = "|donjon|"):
    vie_en_moins = 0
    force_en_plus = 0
    print("Un monstre du \033[1m\033[35mdonjon\033[0m apparaît, un",monstre,"!")
    if type == "|Unique|":
        nom_monstre = init_donjon(donjon)
        nom_monstre = nom_monstre[2]
    else:
        nom_monstre = str(monstre)
    if nom_monstre == "kishim":
        dragon()
    enemis = Personnage(nom_monstre + " " + type,monstre)
    enemis.fiche_monstre()
    while not enemis.est_mort() and not player.est_mort() :
        sleep(1)
        tour_monstre(enemis,player)
        tour_joueur(enemis,player,vie_en_moins,force_en_plus)
        enemis.fiche_monstre()
        player.fiche_joueur(False)
    recompense_combat(player,monstre)


def init_donjon(donjon):
    match donjon:
        case "donjon gobelin":
            return ("hobgobelin","Roi hobgobelin","Roi Cupide","couronne du roi Cupide")
        case "terre orcs":
            return ("Général orc","Seigneur Boucher","Grand Boucher","croc du Boucher")
        case "tombeau de géant":
            return ("Géant","Monolithe","Coeur de la montagne","Coeur de la Montagne")
        case "abysses éternel":
            return ("Hydre","Mégalodon", "Dévoreur des Abysses","Écaille du Prédateur")
        case "volcan impérial":
            return ("Dragon","Dragon du chaos","Kishim","Épée Dragonicide")
        
    
###########################################################################################################################################################################################################
#
#
#                                                                                     gestion de la boutique
#
#
###########################################################################################################################################################################################################


def boutique(player):
    print("Bienvenue cher client !")
    print("il y a 3 phases :")
    print("  - vente 📥")
    print("  - achat 📤")
    print("  - gacha 📦")
    sleep(2)
    print("\nphase de vente :")
    reponse = " "
    dico = {}
    liste_vendable = []
    for elt in objet:
        if elt not in objet_nom_cumulable :
            if elt not in dico :
                dico[elt] = 1
            else:
                dico[elt] +=1
    for elt in dico:
        if elt not in objet_nom_cumulable:
            liste_vendable.append(elt)
    if len(liste_vendable) > 0: 
        dico_actuel = {}
        for elt in objet:
            if elt in objet_vente_prix:
                dico_actuel[elt] = dico_actuel.get(elt, 0) + 1
        if dico_actuel:
            print("-" * 56)
            print(f"{'Objet':<24} | {'Quantité':>10} | {'Prix Unitaire':>15}")
            print("-" * 56)
            for nom, qte in dico_actuel.items():
                prix = objet_vente_prix[nom]
                print(f"{nom:<24} | {qte:>10} |\033[93m {prix:>12}\033[0m 🪙")
            print("-" * 56)
            while reponse not in choix_reponse:
                reponse = input("Avez vous des objets a vendre ?\n")
                reponse = reponse.lower()
                if reponse == "oui" or reponse == "o":
                    vente(player)
        else:
            print("Vous n'avez pas d'objets vendables.")
    print("phase d'achat :")
    achat(player)
    print("phase gacha :")
    gacha(player)
    

def achat(player):
    print(f"\nVous avez : \033[33m{player.bourse}\033[0m 🪙")
    objet_achat_liste = []
    dependances = {
        "épée+": "épée", "épée++": "épée+", "épée runique": "épée++", "épée ancestrale": "épée runique",
        "casque+": "casque", "casque++": "casque+", "casque runique": "casque++", "casque ancestrale": "casque runique",
        "armure+": "armure", "armure++": "armure+", "armure runique": "armure++", "armure ancestrale": "armure runique",
        "bouclier+": "bouclier", "bouclier++": "bouclier+", "bouclier runique": "bouclier++", "bouclier ancestrale": "bouclier runique"
    }
    for article in objet_achat:
        prix = objet_achat_prix[article]
        if player.bourse >= prix:
            deja_possede = article in objet
            condition_niveau_precedent = True
            if article in dependances:
                if dependances[article] not in objet:
                    condition_niveau_precedent = False
            
            if not deja_possede and condition_niveau_precedent:
                objet_achat_liste.append(article)
            elif article in objet_achat and article not in equipement and article in objet_consomable:
                objet_achat_liste.append(article)
    if len(objet_achat_liste) > 0:
        print("-" * 39)
        print(f"{'Article':<24} | {'Prix':>10}")
        print("-" * 39)
        for article in objet_achat_liste:
            print(f"{article:<24} | \033[33m{objet_achat_prix[article]:>7}\033[0m 🪙")
        print("-" * 39)
        reponse = input("\nQue voulez-vous acheter ?\n").lower()
        if reponse in ["non", "n"]:
            print("Vous partez.")
            return
        if reponse in objet_achat_liste:
            if reponse in objet_consomable:
                nombre = 0
                argent_payer = 0
                while nombre <= 0:
                    saisie = input(f"Combien de {reponse} voulez-vous ? (Max : {player.bourse // objet_achat_prix[reponse]})\n")
                    try:
                        nombre = int(saisie)
                        argent_payer = objet_achat_prix[reponse] * nombre
                        if nombre <= 0:
                            print("Veuillez entrer un nombre positif.")
                        elif argent_payer > player.bourse:
                            print(f"Pas assez d'argent ! Il vous manque {argent_payer - player.bourse} 🪙")
                            nombre = 0
                    except ValueError:
                        print("Savez-vous ce qu'est un nombre au moins ?")
                        if "Nombre = lettre" not in succes:
                            succes.append("Nombre = lettre")
                            succes_obtient()
                        nombre = 0
                print(f"Vous achetez {nombre} {reponse} pour {argent_payer} 🪙")
                player.bourse -= argent_payer
                for _ in range(nombre):
                    objet.append(reponse)
                    objet_bonus(player, reponse)
            else:
                prix = objet_achat_prix[reponse]
                player.bourse -= prix
                print(f"Vous achetez : {reponse} pour {prix} 🪙")
                objet.append(reponse)
                objet_bonus(player, reponse)
            objet_posseder(objet)
            achat(player)
        else:
            print("Cet objet n'est pas disponible ou vous ne pouvez pas l'acheter.")
            achat(player)
    else:
        print("La boutique est vide ou vous n'avez pas assez d'argent !")


def vente(player):
    tri_objet(objet)
    argent = 0
    fin = False
    while fin == False and len(objet) != 0:
        dico_actuel = {}
        for elt in objet:
            if elt in objet_vente_prix:
                dico_actuel[elt] = dico_actuel.get(elt, 0) + 1
        if not dico_actuel:
            print("Vous n'avez plus d'objets vendables.")
            break
        print("-" * 56)
        print(f"{'Objet':<24} | {'Quantité':>10} | {'Prix Unitaire':>15}")
        print("-" * 56)
        for nom, qte in dico_actuel.items():
            prix = objet_vente_prix[nom]
            print(f"{nom:<24} | {qte:>10} |\033[93m {prix:>12}\033[0m🪙")
        print("-" * 56)
        reponse = input("\nQue voulez-vous vendre ?\n").lower()
        if reponse in ["non", "n"]:
            fin = True
        elif reponse == "tout":
            for obj_nom in list(objet):
                if obj_nom in objet_vente_prix:
                    argent += objet_vente_prix[obj_nom]
                    objet.remove(obj_nom)
            print("Vous avez tout vendu.")
            fin = True
        elif reponse in dico_actuel:
            max_possible = dico_actuel[reponse]
            nb_a_vendre = 0
            while nb_a_vendre <= 0:
                saisie = input(f"Combien de {reponse} voulez-vous vendre ? (Max: {max_possible})\n")
                try:
                    nb_a_vendre = int(saisie)
                    if nb_a_vendre <= 0: 
                        print("C'est pas comme ça que sa marche")
                except ValueError:
                    print("Savez vous ce qu'est un nombre au moins ?")
                    if "Nombre = lettre" not in succes:
                        succes.append("Nombre = lettre")
                        succes_obtient()
                    nb_a_vendre = 0
            if nb_a_vendre > max_possible:
                nb_a_vendre = max_possible
            prix_total_vente = nb_a_vendre * objet_vente_prix[reponse]
            for _ in range(nb_a_vendre):
                objet.remove(reponse)
            argent += prix_total_vente
            print(f"Vous vendez {nb_a_vendre} {reponse} pour \033[93m{prix_total_vente}\033[0m🪙.")
        else:
            print("Vous ne possédez pas cet objet ou il n'est pas vendable.")
    player.bourse += argent
    print(f"Gain total : \033[93m{argent}\033[0m🪙")


def gacha(player):
    print("\nVous avez : \033[33m",player.bourse,"\033[0m 🪙")
    print("-" * 35)
    print(f"{'boite':<20} | {'Prix':>10}")
    print("-" * 35)
    for boite in boite_gacha:
        print(f"{boite:<20} | \033[33m{boite_gacha_prix[boite]:>7}\033[0m 🪙")
    print("-" * 35)
    reponse = input("\nQue voulez-vous acheter ?\n").lower()
    if reponse in ["non", "n"]:
        print("Vous partez.")
        return
    if reponse in boite_gacha:
        if boite_gacha_prix[reponse] <= player.bourse:
            ouverture_gacha(reponse)
            player.bourse-= boite_gacha_prix[reponse]
            print("Il vous reste : \033[33m",player.bourse,"\033[0m 🪙")
        else:
            print("Vous n'avez pas assez pour cette boite, je ne fait pas crédit !")
            gacha(player)
    else:
        print("C'est quoi ? je n'en vend pas en tout cas !")
        gacha(player)


###########################################################################################################################################################################################################
#
#
#                                                                                     gestion de l'inventaire et des objets
#
#
###########################################################################################################################################################################################################


def gagner_objet(player,monstre):
    if player.metier == "mercenaire":
        tirage_objet(monstre)
    tirage_objet(monstre)
              

def tirage_objet(monstre):
    tirage = randint(1,15)
    tirage2 = randint(1,15)
    if tirage == 15 or tirage2 == 15:
        tirage3 = randint(1,2)
        if tirage3 == 1:
            objet.append("fruit démoniaque")
            print("vous obtenez : ","\033[31mfruit démoniaque\033[0m")
        else:
            objet.append("statue héroique")
            print("vous obtenez : ","\033[31mstatue héroique\033[0m")
    elif monstre =="dragon":
            objet.append("fruit démoniaque")
            print("vous obtenez : ","\033[31mfruit démoniaque\033[0m")
    elif tirage == 1 or tirage2 == 1 or tirage == 2:
        if monstre == "slime":
            objet.append("acide de slime")
            print("vous obtenez : ","\033[31macide de slime\033[0m")
        elif monstre =="gobelin":
            objet.append("dague de gobelin")
            print("vous obtenez : ","\033[31mdague de gobelin\033[0m")
        elif monstre =="gnoll":
            objet.append("croc de gnoll")
            print("vous obtenez : ","\033[31mcroc de gnoll\033[0m")
        elif monstre =="orc":
            objet.append("lame d'orc")
            print("vous obtenez : ","\033[31mlame d'orc\033[0m")
        else:
            objet.append("potion de vie")
            print("vous obtenez : ","\033[31mpotion de vie\033[0m")
    elif tirage2 == 2 or tirage == 3 and tirage2 == 3 :
        objet.append("potion de sacrifice")
        print("vous obtenez : ","\033[31mpotion de sacrifice\033[0m")
    elif tirage == 4 and tirage2 == 4:
        objet.append("potion de puissance")
        print("vous obtenez : ","\033[31mpotion de puissance\033[0m")


def tri_objet(objet):
    inventaire = []
    for elt_different in objet_possible:
        nb_objet = objet.count(elt_different)
        if nb_objet > 0:
            for _ in range(nb_objet):
                inventaire.append(elt_different)
    for _ in range(len(objet)):
        objet.pop()
    for i in range(len(inventaire)):
        objet.append(inventaire[i])


def affiche_inventaire(dico):
    for elt in dico:
        if elt in equipement:
            return True


def objet_posseder(objet,affiche_tout = True):
    """
    """
    tri_objet(objet)
    liste_special = []
    liste_normal = []
    dico = {}
    for elt in objet:
        if elt not in objet_nom_cumulable :
            if elt not in dico :
                dico[elt] = 1
            else:
                dico[elt] +=1
    for elt in objet_nom_cumulable:
        if elt not in dico and elt in objet:
            dico[elt] = 1
    for elt in dico:
            if elt not in objet_nom_cumulable:
               liste_normal.append(elt) 
            elif elt in objet_donjon or elt in objet_special:
                liste_special.append(elt)
    print("--------------------------------")
    if len(liste_normal) > 0:
        taille_max = taille_max_elt_liste(liste_normal)
        print("\033[1m\033[4minventaire :\033[0m")    
        for elt in liste_normal :
            espace = " "*(taille_max-len(elt))
            print(elt,espace,":",dico[elt])
        print("--------------------------------")
    if affiche_tout == True:
        inventaire_complet(dico,liste_special)
    

def inventaire_complet(dico,liste_objet):
    inventaire = affiche_inventaire(dico)
    if inventaire:
        print("\033[1m\033[4méquipement :\033[0m")  
        niveau(objet)
        print("--------------------------------")
    if liste_objet:
        print("\033[1m\033[4méquipement unique :\033[0m") 
        liste_objet_donjon = []
        liste_objet_special = []
        for elt in liste_objet:
            if elt in objet_donjon:
                liste_objet_donjon.append(elt)
            else:
                liste_objet_special.append(elt)
        if liste_objet_special:
            print("- Spécial :")
            for elt in liste_objet_special:
                print("   ",elt)
        if liste_objet_donjon:
            print("- Donjon :")
            for elt in liste_objet_donjon:
                print("   ",elt)     
        print("--------------------------------\n") 


def taille_max_elt_liste(liste):
    max = 0
    for elt_max in liste:
        if len(elt_max) > max:
            max = len(elt_max)
    return max


def niveau(liste_objet):
    comp_epee = ""
    comp_casque = ""
    comp_armure = ""
    comp_bouclier = ""
    for elt in liste_objet:
        if elt in tab_epee:
            comp_epee += "⭐"
        elif elt in tab_casque:
            comp_casque += "⭐"
        elif elt in tab_armure:
            comp_armure += "⭐"
        elif elt in tab_bouclier:
            comp_bouclier += "⭐"
    if comp_epee != "":
        print("épée     : ",comp_epee)
    if comp_casque != "":
        print("casque   : ",comp_casque)
    if comp_armure != "":
        print("armure   : ",comp_armure)
    if comp_bouclier != "":
        print("bouclier : ",comp_bouclier)
    if comp_epee == comp_casque ==  comp_armure == comp_bouclier == "⭐⭐⭐⭐⭐" and "Armement lourd" not in succes:
        succes.append("Armement lourd")
   
   
def objet_bonus(player,objet_ajouter):
    match objet_ajouter:
        case 'épée':
            player.force += 5
        case 'casque' | 'armure':
            player.max_pv += 5
            player.pv += 5
        case 'bouclier'|'casque+' | 'armure+':
            player.max_pv += 10
            player.pv += 10
        case 'épée+':
            player.force += 10
        case 'bouclier+' |'casque++' | 'armure++' | "orbe elfique" | "poil de pied":
            player.max_pv += 20
            player.pv += 20
        case 'épée++':
            player.force += 20
        case "bouclier++" |"casque runique" |"armure runique":
            player.max_pv += 30
            player.pv += 30
        case "épée runique":
            player.force += 30
        case "bouclier runique"|"casque ancestrale"|"armure ancestrale":
            player.max_pv += 50
            player.pv += 50
        case "épée ancestrale":
            player.force += 50
        case "bouclier ancestrale":
            player.max_pv += 70
            player.pv += 70
        case "coeur démoniaque"| "Épée Dragonicide":
            player.force += 100
        case "coeur angelique" | "Coeur de la Montagne":
            player.max_pv += 100
            player.pv += 100
        case "collier de général gobelin":
            player.max_pv += 10
            player.pv += 10
            player.force += 5
        case "massue de général orc":
            player.max_pv += 5
            player.pv += 5
            player.force += 10
        case "rose corrompu":
            player.force += 20
        case "cape cendrée":
            player.force += 10
            player.max_pv += 10
            player.pv += 10
        case "couronne du roi Cupide":
            player.max_pv += 50
            player.pv += 50
            player.force += 10
        case "croc du Boucher":
            player.max_pv += 30
            player.pv += 30
            player.force += 30
        case "Écaille du Prédateur": 
            player.parade = 0.1
            

def ouverture_gacha(reponse):
    liste_recompense = []
    dico_recompense = {}
    print("Vous obtenez :")
    if reponse == "commune":
        objet_boite_commune = ["potion de vie","potion de sacrifice","potion de puissance"]
        for _ in range(5):
            indice_alea = randint(0,2)
            objet_gagner = objet_boite_commune[indice_alea]
            liste_recompense.append(objet_gagner)
    elif reponse == "rare":
        objet_boite_commune = ["potion de vie","potion de sacrifice","potion de puissance","fruit démoniaque","statue héroique"]
        for _ in range(10):
            indice_alea = randint(0,4)
            objet_gagner = objet_boite_commune[indice_alea]
            liste_recompense.append(objet_gagner)   
    elif reponse == "épique":
        objet_boite_commune = ["potion de vie supérieure","potion de puissance","fruit démoniaque","statue héroique"]
        for _ in range(10):
            indice_alea = randint(0,3)
            objet_gagner = objet_boite_commune[indice_alea]
            liste_recompense.append(objet_gagner)
    elif reponse == "ultime":
        objet_boite_commune = ["potion de vie supérieure","potion de puissance","fruit démoniaque","potion de vie ultime"]
        for _ in range(10):
            indice_alea = randint(0,3)
            objet_gagner = objet_boite_commune[indice_alea]
            liste_recompense.append(objet_gagner)
        if "boite porte bonheur" not in objet:
            objet.append("boite porte bonheur")
        if "Fou de gâcha" not in succes:
            succes_obtient()
            succes.append("Fou de gâcha")
    elif reponse == "mystère":
        nb_objet = randint(10,20)
        for _ in range(nb_objet):
            indice_alea = randint(0, 10)
            objet_gagner = objet_possible[indice_alea]
            liste_recompense.append(objet_gagner)
        if "Quitte ou double !" not in succes:
            succes_obtient()
            succes.append("Quitte ou double !")
    for objet_gagner in liste_recompense:
        if objet_gagner not in dico_recompense :
            dico_recompense[objet_gagner] = 1
        else:
            dico_recompense[objet_gagner] +=1
    for elt in dico_recompense:
        print("  -",dico_recompense[elt],elt)
    for elt in liste_recompense:
        objet.append(elt)


###########################################################################################################################################################################################################
#
#
#                                                                                          autres actions
#
#
###########################################################################################################################################################################################################


def collecte(player):
    player.gagner_argent(5,20)
    print("la vente des matériaux raporte bien !")
    
        
def repos(player):
    print("Vous décidez de vous reposer... vous êtes un flemmard ou quoi !? ")
    player.recuperer_vie()


###########################################################################################################################################################################################################
#
#
#                                                                                             fin de jeu
#
#
###########################################################################################################################################################################################################


def fin_jeu(player):
    fin()
    sleep(2)
    player.fiche_joueur()
    if len(succes) > 0:
        print("\n____________________________________")
        print("\n\033[1m\033[4mSuccès :\033[0m\n")
        nb_succes = 0
        for elt in succes_exite:
            sleep(1)
            if elt in succes:
                nb_succes += 1
                print("  -",icone_succes[elt],elt)
            else:
                print("  -   ???")
        print("\n",nb_succes,"/",len(succes_exite),"succes !")
        print("____________________________________")
