name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original,name_new)

list_original = [1,2,3]
list_new = list_original
list_original[0] = -5
print('original:',list_original,'\nnew:',list_new)
#this is how u make copying made idendendant from line line to the next. 
list_original = [1,2,3]
list_new = list_original[:]
list_original[0] = -5
print('original:',list_original,'\nnew:',list_new)

list_original = [1,2,3]
list_new = list_original[:2]
list_original[0] = -5
print('original:',list_original,'\nnew:',list_new)