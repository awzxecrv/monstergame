import main
import pytest


def test_main_creation_du_personnage():
    personnage = main.creation_du_personnage('Pseudo', 16, 20, 10)

    assert type(personnage) == list
    assert len(personnage) == 4
    assert personnage[0] == 'Pseudo'
    assert personnage[1] == 16
    assert personnage[2] == 20
    assert personnage[3] == 10


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
            