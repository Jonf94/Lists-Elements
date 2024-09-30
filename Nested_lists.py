numbers = [1,2,3,4]
countries = ['UK','US','Germany']
# this is not recommended to do.
countries = [1,'UK',2,'US']
cells = [['A1','A2','A3'], ['B1','B2','B3']]
print(cells[0])
print(cells[0][0])

print(cells[0][1])
print(cells[1][2])

cells = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cells:
    print('Element:',x)

cells = [['A1','A2','A3'], ['B1','B2','B3']]
for x in cells:
    for y in x:
        print('Element',y)

table = [['A1','A2','A3'], ['B1','B2','B3']]
for row in cells:
    for cell in x:
        print('Element',cell)

table = [['A1','A2','A3'], ['B1','B2','B3']]
for row in cells:
    for cell in row:
        print(cell, '', end='')
    print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

table = [i for i in range(1,6)]
print(table)

table = [[i for i in range(1,6)] for j in range(4)]
print(table)