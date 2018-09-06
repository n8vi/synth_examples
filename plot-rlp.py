#!/usr/bin/python3

# Resonant lowpass filter based on code from
# https://beammyselfintothefuture.wordpress.com/2015/02/16/simple-c-code-for-resonant-lpf-hpf-filters-and-high-low-shelving-eqs/

# This is a slow script for visually characterizing filters.  It is meant to be slow and simply written, as its purpose
# is purely pedagogical.

import matplotlib.pyplot as plt
import math

import sys
import random
import struct

class reslp:
    lastOutput = 0
    momentum = 0

    def __init__(this,freq=0.125,res=0.125):
        this.freqv = freq
        this.resv = res

    def reslp(this,samp):
        distanceToGo = samp - this.lastOutput;
        this.momentum += distanceToGo * this.freqv
        this.lastOutput += this.momentum + distanceToGo * this.resv
        return this.lastOutput * 0.7

fig, ax = plt.subplots()
ax.grid()
ax.set(xlabel="frequency", ylabel="amplitude", title="Frequency Response")

for fv in range(5, 90, 10):
    r = reslp(fv*0.009, fv*0.0009)
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

    ax.plot(xvals,yvals)
    plt.pause(0.05)

plt.show()
