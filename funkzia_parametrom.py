def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 2, b = 3)
print_params(c = 3)
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [1, True, 'stroka']
values_list_2 = [5, 'True', False]
values_dict = {'a': 1, 'b': 2, 'c':5}
print_params(*values_list)
print_params(**values_dict)
#print_params(*values_list_2, 42) #это не работает