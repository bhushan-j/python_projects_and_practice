shopping_list = ['apple', 'juice', 'tomatoes', 'oats']
print("first item", shopping_list[0])
print("Second item", shopping_list[1])
print("third item", shopping_list[2])
print("forth item", shopping_list[3])
print("last item", shopping_list[-1])
print("second last item", shopping_list[-2])
print("multiple items", shopping_list[1:3])
other = ['movie', 'dinner']
day_schedule = [shopping_list, other]
print(day_schedule)
print("this third item from first list is:",(day_schedule[0][2]))
print("this last item from second list is:",(day_schedule[1][-1]))
day_schedule.append('Gym') # this will add item in the last position
print("my schedule :", day_schedule)
day_schedule.insert(1, "coffee")
print("my schedule :", day_schedule)
day_schedule.remove("coffee")
print("my schedule :", day_schedule)



'''OUTPUT:
first item apple
Second item juice
third item tomatoes
forth item oats
last item oats
second last item tomatoes
multiple items ['juice', 'tomatoes']
[['apple', 'juice', 'tomatoes', 'oats'], ['movie', 'dinner']]
this third item from first list is: tomatoes
this last item from second list is: dinner
my schedule : [['apple', 'juice', 'tomatoes', 'oats'], ['movie', 'dinner'], 'Gym']
my schedule : [['apple', 'juice', 'tomatoes', 'oats'], 'coffee', ['movie', 'dinner'], 'Gym']
my schedule : [['apple', 'juice', 'tomatoes', 'oats'], ['movie', 'dinner'], 'Gym']

'''