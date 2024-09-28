first = input('Enter first number:')
second = input('Enter second number:')
print('Before swapping:', first, second)
first = second 
second = first
print('After Swapping:', first, second)
# Above is an ecample of something that doesnt work. we will dive into a methond that actually does work.
first = input('Enter first number:')
second = input('Enter second number:')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After Swapping:', first, second)
# this method worked !- but now theres a even easiler method to the equation. 
first = input('Enter first number:')
second = input('Enter second number:')
print('Before swapping:', first, second)
first, second = second, first
print('After Swapping:', first, second)
# now you and do the same with lists elements. 
top_cities = ['New York City', 'Los Angeles', 'Chicago','Houston','Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)
# not in alpahbetical order - we will using the sort function. 
top_cities = ['New York City', 'Los Angeles', 'Chicago','Houston','Phoenix']
top_cities.sort()
print(top_cities)
#same logic can be applied to number 
random_numbers = [2,5,0,-3,4]
random_numbers.sort()
print(random_numbers)
#now in the resevse order | Remmber that Sort()- is a method.. it changes the list it belongs to. 
random_numbers = [2,5,0,-3,4]
random_numbers.sort(reverse=True)
print(random_numbers)
#now giving the difference between sort and shorted- Sort : sorts the orginal list WHEREAS sorted(list_name): gives back the new , sorted list,keeps the original unchanged. 
top_cities = ['New York City', 'Los Angeles', 'Chicago','Houston','Phoenix']
print(sorted(top_cities))
print(top_cities)