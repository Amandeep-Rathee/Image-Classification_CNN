

from PIL import Image
import numpy as np
import sys
import os
import csv

myDir='D:\Data for test\combined'
# default format can be changed as needed
def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    labels = []
    names = []
    keywords = {"B" : "1","C": "2", "S": "3"} # keys and values to be changed as needed
    for root, dirs, files in os.walk(myDir, topdown=True):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
            for keyword in keywords:
                if keyword in name:
                    labels.append(keywords[keyword])
                else:
                    continue
            names.append(name)
    return fileList, labels, names

myFileList, labels, names  = createFileList(myDir)
i = 0
for file in myFileList:
    print(file)
    img_file = Image.open(file)
    img_file = img_file.resize((32,32))
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    img_grey = img_file.convert('RGB')
 
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((width, height, 3))
    value = value.flatten()
    
    value = np.append(value,labels[i])
    i +=1
    
    print(value)
    with open("DS4.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)