"""
This script handles files
"""
file_object = open("example.txt","r")
content = file_object.readlines()
# content = [i.rstrip("\n")for i in content] this line removes \n in all contents of the list called loop of comprehension
j=0
for i in content:
    content[j]=i.rstrip("\n")
    j+=1
#file_object.close()
"""
Method to create a text file from list
"""
content_newfile = content
content_newfile[0]="Hello "
file_new_object = open("mytext.txt","w")

content_newfile=[j.ljust(7,"\n")for j in content_newfile]
file_new_object.writelines(content_newfile)
"""
Method to create a text file directly
"""
lst =["Line1","line2","line3"]
file2_object =open("text.txt","w")
for i in lst:
    file2_object.write(i+"\n") #appending \n to each element in list
file2_object.close()

"""
Appending to a file
"""
