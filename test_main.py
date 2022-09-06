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
