import random
import numpy as np
import lab2.robot_movement as rm
import lab2.robot_sensor as rs

size = 8

t_mat = rm.get_transition_matrix(size, size)
f = np.ones((size ** 2 * 4, 1)) * (1 / (size ** 2))

robot_pos = []
pos = (random.randint(0, size - 1), random.randint(0, size - 1))
dir = random.choice([(-1, 0), (0, 1), (1, 0), (0, -1)])
# robot_pos.append(pos)

for i in range(2):
    movement = rm.get_move(pos, dir, size, size)
    pos = movement[0]
    dir = movement[1]
    reading = rs.get_sensor_reading(pos, size, size)
    o_mat = rs.get_obs_mat(reading, size, size)
    f = np.matmul(o_mat, np.matmul(t_mat.transpose(), f))
    f = f/sum(f)

robot_pos.append(pos)

print(f)
print()
print(pos)
print(sum(f))
