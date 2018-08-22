#!/usr/bin/python3

# test: ./reslp.py | play -t raw -r 22100 -e float -b 32 -
# source: https://beammyselfintothefuture.wordpress.com/2015/02/16/simple-c-code-for-resonant-lpf-hpf-filters-and-high-low-shelving-eqs/

import sys
import random
import struct


class reslp:
    lastOutput = 0
    momentum = 0

    def reslp(this,samp):
        distanceToGo = samp - this.lastOutput;
        this.momentum += distanceToGo * 0.125 * i * 0.0001
        this.lastOutput += this.momentum + distanceToGo * 0.100
        return this.lastOutput * 0.7

r1 = reslp()
r2 = reslp()

saw1 = saw2 = 0

while True:

    for i in range(2205, 8820):
        saw1 = (saw1-1)%400
        saw2 = (saw2-1)%403
        samp = (saw1+saw2)/800
        #samp = random.random()
        samp = r2.reslp(r1.reslp(samp))
        sys.stdout.buffer.write(struct.pack("f", samp))
    for i in range(8820, 2205,-1):
        saw1 = (saw1-1)%400
        saw2 = (saw2-1)%403
        samp = (saw1+saw2)/800
        #samp = random.random()
        samp = r2.reslp(r1.reslp(samp))
        sys.stdout.buffer.write(struct.pack("f", samp))
