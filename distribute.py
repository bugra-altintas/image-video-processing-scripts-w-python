import os
import random

#change directory to desktop
os.chdir("/Users/bugra/Desktop")

names = ["bugra","ayberk","berke","tayyip","mehmet"]

#make 5 directories if they don't exist
for n in names:
    os.system(f"mkdir {n}")

#list all files in the directory
files_new = os.listdir("./frames-new2")

#list all files in the directory
files_old = os.listdir("/Users/bugra/Desktop/Video Frames/rgbimages")




for n in names:
    #select 10 random files from the directory
    random_files = random.sample(files_old, 4)
    #select 10 random files from the directory
    random_files2 = random.sample(files_new, 6)
    for i in random_files:
        os.system(f"cp /Users/bugra/Desktop/Video\ Frames/rgbimages/{i} /Users/bugra/Desktop/{n}/{i}")

    #copy the files to the new directory
    for i in random_files2:
        os.system(f"cp /Users/bugra/Desktop/frames-new2/{i} /Users/bugra/Desktop/{n}/{i}")

    #zip the directory
    os.system(f"zip -r {n}.zip {n}")
