#!/usr/bin/python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

import sys
import random
import struct

class reslp:
    lastOutput = 0
    momentum = 0

    def reslp(this,samp):
        distanceToGo = samp - this.lastOutput;
        this.momentum += distanceToGo * 0.125 # * 0.0001
        this.lastOutput += this.momentum + distanceToGo * 0.125
        return this.lastOutput * 0.7

r = reslp()
x = y = []

t = np.arange(0, 44100, 1)

for f in range (0,4410, 10):
    s = [math.sin(2 * np.pi * (sam/44100.0) * f) for sam in t]
    fr = [r.reslp(sam) for sam in s]
    sq = [sam*sam for sam in fr]
    rms = math.sqrt(sum(sq)/len(sq))
    x.append(f)
    y.append(rms)
    print("Frequency %f | Amplitude %f"%(f, rms))

nx = np.array(y)
ny = np.array(y)

fig, ax = plt.subplots()
ax.plot(nx, ny)

ax.set(xlabel='frequency', ylabel='amplitude',
       title='Frequency response')
ax.grid()

plt.show()
