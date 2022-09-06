from random import randint

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
    