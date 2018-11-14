# -*- coding: utf-8 -*-

import re
input_reg = input('Enter expression, ex.: + 2 3: ')
input_pattern = r'[+\-*/][ ]\d[ ]\d'
match = re.fullmatch(input_pattern, input_reg)
if not match:
    print('enter expression with spaces like this: + 2 3')
else:
    input_list = []
    for i in input_reg:
        input_list.append(i)
    input_list[0], input_list[2] = input_list[2], input_list[0]
    input_list = ''.join(input_list)
    try:
        print(eval(input_list))
    except ZeroDivisionError:
        print('Error ! Divizion by zero')
    else:
        assert (eval(input_list) > 0), 'result is negative'
