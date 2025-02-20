#! /usr/bin/env python3

import os

file = input("Enter a file name: ")

if os.path.isfile(file):
     print("The file exists.")
else:
     print("The file does not exist.")
     print("Creating it...")
     os.system('touch {}'.format(file))
