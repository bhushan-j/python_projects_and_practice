import random
random_num=random.randrange(0,500)
while random_num !=10:
    print(random_num)
    random_num=random.randrange(0,500)
# this will print all even numbers between 0 to 50
i=0
while (i <= 50):
    if (i%2 == 0):
        print(i)
    elif(i == 50):
        break
    else:
        i +=1
        continue
    i+=1