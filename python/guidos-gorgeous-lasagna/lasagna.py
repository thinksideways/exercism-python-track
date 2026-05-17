"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

"""
Constants for the time in oven and time to prepare.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers_of_lasagna):
    """Calculate the preparation time in minutes.

    Parameters:
        layers_of_lasagna (int): The number of lasagna layers being prepared.

    Returns:
        int: The number of minutes in total preparation assuming 'PREPARATION_TIME' per layers_of_lasagna
    """
    return PREPARATION_TIME * layers_of_lasagna

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes of preparation and baking.

    Parameters:
        number_of_layers (int): The number of lasagna layers being prepared.
        elapsed_bake_time (int): The time already spent baking in minutes.

    Returns:
        int: The total minutes gone by in preparation and baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
