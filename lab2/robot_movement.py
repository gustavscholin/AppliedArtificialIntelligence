import random
import numpy as np


def get_move(pos, dir, nbr_rows, nbr_cols):
    if 0 <= pos[0] + dir[0] < nbr_rows and 0 <= pos[1] + dir[1] < nbr_cols:
        if random.random() < 0.3:
            dir = get_new_dir(pos, nbr_rows, nbr_cols)
        return [(pos[0] + dir[0], pos[1] + dir[1]), dir]
    dir = get_new_dir(pos, nbr_rows, nbr_cols)
    return [(pos[0] + dir[0], pos[1] + dir[1]), dir]


def get_new_dir(pos, nbr_rows, nbr_cols):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new_dir = random.choice(dirs)
    while not (0 <= pos[0] + new_dir[0] < nbr_rows and 0 <= pos[1] + new_dir[1] < nbr_cols):
        dirs.remove(new_dir)
        new_dir = random.choice(dirs)
    return new_dir


def get_transition_matrix(nbr_rows, nbr_cols):
    t_matrix = np.zeros((nbr_rows * nbr_cols * 4, nbr_rows * nbr_cols * 4))

    for row in range(nbr_rows):
        for col in range(nbr_cols):
            dirs = get_valid_dirs((row, col), nbr_rows, nbr_cols)
            to_indexes = get_to_indexes(dirs, row, col, nbr_cols)
            nbr_valid_dirs = sum(x is not None for x in dirs)
            for dir in range(4):
                from_index = row * nbr_cols * 4 + col * 4 + dir
                for op_dir in dirs:
                    if op_dir is not None:
                        if dirs[dir] is not None:
                            print(to_indexes[dirs.index(op_dir)])
                            t_matrix[from_index, to_indexes[dirs.index(op_dir)]] = 0.7 if op_dir == dirs[
                                dir] else 0.3 / (nbr_valid_dirs - 1)
                        else:
                            t_matrix[from_index, to_indexes[dirs.index(op_dir)]] = 1.0 / nbr_valid_dirs
    return t_matrix


def get_valid_dirs(pos, nbr_rows, nbr_cols):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    valid_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for dir in dirs:
        if not (0 <= pos[0] + dir[0] < nbr_rows and 0 <= pos[1] + dir[1] < nbr_cols):
            valid_dirs[dirs.index(dir)] = None
    return valid_dirs


def get_to_indexes(dirs, row, col, nbr_cols):
    to_indexes = []
    for dir in dirs:
        if dir is None:
            to_indexes.append(None)
        else:
            to_index = (dir[0] + row) * nbr_cols * 4 + (dir[1] + col) * 4 + dirs.index(dir)
            to_indexes.append(to_index)
    return to_indexes
