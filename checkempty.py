import os
import sys
os.chdir("/home/sushant/yolov3cd/yolov3/more/labels/")
filenames = os.listdir(os.getcwd())

for file in filenames:
    with open(file) as myfile:
        myfile.seek(0)
        firstc = myfile.read(1)
        if not firstc:
            print(file)
