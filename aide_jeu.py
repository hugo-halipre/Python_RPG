###########################################################################################################################################################################################################
#
#
#                                                                               aide de jeu / affichage
#
#
###########################################################################################################################################################################################################

def affichage_complet(player):
    player.fiche_joueur()
    print("Détails des caractéristiques :\n")
    print("Nom : comment vous serez appelé.")
    print("Race : détermine votre ethnie et vos capacités.")
    print("Force : puissance d'attaque.")
    print("Bouclier : défense obtenue avec de l'équipement.")
    print("Point de vie (pv) : si ils tombent à 0, c'est la mort.")
    print("\nDifférentes actions :\n")
    print("	- Combat : permet de combattre des monstres et de gagner de l'argent")
    print("		  - Attaquer : permet d'attaquer l'adversaire, done de l'argent et/ou des objets")
    print("		  - Blesser : permet d'essayer d'attaquer en multipliant les dégats par 1.5,sinon l'adversaire se protège")
    print("		  - Booster : permet de se doper afin d'augmenter les dégâts de 1 en perdant 5 pv")
    print("		  - Objet : permet d'utiliser un objet (aucune limite)")
    print("		  - Fiche joueur : permet de voir la fiche de joueur")
    print("	- Collecte : permet de gagner un peu d'argent")
    print("	- Repos : récupère un peu de vie")
    print("	- Achat : permet d'acheter des objets\n")
    
def affichage_objet():
    print("potion de vie : permet de récupéré 15 pv")
    print("potion de sacrifice : permet de récupéré 1 en force contre 10 pv")
    print("potion de puissance : permet de gagner 1 en force")
    print("acide de slime : permet d'infliger entre 2 et 10 dégâts")
    print("dague de gobelin : permet d'infliger 5 dégâts")
    print("croc de gnoll : permet d'infliger 10 dégâts")
    print("lame d'orc : permet d'infliger 15 dégâts")
    print("fruit démoniaque : permet de faire perdre la moitier des pv de l'adversaire")


def grade(force):
    if force <= 100:
        return "Simple"
    elif 100 < force <= 250:
        return "Grand"
    elif 250 < force <= 500:
        return "Haut"
    elif force > 500:
        return "Dieu"

mot_de_passe = "alpha"

#Catégorie,Couleur,Code pour le Texte (Foreground),Exemple de Constante Python
#Reset,Réinitialisation,0,"RESET = ""\033[0m"""
#Gras/Clair,1,"BOLD = ""\033[1m"""
#Standard,Noir,30,"NOIR = ""\033[30m"""
#Standard,Rouge,31,"ROUGE = ""\033[31m"""
#Standard,Vert,32,"VERT = ""\033[32m"""
#Standard,Jaune,33,"JAUNE = ""\033[33m"""
#Standard,Bleu,34,"BLEU = ""\033[34m"""
#Standard,Magenta,35,"MAGENTA = ""\033[35m"""
#Standard,Cyan,36,"CYAN = ""\033[36m"""
#Standard,Blanc/Gris,37,"BLANC = ""\033[37m"""
#Vives (Bright),Noir/Gris Vif,90,"GRIS_VIF = ""\033[90m"""
#Vives (Bright),Rouge Vif,91,"ROUGE_VIF = ""\033[91m"""
#Vives (Bright),Vert Vif,92,"VERT_VIF = ""\033[92m"""
#Vives (Bright),Jaune Vif,93,"JAUNE_VIF = ""\033[93m"""
#Vives (Bright),Bleu Vif,94,"BLEU_VIF = ""\033[94m"""
#Vives (Bright),Magenta Vif,95,"MAGENTA_VIF = ""\033[95m"""
#Vives (Bright),Cyan Vif,96,"CYAN_VIF = ""\033[96m"""
#Vives (Bright),Blanc Vif,97,"BLANC_VIF = ""\033[97m"""