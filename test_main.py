import main
import pytest


def test_generation_du_monstre():
    for _ in range(200):
        monstre = main.generation_du_monstre('Lockness')
    
        assert type(monstre) == list
        assert len(monstre) == 4
        assert monstre[0] == 'Lockness'
        assert 5 <= monstre[1] <= 20
        assert 3 <= monstre[2] <= 8
        assert 0 <= monstre[3] <= 5
