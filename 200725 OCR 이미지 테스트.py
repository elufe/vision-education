#!/usr/bin/env python
# coding: utf-8

# In[76]:


get_ipython().system(' pip install pytesseract')


# In[56]:


from PIL import Image
from pytesseract import *
import re
import cv2


# In[57]:


img = Image.open('ocr_test.jpg')


# In[78]:


text = pytesseract.image_to_string(img, lang = 'kor+eng')
print(text)
#text


# In[59]:


size_table = re.split('\n',text)
size_table


# In[60]:


matchers = ['사이즈(','어깨너비','가슴둘레','소매길이','출장']
size = [s for s in size_table if any(xs in s for xs in matchers)]
size


# In[61]:


size[0]


# In[62]:


size[1][57:]


# In[63]:


size[2][25:]


# In[64]:


size[3][42:]


# In[65]:


size[4]


# In[66]:


size2 = []

size2.append(size[0])
size2.append(size[1][57:])
size2.append(size[2][25:])
size2.append(size[3][42:])
size2.append(size[4])

size2


# In[67]:


for i in range(len(size2)):
    size2[i] = re.sub('     ',' ', size2[i])
    size2[i] = re.sub('    ',' ', size2[i])
    size2[i] = re.sub('   ',' ', size2[i])
    size2[i] = re.sub('  ',' ', size2[i])
    size2[i] = re.sub(' ',' ', size2[i])
    
size2


# In[68]:


size3 = []

for i in range(len(size2)):
    size3.append(size2[i].split(' '))
    
size3


# In[69]:


import numpy as np
size4 = np.array(size3)
size4


# In[70]:


size4.T


# In[71]:


import pandas as pd


# In[72]:


df = pd.DataFrame(size4.T)
df


# In[73]:


df.loc[[1,2,3]]


# In[74]:


df2 = df.loc[[1,2,3]]
df2.columns = ['사이즈', '어깨너비', '가슴둘레', '소매길이', '출장']
df2


# In[75]:


df2['사이즈'] = df2['사이즈'].astype(int)
df2


# In[ ]:




