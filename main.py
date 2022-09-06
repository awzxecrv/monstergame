from random import randint


def gestion_des_degats(att, deff):
    """
    La fonction de gestion des dégâts prendra en compte la force de l’attaquant,
    les PV de celui qui reçoit l’attaque ainsi que son armure.
    Il renverra alors PV défenseur – (Force attaque – armure défenseur)
    """
    pv_defenseur = deff[1]
    force_attaque = att[2]
    armure_defenseur = deff[3]

    pv_restant = pv_defenseur - (force_attaque - armure_defenseur)
    return pv_restant


def creation_du_monstre():
    """
    La fonction de création d’un monstre prendra aucun paramètre 
    mais appellera la fonction de génération de monstre en 
    demandant à l’utilisateur le nom voulu pour le monstre.
    La fonction renverra donc le tableau avec les statistiques du monstre.
    """
    n_monstre = input('Entrez le nom du monstre : ')
    return generation_du_monstre(n_monstre)


def gestion_du_combat(joueur, monstre):
    """
    La fonction de gestion de combat va permettre de continuer un combat
    jusqu’à ce qu’un le joueur ou le monstre n’ait plus de point de vie,
    et retournera le tableau de stats du joueur
    """

    # Tant que les deux personnages sont en vie
    while joueur[1] > 0 and monstre[1] > 0:
        joueur[1] = gestion_des_degats(monstre, joueur)
        if joueur[1] <= 0:
            continue

        monstre[1] = gestion_des_degats(joueur, monstre)

    #print(joueur, monstre)
    return joueur


def creation_du_personnage(pseudo, pv, forc, arm):
    """
    La fonction de création d’un personnage prendra en paramètre : 
    Pseudo, PV, Force et Armure et renverra un tableau contenant l’ensemble.
    """
    personnage = ['Pseudo', 16, 20, 10]

    return personnage

#print(help(creation_du_personnage))


def generation_du_monstre(monstre):
    """
    La fonction de génération du monstre prendra en paramètre 
    le nom du monstre et 
    renverra un tableau contenant l’ensemble des valeurs.
    La valeur pour PV, Force et Armure seront des valeurs aléatoires 
    respectivement entre 5 et 20, 3 et 8, 0 et 5
    """
    pv = randint(5,20) 
    forc = randint(3,8)
    arm = randint(0,5)

    monstre = [monstre, pv, forc, arm]
       
    return monstre


def compteur_ennemis_tue(joueur):
    """
    La fonction de compteur d’ennemis tués va s’incrémenter à chaque ennemi tué 
    et retourner cette valeur en fin de partie.
    """
    compteur = 0
    
    while joueur[1] > 0:
        monstre = creation_du_monstre()
        print(gestion_du_combat(joueur, monstre))
        break

    return None
compteur_ennemis_tue(['toto', 10, 5, 5])

