##library package
import cv2
import os
from matplotlib import pyplot as plt

##define path where your input images available
input_path=r'C:\Users\rajeev\Desktop' ##it is optional
os.chdir(input_path)


#read images from yout input path
img=cv2.imread("map.jpg")

##write images on your path
cv2.imwrite('out_put_map.jpg',img)


##show images
cv2.imshow('Image',img)
cv2.waitKey()
cv2.destroyAllWindows()


##show on screen
plt.imshow(img)
plt.show()

