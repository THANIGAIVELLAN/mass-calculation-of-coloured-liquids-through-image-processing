import cv2
import numpy as np
import matplotlib.pyplot as plt

g=0
avg=0
massc=[]
pixc=[]
#path="full.png"
plt.xlabel("MASS")
plt.ylabel("PIXEL COUNT")
while (1):
        capture = cv2.VideoCapture(1)

        #define the resolution size....
        def make_1080p():
                capture.set(3,1920)
                capture.set(4,1080)


                #return frame by frame.....
        ret,frame = capture.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #plt.imshow(gray)
        #plt.show()
                
        
        capture.release()

        #plt.imshow(gray)
        #plt.show()

        #img=cv2.imread(path)

        #out_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        out=np.array(gray)

        
        count=0
        COUNT2=0
        for i in range(480):
            for j in range(640):
                if out[i][j]<=150 and out[i][j]>=130:
                    count+=1

        print("PIXEL COUNT",count)
        g=g+1
        avg=count

        ma=115320

        #print(avg/30)
        #d=avg/3
        val=500*avg
        #print(val)
        res=val/ma
        print("\n\nVOLUME OF THE GIVEN LIQUID IS:",round(res,3)," ml")
        density=0.910
        mass=density*res
        massc.append(mass)
        pixc.append(count)
        if(mass>420):
                plt.plot(massc,pixc)
                plt.show()
                break



ma=98953

#print(avg/30)
#d=avg/3
val=500*avg
#print(val)
res=val/ma
print("\n\nVOLUME OF THE GIVEN LIQUID IS:",round(res,3)," ml")
density=0.970
mass=density*res

print("\n\nMASS  OF THE GIVEN LIQUID IS:",round(mass,3),"g")
        


