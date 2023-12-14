import main

'''
Tests for each function
'''


def test_read_numerals(capsys, monkeypatch):
    inputs = iter(['L', '1', 'C', '12', '§'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'read_int', dummy_read_int)
    result = dict()
    main.read_numerals(result)
    assert result == {'L': 1, 'C': 12}


def test_read_int(capsys, monkeypatch):
    inputs = iter(['L', '-3', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = main.read_int('')
    assert result == 5
    captured = capsys.readouterr()
    assert captured.out == 'Please, enter a whole number!\nPlease, enter a number greater than or equal to 0\n'


def test_convert(capsys):
    numerals = {'I': 1, 'V': 5, 'X': 10}
    result = main.convert('XXVIII', numerals)
    assert result == 28


def test_roman(capsys, monkeypatch):
    inputs = iter(['I', '1', 'V', '5', 'X', '10', 'C', '100', '§', 'CXXVII'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == 'CXXVII entspricht 127\n'


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
    assert captured.out == "Please, enter a whole number!\nA entspricht 1\n"


def test_negative_number(capsys, monkeypatch):
    inputs = iter(['A', '-3', '1', '§', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == 'Please, enter a number greater than or equal to 0\nA entspricht 1\n'


'''
helper functions for testing
'''


# monkeypatch to replace the function 'read_int' in main
def dummy_read_int(prompt):
    return int(input(''))
