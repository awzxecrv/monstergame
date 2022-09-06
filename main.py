

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

