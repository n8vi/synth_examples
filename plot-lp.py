#!/usr/bin/python3

# Lowpass filter based on code from
# https://beammyselfintothefuture.wordpress.com/2015/02/16/simple-c-code-for-resonant-lpf-hpf-filters-and-high-low-shelving-eqs/

# This is a slow script for visually characterizing filters.  It is meant to be slow and simply written, as its purpose
# is purely pedagogical.

import matplotlib.pyplot as plt
import math

import sys
import random
import struct

class lp:
    lastOutput = 0

    def lp(this,samp):
        distanceToGo = samp - this.lastOutput;
        this.lastOutput += distanceToGo * 0.125
        return this.lastOutput * 0.7

l = lp()
xvals = []
yvals = []

t = range(0, 44100)
k = 1

for f in range (0,8820, 50):
    s = [k*math.cos(2 * math.pi * (sam/44100.0) * f) for sam in t]
    fr = [l.lp(sam) for sam in s]
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
