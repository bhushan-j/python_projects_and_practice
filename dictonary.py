'''
values with unique keys
Dictionaries Similar to list but cant join like lists
dictionaries are surrounded with {}
'''
age_data={'john':'18','smith':'20','sam':'21','ray':'19'}
print(age_data['sam'])#this will print 21
del age_data['sam']
age_data['mark']='23'
print(age_data)
print(len(age_data))
print(age_data.get("mark"))