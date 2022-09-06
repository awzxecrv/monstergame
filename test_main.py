import main
import pytest


def test_main_creation():
    joueurs  = [['a', 9, 0, 0], ['b', 10, 5, 1], ['c',10, 0, 0]]
    monstres = [['A', 1,10, 0],[ 'B', 10, 1, 1], ['C',10, 2, 0]]
    res      = [['a',-1, 0, 0], ['b', 10, 5, 1], ['c', 0, 0, 0]]
    
    for j,m,r in zip(joueurs, monstres, res):
        res = main.gestion_du_combat(j, m)
        assert res == r
