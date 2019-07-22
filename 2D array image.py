import numpy as np
from PIL import Image


def lighten(im,l):

    br = False
    a = np.array(im)
    
    a = a * l
    b = (a > 255)
    
    if len(a[b]) > 0:
        br = True
        a[b] = 255

    Image.fromarray(a).show()

    return br


def flip(im):
    
    a = np.array(im)
    

    for z in range(len (a)):
        a[z]=a[z][::-1]
    #print (a[3])
    return Image.fromarray(a)


def clip(im,MaxVal):

    a = np.array(im)
    
    b = (a > MaxVal)
    
    if len(a[b]) > 0:
        
        a[b] = MaxVal

    return Image.fromarray(a)
    


im = Image.open("2d.bmp")

#im.show()

if im.mode != "L":
    im = im.convert("L")
    #im.show()

#imarray = np.asarrary(im)
burn = False
burn = lighten(im,1.1)
if burn:
    print ("the resultant image is 'burnt out'")


flip(im).show()

clip (im,120).show()




