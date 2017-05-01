"""
This script merges files and creates a new text file with current date as name
"""
import datetime
import os

file_list =os.listdir()

new_filename =datetime.datetime.now().strftime("%Y-%m-%d")+".txt"
with open(new_filename,"w+") as file_object:

    for item in file_list:
        if ".txt" in item:
            filename=item

            with open(filename,"r") as file_object2:
                content=file_object2.read()
                file_object.write(content+"\n")
