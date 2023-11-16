#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:49:23 2022

@author: Januario Cipriano
"""

import os
import threading


def cpu_waster():
	while True:
		pass

print('Process ID:', os.getpid())
print('Thread Count:', threading.active_count())
for thread in threading.enumerate():
	print(thread)

print('Starting 12 CPU Wastres...')
for i in range(12):
	threading.Thread(target=cpu_waster).start()


print('Process ID:', os.getpid())
print('Thread Count:', threading.active_count())
for thread in threading.enumerate():
	print(thread)






























