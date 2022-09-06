
def gestion_des_degats(a,d):
    return d[1] - a[2] + d[3]

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

    return joueur
