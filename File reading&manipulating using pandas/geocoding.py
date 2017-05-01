
# coding: utf-8

# In[350]:

"""
This is a geocoding exercise to add latitudes and longitudes to a Dataframe 
"""
import pandas
import os 
from geopy.geocoders import Nominatim
nom = Nominatim()
os.listdir()


# In[351]:

df1=pandas.read_csv("supermarkets.csv")
df1=df1.set_index("ID")
df1


# In[352]:


df1.ix[df1.index[0:6],df1.columns[1:4]]


# In[353]:

df1["Latitudes"]=df1.shape[0]*[" "]
df1["Longitudes"]=df1.shape[0]*[" "]
df1


# In[354]:

df1["Address"]=df1["Address"]+", "+df1["City"]+", "+ df1["State"]

#Run this only once , dont run it again

    


# In[355]:

for i in range(0,6):
    result=nom.geocode(df1.ix[df1.index[i],df1.columns[1]])
    if result!=None:#We wrote a condition because the geo code object at place 2 is a none object
        
        df1.ix[df1.index[i],"Latitudes"]=result.latitude
        df1.ix[df1.index[i],"Longitudes"]=result.longitude
    else:#The else none statement will store a Nothing if the geocode object is None 
        None
df1
        
        
    


# In[348]:

#The other way of implementing the same code above 
df1["Codinates"]=df1["Address"].apply(nom.geocode)
df1["Latitudes"]=df1["Codinates"].apply(lambda x: x.latitude if x!=None else None)
df1["Longitudes"]=df1["Codinates"].apply(lambda x: x.longitude if x!=None else None)
df1

