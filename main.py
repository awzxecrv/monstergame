

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
