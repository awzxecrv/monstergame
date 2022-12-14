#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

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

    degats = force_attaque - armure_defenseur
    if degats < 0:
        degats = 0

    pv_restant = pv_defenseur - degats
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
    # On detecte quand le match sera nul :
    if joueur[3] >= monstre[2] and joueur[2] <= monstre[3]:
        # Si il l'est le houeur perd le nombre de point de vie du monstre
        joueur[2] -= monstre[2]
        return joueur

    # Tant que les deux personnages sont en vie
    while joueur[1] > 0 and monstre[1] > 0:

        # Le monstre attaque le joueur
        joueur[1] = gestion_des_degats(monstre, joueur)
        if joueur[1] <= 0:
            continue

        #Le joueur attaque le monstre
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

        print(f'Monstre {compteur}, {monstre[0]} : {monstre[1]}PV, {monstre[2]}Force et {monstre[3]}Armure.')

        joueur = gestion_du_combat(joueur, monstre)
    
        if joueur[1] > 0:
            print(f'{monstre[0]} a était vaincu... Il reste {joueur[1]}PV à {joueur[0]} !')
            compteur += 1
        else:
            print(f'{monstre[0]} a tué {joueur[0]}...')

    return compteur

def game():
    total_kill = 0
    nom_joueur = input('Entrez le nom de votre héro : ')
    
    answr = 'o'
    while answr != 'n':
        if answr != 'o':
            answr = input('Demande incomprise, Voulez vous rejouer [o/n]')
            continue

        joueur = [nom_joueur, 20, 5, 5]

        n_tue = compteur_ennemis_tue(joueur)
        print(f'{joueur[0]} à réussi à tué {n_tue} monstres.')
        total_kill += n_tue

        answr = input('Voulez vous rejouer [o/n] ?')

    print('Fin de partie,', nom_joueur, 'a tué', total_kill, 'monstres !')


if __name__ == '__main__':
    game()

