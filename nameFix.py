import os
import sys


folder = sys.argv[1]
os.chdir(folder)

for i in os.listdir("."):
    name = i[0:6] + ".txt"
    os.rename(i,name)

