my_dict = {'Dima': 20012001, 'Anya': 14082001 }
print(my_dict)
print(my_dict['Dima'])
my_dict = {'Maksim': 30072003}
print(my_dict)
my_dict.update({'Svetlana': 31071987,
                'Ruslan': 3091997,
                'Andrey': 21041986,
                'Denis': 25081979})
print(my_dict)
del my_dict['Svetlana']
del my_dict['Ruslan']
print(my_dict)
print(my_dict.get('Svetlana', 'Такого ключа нет'))
print(my_dict.get('Ruslan', 'Такого ключа нет'))
print(my_dict)
my_set = {5,5,6,8,8, 'Ruslan','Ruslan', True, (2,3,4)}
print(my_set)
my_set.update({2,3,3,4,4, 'Apple'})
print(my_set)
my_set.discard((2,3,4))
print(my_set)