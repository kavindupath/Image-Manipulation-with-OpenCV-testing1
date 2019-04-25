#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[16]:


color1=[255,0,0] #red
color2=[0,255,0] #green
color3=[0,0,255] #blue
color4=[127,127,127] #gray
plt.imshow(np.array([[color1,color2],[color3,color4]]))


# In[18]:


image=cv2.imread("C:/Users/kavindu/Pictures/test.jpg")


# In[19]:


type(image)


# In[20]:


image.shape


# In[21]:


plt.imshow(image)


# In[22]:


# By defaulr Opencv is not using the RGB color model. It uses BGR model instead.That is why the image above has changed

# Transform from BGR to RGB
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)


# In[23]:


grayimage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.imshow(grayimage)


# In[26]:


#resize a image
width=100
height=100
resize=cv2.resize(image,(width,height))
plt.imshow(resize)


# In[28]:


# Drawing on a image
cv2.putText(image,"Bolakumari bordima",(70,270),cv2.FONT_HERSHEY_SIMPLEX ,0.8,(20,240,150),2)
plt.imshow(image)


# In[ ]:




