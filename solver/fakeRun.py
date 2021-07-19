#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FakeRun
import sys


tam = len(sys.argv)

arq = open(sys.argv[1].replace("padoca","prun").replace("PadocaInstances","PadocaRuns"),"a+", encoding="utf-8")

arq.write("fake write\n")

a = 0
for i in range(9999):
        a += 1

print("aaaaa")