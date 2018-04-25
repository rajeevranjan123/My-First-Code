
# coding: utf-8

# In[18]:


##library package
import cv2
import os
from matplotlib import pyplot as plt


# In[13]:


##define path where your input images available
input_path=r'C:\Users\rajeev\Desktop' ##it is optional
os.chdir(input_path)


# In[14]:


#read images from yout input path
img=cv2.imread("map.jpg")


# In[16]:


##write images on your path
cv2.imwrite('out_put_map.jpg',img)


# In[17]:


##show images
cv2.imshow('Image',img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[20]:


##show on screen
plt.imshow(img)
plt.show()

