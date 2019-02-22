import numpy as np
import random


# Method to return the simulated sensor reading
# Parameters: Tuple with true position, number of rows, and number of cols
# Return: Tuple with the sensor read position
def get_sensor_reading(true_position, nbr_rows, nbr_cols):

    # Get first and second adj squares
    level_1 = get_level_1(true_position, nbr_rows, nbr_cols)
    level_2 = get_level_2(true_position, nbr_rows, nbr_cols)

    # Calculate ranges for probabilities
    true_upper_lim = 9
    true_range = (0, true_upper_lim)
    level_1_size = len(level_1)*5
    level_1_upper_lim = true_upper_lim + 1 + level_1_size
    level_1_range = (true_upper_lim + 1, level_1_upper_lim)
    level_2_size = len(level_2)*2.5
    level_2_upper_lim = level_1_upper_lim + 1 + level_2_size
    level_2_range = (level_1_upper_lim + 1, level_2_upper_lim)

    # Choose square to return
    choosen = random.randint(1, 101)

    if true_range[0] <= choosen <= true_range[1]:
        return true_position
    elif level_1_range[0] <= choosen <= level_1_range[1]:
        ind = int((choosen - true_upper_lim - 1) / 5)
        return level_1[ind]
    elif level_2_range[0] <= choosen <= level_2_range[1]:
        ind = int((choosen - level_1_upper_lim - 1) / 2.5)
        return level_2[ind]
    else:
        return (-1, -1)


# Helper method to get_sensor_reading
# Parameters: True position on robot, number of rows, and number of cols
# Return: List of tuples of immediately adjacent squares to true position
def get_level_1(true_position, nbr_rows, nbr_cols):
    adj = []
    for i in range(true_position[0] - 1, true_position[0] + 2):
        if i < 0 or i > nbr_rows - 1:  # If outside board bounds for rows
            continue
        for j in range(true_position[1] - 1, true_position[1] + 2):
            if j < 0 or j > nbr_cols - 1:  # If outside board bounds for cols
                continue
            if not (i == true_position[0] and j == true_position[1]):
                to_app = (i, j)
                adj.append(to_app)
    return adj


# Helper method to get_sensor_reading
# Parameters: True position on robot, number of rows, and number of cols
# Return: List of tuples of twice removed adjacent squares to true position
def get_level_2(true_position, nbr_rows, nbr_cols):
    adj = []
    for i in range(true_position[0] - 2, true_position[0] + 3):
        if i < 0 or i > nbr_rows - 1:  # If outside board bounds for rows
            continue
        for j in range(true_position[1] - 2, true_position[1] + 3):
            if j < 0 or j > nbr_cols - 1:  # If outside board bounds for cols
                continue
            # If current position is equal to or immediately adj to true pos, skip
            if not (abs(i - true_position[0]) <= 1 and  abs(j - true_position[1]) <= 1):
                to_app = (i, j)
                adj.append(to_app)
    return adj


print("RETURN:", get_sensor_reading((5,5), 10, 10))
