import random


def get_move(pos, dir, nbr_rows, nbr_cols):
    if 0 <= pos[0] + dir[0] < nbr_rows and 0 <= pos[1] + dir[1] < nbr_cols:
        if random.random() < 0.3:
            dir = get_new_dir(pos, nbr_rows, nbr_cols)
        return [(pos[0] + dir[0], pos[1] + dir[1]), dir]
    dir = get_new_dir(pos, nbr_rows, nbr_cols)
    return [(pos[0] + dir[0], pos[1] + dir[1]), dir]


def get_new_dir(pos, nbr_rows, nbr_cols):
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    new_dir = random.choice(dirs)
    while not (0 <= pos[0] + new_dir[0] < nbr_rows and 0 <= pos[1] + new_dir[1] < nbr_cols):
        dirs.remove(new_dir)
        new_dir = random.choice(dirs)
    return new_dir

