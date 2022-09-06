import main
import pytest


def test_main_creation():
    deffs = [['a', 9, 0, 0], ['b', 10, 5, 5], ['c', 10, 0, 0]]
    atts  = [['A', 1, 10, 0],['B', 10, 1, 1], ['C', 10, 2, 0]]
    res = [['a',-1,0,0], ['b', 8, 5, 5], ['c', 0, 0, 0]]
    
    for d,a,r in zip(deffs, atts, res):
        res = main.gestion_du_combat(d,a)
        assert res == r
