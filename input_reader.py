"""Helper functions for reading validated numbers from the user, within optional bounds."""

from math import inf


def read_float(text_to_display, lower_bound=float(-inf), upper_bound=float(inf)):
    """
    Reads a float from the user within the given bounds.

    :param text_to_display (str): text to display when asking for the input
    :param lower_bound (float): smallest value accepted
    :param upper_bound (float): largest value accepted
    :return: number (float): the validated float entered by the user
    """
    while True:
        try:
            num = float(input(text_to_display))
        except ValueError:
            print('Please, enter a real number!')
            continue
        else:
            if num < lower_bound:
                print('Please, enter a number greater than or equal to', lower_bound)
                continue
            if num > upper_bound:
                print('Please, enter a number less than or equal to', upper_bound)
                continue
            return num


def read_int(text_to_display, lower_bound=float(-inf), upper_bound=float(inf)):
    """
    Reads an int from the user within the given bounds.

    :param text_to_display (str): text to display when asking for the input
    :param lower_bound (float): smallest value accepted
    :param upper_bound (float): largest value accepted
    :return: number (int): the validated integer entered by the user
    """
    while True:
        try:
            num = int(input(text_to_display))
        except ValueError:
            print('Please, enter a whole number!')
            continue
        else:
            if num < lower_bound:
                print('Please, enter a number greater than or equal to', lower_bound)
                continue
            if num > upper_bound:
                print('Please, enter a number less than or equal to', upper_bound)
                continue
            return num
