from math import inf


def read_float(text_to_display, lower_bound=float(-inf), upper_bound=float(inf)):
    '''
    Read a float from the user within bounds
    '''
    while True:
        try:
            num = float(input(text_to_display))
        except ValueError:
            print("Please, enter a real number!")
            continue
        else:
            if num < lower_bound:
                print("Please, enter a number greater than or equal to", lower_bound)
                continue
            if num > upper_bound:
                print("Please, enter a number less than or equal to", upper_bound)
                continue
            return num


def read_int(text_to_display, lower_bound=float(-inf), upper_bound=float(inf)):
    '''
    Read an int from the user within bounds
    '''
    while True:
        try:
            num = int(input(text_to_display))
        except ValueError:
            print("Please, enter a whole number!")
            continue
        else:
            if num < lower_bound:
                print("Please, enter a number greater than or equal to", lower_bound)
                continue
            if num > upper_bound:
                print("Please, enter a number less than or equal to", upper_bound)
                continue
            return num