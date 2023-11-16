#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:54:12 2022

@author: Januario Cipriano
"""

import os
import threading
import multiprocessing as mp


def cpu_waster():
	while True:
		pass


print('Hi! My name is', __name__)
if __name__=='__main__':
	print('Process ID:', os.getpid())
	print('Thread Count:', threading.active_count())
	for thread in threading.enumerate():
		print(thread)

	print('Starging 12 CPU Wasters...')
	for i in range(12):
		mp.Process(target=cpu_waster).start()

	print('Process ID:', os.getpid())
	print('Thread Count:', threading.active_count())
	for thread in threading.enumerate():
		print(thread)









































