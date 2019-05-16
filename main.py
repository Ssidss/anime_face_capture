# -*- coding: UTF-8 -*-
import cv2
import os
import sys

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
  
    if not os.path.exists(outputpath):
        os.makedirs(str(outputpath))                        
    for (x, y, w, h) in faces:
        cv2.imwrite(outputpath+filename+".png", image[y:y+h,x:x+w])
  
def set_path():
    for j in range (0,maxdir):
        dirl = os.listdir("./image/"+str(j))
        for i in dirl:
            outpath = "./outimage/" + str(j) + "/"
            detect("./image/"+str(j),outpath,i)
        print ("%d Done!"%(j))



def main(videoname) :
    cap = cv2.VideoCapture(videoname)#名为'003.mp4'的文件
    if False == cap.isOpened():
        sys.stderr.write("file \"%s\" is not exist\n"%(videoname))
        sys.exit(-1)
    c=0                             #文件名从0开始
    maxdir = 0 
    global maxdir
    while(1):
        # get a frame
        ret, frame = cap.read()
        if frame is None :
            break
        # show a frame
        #cv2.imshow("capture", frame)
        cc = c/2000
        if  not os.path.exists('./image/'+str(cc)):#如果路径不存在
            os.makedirs('./image/'+str(cc))
            maxdir = cc
        if c%30==0 :
            cv2.imwrite('./image/'+str(cc)+'/'+str(c) + '.jpg',frame) #存储为图像 
            if c%1000 == 0:       
                print ("%d write done! "%(c))
        c=c+1
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("usage: detect.py <filename>\n")
        sys.exit(-1)
    main(sys.argv[1])
    print ("Start to detect face")
    set_path()
