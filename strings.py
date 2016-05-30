my_string="Hello everyone !!! I am enjoying my python practice"
print(my_string[0:5])#Hello
print(my_string[-8:])#practice
print(my_string[0:-8])#Hello everyone !!! I am enjoying my python
print(my_string+" because i like coding")#Hello everyone !!! I am enjoying my python practice because i like coding
print(my_string.capitalize())#Hello everyone !!! i am enjoying my python practice
print(my_string.find("python"))#36
print(len(my_string))#51
print(my_string.replace("practice","coding"))#Hello everyone !!! I am enjoying my python coding

list=my_string.split(" ")
print(list)