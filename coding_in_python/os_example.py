#! /usr/bin/env python3

import os

print("Your current working directory is: " + os.getcwd() + "\n\n")
print("The contents of this directory are: ")
os.system('ls')

os.rename("first.txt", "second.txt")
