
# coding: utf-8

# In[ ]:




# In[63]:

import pandas
df1=pandas.read_csv("supermarkets.csv")
df1.set_index("ID")
df1.to_csv("supermarkets.csv")


# In[62]:



