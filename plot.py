#!/usr/bin/python3

import matplotlib.pyplot as plt
import math

import sys
import random
import struct

class reslp:
    lastOutput = 0
    momentum = 0

    def reslp(this,samp):
        distanceToGo = samp - this.lastOutput;
        this.momentum += distanceToGo * 0.125
        this.lastOutput += this.momentum + distanceToGo * 0.125
        return this.lastOutput * 0.7

r = reslp()
xvals = []
yvals = []

t = range(0, 44100)
k = 1

for f in range (0,8820, 50):
    s = [k*math.cos(2 * math.pi * (sam/44100.0) * f) for sam in t]
    fr = [r.reslp(sam) for sam in s]
    sq = [sam*sam for sam in fr]
    rms = math.sqrt(sum(sq)/len(sq))
    xvals.append(f)
    yvals.append(rms)
    print("Frequency %f | Amplitude %f"%(f, rms))
    k = math.sqrt(2)

fig, ax = plt.subplots()
ax.plot(xvals,yvals)
ax.set(xlabel="frequency", ylabel="amplitude", title="Frequency Response")
ax.grid()
plt.show()
