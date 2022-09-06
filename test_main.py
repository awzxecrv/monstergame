import main
import pytest


def test_generation_du_monstre():
    for _ in range(200):
        for n_monstre in ['Orc', 'Elf', 'Tyrannide']:
            monstre = main.generation_du_monstre(n_monstre)
        
            assert type(monstre) == list
            assert len(monstre) == 4
            assert monstre[0] == n_monstre
            assert 5 <= monstre[1] <= 20
            assert 3 <= monstre[2] <= 8
            assert 0 <= monstre[3] <= 5
            