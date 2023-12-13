import main


def test_roman(capsys, monkeypatch):
    inputs = iter(['I', '1', 'V', '5', 'X', '10', 'C', '100', '§', 'CXXVII'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "CXXVII entspricht 127\n"


def test_assyrian(capsys, monkeypatch):
    inputs = iter(['L', '1', 'C', '12', 'V', '144', 'X', '288', '§', 'XXCLLLLL'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "XXCLLLLL entspricht 593\n"


def test_not_a_number(capsys, monkeypatch):
    inputs = iter(['A', 'B', '1', '§', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Gib eine positive Ganzzahl ein\nA entspricht 1\n"


def test_negative_number(capsys, monkeypatch):
    inputs = iter(['A', '-3', '1', '§', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Gib eine positive Ganzzahl ein\nA entspricht 1\n"
