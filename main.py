"""Converts a string of numeral letters (e.g. Roman numerals) into their decimal value."""


def main():
    """
    Runs the numeral-conversion program.

    :return: None
    """
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
    character = input('Zahlzeichen (§=Ende) > ')
    while character != '§':
        value = read_int('Wert')
        numeral_dict[character] = value
        character = input('Zahlzeichen (§=Ende) > ')


def read_int(prompt):
    """
    Asks the user to input a positive integer.

    :param prompt (str): text to display when asking for the input
    :return: number (int): the positive integer entered by the user
    """

    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Please, enter a whole number!')
            continue
        else:
            if num < 0:
                print('Please, enter a number greater than or equal to', 0)
                continue
            return num
    '''
    # Alternative Lösung:
    from input_reader import read_int
    return read_int(prompt, 0)
    '''


def convert(letters, numeral_dict):
    """
    Converts the numeral letters into a decimal number.

    :param letters (str): the numeral letters to convert
    :param numeral_dict (dict): dictionary mapping each letter to its value
    :return: decimal_value (int): the sum of the values of all letters
    """
    total = 0
    for character in letters:
        total += numeral_dict[character]

    return total


if __name__ == '__main__':
    main()
