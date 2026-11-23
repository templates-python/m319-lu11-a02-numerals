"""Converts a string of numeral letters (e.g. Roman numerals) into their decimal value."""


def main():
    """
    Runs the numeral-conversion program.

    :return: None
    """
    # Die Main-Funktion ist bereits komplett und muss nicht angepasst werden.
    numerals = dict()
    read_numerals(numerals)
    letters = input('Schriftzeichen > ')
    decimal_value = convert(letters, numerals)
    print(f'{letters} entspricht {decimal_value}')


def read_numerals(numeral_dict):
    """
    Reads the numeral letters and their values from user input.

    :param numeral_dict (dict): dictionary to fill with letter-value pairs
    :return: None
    """
    # Speichere die Eingabe des Benutzers in Buchstabe
    # Solange Buchstabe nicht § ist
        # Speichere den Returnwert von read_int als Zahl
        # Speichere die Eingaben im Dictionary (Buchstabe ist der Schlüssel, Zahl ist der Wert)
        # Speichere die Eingabe des Benutzers in Buchstabe


def read_int(prompt):
    """
    Asks the user to input a positive integer.

    :param prompt (str): text to display when asking for the input
    :return: number (int): the positive integer entered by the user
    """

    '''
    Du könntest deine Funktion zum Lesen von Ganzzahlen aus einem früheren Programm (LU 10)
    verwenden. Du könntest diese importieren (from xx import read_int as my_read_int)
    und dann hier ihre my_read_int aufrufen mit dem min_value von 0
    oder sie kopieren den Inhalt von read_int hierhin und passen Sie den min_value mit 0 an.
    Ergänze eine Bedingung, dass die Zahl positiv sein muss (grösser 0)
    '''
    pass


def convert(letters, numeral_dict):
    """
    Converts the numeral letters into a decimal number.

    :param letters (str): the numeral letters to convert
    :param numeral_dict (dict): dictionary mapping each letter to its value
    :return: decimal_value (int): the sum of the values of all letters
    """
    # setze das Total gleich 0
    # Iteration über alle Buchstaben in letters
        # nimm den Wert im Dictionary mit dem Buchstaben als Key, addiere diesen Wert zum Total

    # Gib das Total als Returnwert zurück
    pass


if __name__ == '__main__':
    main()
