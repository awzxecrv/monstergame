import main

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
