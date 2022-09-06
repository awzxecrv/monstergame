import main
import pytest


def test_gestion_des_degats():
    bob = ['Bob', 10, 5, 10]
    alice = ['Alice', 20, 15, 5]

    pv_defenseur = main.gestion_des_degats(bob, alice)

    assert type(pv_defenseur) == int
    assert pv_defenseur == alice[1] - (bob[2] - alice[3])

