#! /usr/bin/env python3

myfile = "file.txt"
try:
     file = open(myfile, "r")
except FileNotFoundError as e:
     print("The file was not found.")
     print(e)
     exit(1)
for line in file:
     print(line)
