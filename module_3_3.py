def print_params(a = 1, b = 'Artyom', c = True):
    print(a, b, c)

print_params(1, 'Artyom', True)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [8, 'Robin', False]
values_dict = {'a':19, 'b':'Tatyana','c':False}
print_params(**values_dict)
print_params(*values_list)

values_list_2 = [54.32, 'Anton']
print_params(*values_list_2, 42)