import random
import numpy as np
import lab2.robot_movement as rm
import lab2.robot_sensor as rs
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

size = 8
steps = 1000

t_mat = rm.get_transition_matrix(size, size)
f = np.ones((size ** 2 * 4, 1)) * (1 / (size ** 2))

robot_pos = []
pos = (random.randint(0, size - 1), random.randint(0, size - 1))
dir = random.choice([(-1, 0), (0, 1), (1, 0), (0, -1)])
manh_dist = []
manH_dist_accum = []
pos_x = np.ndarray(steps)
pos_y = np.ndarray(steps)
pos_est_x = np.ndarray(steps)
pos_est_y = np.ndarray(steps)

print('True:  | Estimated:')
for i in range(steps):
    movement = rm.get_move(pos, dir, size, size)
    pos = movement[0]
    dir = movement[1]
    reading = rs.get_sensor_reading(pos, size, size)
    o_mat = rs.get_obs_mat(reading, size, size)
    f = np.matmul(o_mat, np.matmul(t_mat.transpose(), f))
    f = f / sum(f)

    robot_pos.append(pos)
    pos_est = ((np.argmax(f) // 4) // size, (np.argmax(f) // 4) % size)
    print(str(pos) + ' | ' + str(pos_est))

    manh_dist.append(abs(pos[0] - pos_est[0]) + abs(pos[1] - pos_est[1]))
    manH_dist_accum.append(sum(manh_dist)/len(manh_dist))

    pos_x[i] = pos[0]
    pos_y[i] = pos[1]
    pos_est_x[i] = pos_est[0]
    pos_est_y[i] = pos_est[1]


print()
print('Accuracy: ' + str(manh_dist.count(0)/len(manh_dist)))
print()
print('Average Manhattan distance: ' + str(sum(manh_dist)/len(manh_dist)))

plt.plot(manH_dist_accum)
plt.ylabel('Average Manhattan distance')
plt.xlabel('Steps')
plt.show()


