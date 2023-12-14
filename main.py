def main():
    """
    main program
    :return: None
    """
    numerals = dict()
    read_numerals(numerals)
    letters = input('Schriftzeichen > ')
    decimal_value = convert(letters, numerals)
    print(f'{letters} entspricht {decimal_value}')


def read_numerals(numeral_dict):
    """
    reads the numerals and their values
    :param numeral_dict:
    :return: None
    """
    # Speichere die Eingabe des Benutzers in Buchstabe
    # Solange Buchstabe nicht § ist
        # Speichere den Returnwert von read_int als Zahl
        # Speichere die Eingaben im Dictionary (Buchstabe ist der Schlüssel, Zahl ist der Wert)
        # Speichere die Eingabe des Benutzers in Buchstabe


def read_int(prompt):
    """
    asks the user to input a positive integer
    :param prompt:
    :return: number
    """

    '''
    Du könntest deine Funktion zum Lesen von Ganzzahlen aus einem früheren Programm (LU 10)
    verwenden. Du könntest diese importieren oder hierhin kopieren.
    Ergänze eine Bedingung, dass die Zahl positiv sein muss (grösser 0)
    '''
    pass


def convert(letters, numeral_dict):
    """
    converts the numerals into a decimal number
    :param letters:
    :param numeral_dict:
    :return:
    """
    # setze das Total gleich 0
    # Iteration über alle Buchstaben in letters
        # nimm den Wert im Dictionary mit dem Buchstaben als Key, addiere diesen Wert zum Total

    # Gib das Total als Returnwert zurück
    pass


if __name__ == '__main__':
    main()
