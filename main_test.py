"""Unit tests for the main module."""

import main


# Tests for each function


def test_read_numerals(capsys, monkeypatch):
    """Checks that read_numerals stores the entered letter-value pairs until '§' is entered."""
    inputs = iter(['L', '1', 'C', '12', '§'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'read_int', dummy_read_int)
    result = dict()
    main.read_numerals(result)
    assert result == {'L': 1, 'C': 12}


def test_read_int(capsys, monkeypatch):
    """Checks that read_int rejects non-numbers and negative numbers until a valid one is entered."""
    inputs = iter(['L', '-3', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = main.read_int('')
    assert result == 5
    captured = capsys.readouterr()
    assert captured.out == 'Please, enter a whole number!\nPlease, enter a number greater than or equal to 0\n'


def test_convert(capsys):
    """Checks that convert sums the values of the given numeral letters."""
    numerals = {'I': 1, 'V': 5, 'X': 10}
    result = main.convert('XXVIII', numerals)
    assert result == 28


def test_roman(capsys, monkeypatch):
    """Checks the full program with Roman numerals."""
    inputs = iter(['I', '1', 'V', '5', 'X', '10', 'C', '100', '§', 'CXXVII'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == 'CXXVII entspricht 127\n'


def test_assyrian(capsys, monkeypatch):
    """Checks the full program with a different, Assyrian-style numeral system."""
    inputs = iter(['L', '1', 'C', '12', 'V', '144', 'X', '288', '§', 'XXCLLLLL'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "XXCLLLLL entspricht 593\n"


def test_not_a_number(capsys, monkeypatch):
    """Checks that a non-numeric value entered is rejected by read_int."""
    inputs = iter(['A', 'B', '1', '§', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Please, enter a whole number!\nA entspricht 1\n"


def test_negative_number(capsys, monkeypatch):
    """Checks that a negative value entered is rejected by read_int."""
    inputs = iter(['A', '-3', '1', '§', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    captured = capsys.readouterr()
    assert captured.out == 'Please, enter a number greater than or equal to 0\nA entspricht 1\n'


# helper functions for testing


def dummy_read_int(prompt):
    """Replacement for main.read_int used via monkeypatch, without validation."""
    return int(input(''))
