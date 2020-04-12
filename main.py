#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

valuesArray = np.zeros(100000)
maxValue = 0
bagAtMax = 0

for bag in range(100000):
    tempBag = bag
    if bag > 10000:
        tempBag = 10000
    seventy = tempBag * 3
    thirty = bag * 3
    value = (0.7 * seventy) + (0.3 * thirty)
    expectedValue = value - bag
    if expectedValue > maxValue:
        bagAtMax = bag
        maxValue = expectedValue
    print(bag, expectedValue)
    valuesArray[bag] = expectedValue


print(bagAtMax, maxValue)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(valuesArray)
ax.annotate(xytext=(4000, 20200), s="(10000, 20000)", xy=(10000, 20000))
ax.set_ylabel("Expected Return")
ax.set_xlabel("Bells Put Into Hole")
ax.set_title("Money Tree Optimization")

plt.show()
