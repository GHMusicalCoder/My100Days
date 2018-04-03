from itertools import islice
import sys
sys.path.append('/home/chris/PycharmProjects/My100Days/extra_files/')

import my_100days_library as mylib

dict_State = mylib.us_state_abbrev
list_State = mylib.states_list

print('First we will print both the list and dictionary as it was imported.')
print('-' * 60)

print('List View:')
print(*list_State, sep=' * ')
print(*[key for key in dict_State.keys()], sep=' * ')

print('-' * 60)


# now the assignments
print('Now we will print out the 10th element in each collection')
print('10th item in the list: ', list_State[9])

dict_list_States = [key for key in dict_State.keys()]
print('10th item in the dictionary: {0} - {1}'.format(dict_list_States[9], dict_State.get(dict_list_States[9])))
print('-' * 60)
print('Now we will print out the 45th key in the dictionary')
print('45th key in the dictionary is ', dict_list_States[44])

print('-' * 60)
print('Now we will print out the 27th value in the dictionary')
print('2th value in the dictionary is ', dict_State.get(dict_list_States[26]))

print('-' * 60)
print('Now to replace the 15th key in the dictionary with the 28th item in the list')
print('the 15th key is ', dict_list_States[14])
print('and the 28th item is ', list_State[27])
dict_State[list_State[27]] = dict_State.pop(dict_list_States[14])
dict_list_States = [key for key in dict_State.keys()]
print('and now the 15th key is ', dict_list_States[14])