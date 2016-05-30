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
