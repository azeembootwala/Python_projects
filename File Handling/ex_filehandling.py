def celcius_to_farhenheit(celcius):
    if celcius<-273.15:
        print("are you crazy !!!")
    else:
        farhenheit = celcius*(9/5)+32
        return farhenheit
list_celcius=[]
list_farhenheit=[]
j=0
for item in range(0,4):
    temperature = float(input("Enter temperature in degree celcius:- "))
    list_celcius.insert(item,temperature)
    temperature_farn = celcius_to_farhenheit(temperature)
    if type(temperature_farn)!=float:
        k=0
    else:
        list_farhenheit.insert(j,temperature_farn)
        j+=1
with open("temperature_file.txt","w+") as file_object:
    for i in list_farhenheit:
        file_object.write(str(i)+"\n")
