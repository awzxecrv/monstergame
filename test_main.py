import main


def test_gestion_des_degats():
    bob  = ['Bob', 10, 5, 10]
    alice = ['Alice', 20, 15, 5]

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


def test_gestion_du_combat():
    joueurs  = [['a', 9, 0, 0], ['b', 10, 5, 1], ['c',10, 0, 0]]
    monstres = [['A', 1,10, 0],[ 'B', 10, 1, 1], ['C',10, 2, 0]]
    res      = [['a',-1, 0, 0], ['b', 10, 5, 1], ['c', 0, 0, 0]]
    
    for j,m,r in zip(joueurs, monstres, res):
        res = main.gestion_du_combat(j, m)
        assert res == r


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
            