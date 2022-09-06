

def creation_du_monstre():
    """
    La fonction de création d’un monstre prendra aucun paramètre 
    mais appellera la fonction de génération de monstre en 
    demandant à l’utilisateur le nom voulu pour le monstre.
    La fonction renverra donc le tableau avec les statistiques du monstre.
    """
    n_monstre = input('Entrez le nom du monstre : ')
    return generation_du_monstre(n_monstre)

