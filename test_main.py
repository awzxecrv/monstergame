import main

def test_gestion_des_degats():
    bob = ['Bob', 10, 5, 10]
    alice = ['Alice', 20, 15, 5]

<<<<<<< HEAD
    pv_defenseur = main.gestion_des_degats(bob, alice)

    assert type(pv_defenseur) == int
    assert pv_defenseur == alice[1] - (bob[2] - alice[3])

def test_creation_du_monstre(monkeypatch):
    for m_name in ['Lock', 'Ness', 'Tada']:
        monkeypatch.setattr('builtins.input', lambda _: m_name)
        #monkeypatch.setattr('__main__.generation_du_monstre', lambda n: [n, 6, 3, 0])

        monstre = main.creation_du_monstre()
        assert type(monstre) == list
        assert monstre[0] == m_name
        assert 5 <= monstre[1] <= 20
        assert 3 <= monstre[2] <= 8
        assert 0 <= monstre[3] <= 5
=======
def test_main_creation():
    joueurs  = [['a', 9, 0, 0], ['b', 10, 5, 1], ['c',10, 0, 0]]
    monstres = [['A', 1,10, 0],[ 'B', 10, 1, 1], ['C',10, 2, 0]]
    res      = [['a',-1, 0, 0], ['b', 10, 5, 1], ['c', 0, 0, 0]]
    
    for j,m,r in zip(joueurs, monstres, res):
        res = main.gestion_du_combat(j, m)
        assert res == r
>>>>>>> gestion_du_combat
