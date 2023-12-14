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

    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("Please, enter a whole number!")
            continue
        else:
            if num < 0:
                print("Please, enter a number greater than or equal to", 0)
                continue
            return num
    '''
    # Alternative Lösung:
    from input_reader import read_int
    return read_int(prompt, 0)
    '''


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
