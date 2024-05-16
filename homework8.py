def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('ok')
print_params(7, 25, [1, 2, 3])
print_params(9, 4)


values_list = [7, 'dog', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}


def print_params(*params):
    print(*params)


print_params(values_list)
print_params(*values_list)


def print_params(**params):
    print(params)


print_params(**values_dict)


values_list_2 = ['dog', 85]


def print_params(params):
    print(params)


print_params(*values_list_2, 42)


