import os
test_file = open("mytest.txt","wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("This is my first line\n",'UTF-8'))
test_file.close

test_file= open("mytest.txt","r+")
text_in_file=test_file.read()
print(text_in_file)



os.remove("mytest.txt")

