# -*- coding: UTF-8 -*-
import cv2
import sys
import os.path

def detect(inputpath,outputpath,filename, cascade_file = "./lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(inputpath+'/'+filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))

    #print (faces)   
    if not os.path.exists(outputpath):#如果路径不存在
        os.makedirs(str(outputpath))                        
    for (x, y, w, h) in faces:
        cv2.imwrite(outputpath+filename+".png", image[y:y+h,x:x+w])


def main():
    for j in range (18,2000):
        dirl = os.listdir("./image/"+str(j))
        for i in dirl:
            outpath = "./outimage/" + str(j) + "/"
            detect("./image/"+str(j),outpath,i)

if __name__ == '__main__':
    main()