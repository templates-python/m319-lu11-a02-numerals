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
    character = input('Zahlzeichen (§=Ende) > ')
    while character != '§':
        value = read_int('Wert')
        numeral_dict[character] = value
        character = input('Zahlzeichen (§=Ende) > ')


def read_int(prompt):
    """
    asks the user to input a positive integer
    :param prompt:
    :return: number
    """
    number = None
    while number is None:
        try:
            number = int(input(f'{prompt} > '))
            if number < 0:
                print('Gib eine positive Ganzzahl ein')
                number = None
        except ValueError:
            print('Gib eine positive Ganzzahl ein')
    return number


def convert(letters, numeral_dict):
    """
    converts the numerals into a decimal number
    :param letters:
    :param numeral_dict:
    :return:
    """
    total = 0
    for character in letters:
        total += numeral_dict[character]

    return total


if __name__ == '__main__':
    main()
