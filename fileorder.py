import os
import sys
os.chdir("/home/sushant/yolov3cd/yolov3/images/")
filenames = os.listdir(os.getcwd())

outfile = open("/home/sushant/yolov3cd/yolov3/12train.txt","wb")
content = ""

for file in filenames:
    path = "/home/sushant/rogued/yolov3cd/images/" + file[:len(file)-4] + ".jpg"
    content = content + file + "\n"
# files corresponding to each row in train and test to be taken and put in one file    
#    box = ""
#    with open(file) as f:
#        box = f.read()
#        f.close()
    
#    nums = box.split(' ')
#    a = float(nums[1])
#    b = float(nums[2])
#    c = float(nums[3])
#    d = float(nums[4][:len(nums[4])-2])
    #print(str(int(d))+path)
#    content = content + path + " " + str(round(a)) + "," + str(round(b)) + "," + str(round(c)) + "," + str(round(d))  
#    content = content + path "\n"
outfile.write(str.encode(content))
outfile.close()