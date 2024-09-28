top_cities = ['New York', 'Los Angeles', 'Chicago','Houston','Phoenix']
for city in top_cities:
    print('Current city:', city)

# remember that len - returns the number of charaters. 
top_cities = ['New York', 'Los Angeles', 'Chicago','Houston','Phoenix']
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index],)

# Want to sum up all numbers and print out the total amount spent
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent', sum)