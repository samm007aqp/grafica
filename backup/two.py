import cv2
import math
import numpy as np
from matplotlib import pyplot as plt


def Calculate_C(greatest,BASE):
    return  255/math.pow(BASE,greatest)
                

def Exp_Ope(C,BASE,x):
    return C*(math.pow(BASE,x)-1)
    
def OperadorExponencial(filename):
    img = cv2.imread(filename)
    output = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    row,cols = output.shape
    total = row*cols
    gre= np.amax(output)
       
    count = 0 
    for i in range (row):
        for j in range(cols):
            val =  0.063*math.pow(output[i][j],1.5)
            if val > 255:
                output[i][j] = 255
                count = count +  1
            
            else:
                output[i][j] = val
      
    cv2.imwrite('static/images/upload/salida.jpg',output)



