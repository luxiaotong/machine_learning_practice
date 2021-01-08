# https://zhuanlan.zhihu.com/p/93423829

import numpy as np
import matplotlib.pyplot as plt
# fig, ax = plt.subplots(2, 2, figsize=(14, 7))
fig, ax = plt.subplots(figsize=(14, 7))
# fig = plt.figure(figsize=(7, 7))
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

A = np.arange(1, 5)
B = A**2
C = A**3
# print(A, B, C)

ax.plot(A, B)
ax.plot(B, A)

ax.set_title('Title', fontsize=18)
ax.set_xlabel('xlabel', fontsize=18, fontstyle='italic')
ax.set_ylabel('ylabel', fontsize='x-large', fontstyle='oblique')
ax.legend(['A**2', 'A**1/2'])

ax.set_aspect('equal')
ax.minorticks_on()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.grid(which='minor', axis='both')

ax.xaxis.set_tick_params(rotation=45, labelsize=18, colors='g')
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 1))
ax.yaxis.tick_right()

plt.show()
