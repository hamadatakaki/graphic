#! /usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0.7, 100, 0.1)
y1 = 1/X
y2 = 1/(X)**2

plt.plot(X, y1, label="y=x^(-1)")
plt.plot(X, y2, label="y=x^(-2)")

plt.legend()
plt.savefig('figure07to100.png')