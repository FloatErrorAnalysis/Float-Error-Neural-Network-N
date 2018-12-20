import os
import csv
import operator
import numpy as np

ll_dir_path = '../../cpp_bc/'
x = 145
y = 16


def print_hex(my_byte):
    string = [hex(int(i)) for i in my_byte]
    print(" ".join(string))


def get_ll(path):
    lls = []
    for ll in sorted(os.listdir(ll_dir_path + path)):
        with open(ll_dir_path + path + ll, 'rb') as f:
            byte_array = []
            n = 0
            while n < x * y:
                byte = f.read(1)
                if byte:
                    byte_array.append(byte)
                else:
                    byte_array.append(b'00')
                n = n + 1
            lls.append(byte_array)
    return lls


def get_all_ll():
    return get_ll('add/') + get_ll('mul/')


def get_error(path):
    error_list = []
    for f in sorted(os.listdir('../../dataset/' + path)):
        if f.split('.')[-1] == 'csv':
            error_list.append(get_top5_input(path + f))
    return error_list


def get_all_error():
    return get_error('add/') + get_error('mul/')


def get_top5_input(csv_name):
    reader = csv.reader(open('../../dataset/' + csv_name), delimiter=',')
    data_list = dict(reader)
    for k, v in data_list.items():
        data_list[k] = float(v)
    sorted_list = sorted(data_list.items(), key=operator.itemgetter(1), reverse=True)
    # only use the input
    return [input[0] for input in sorted_list[:5]]


def read_data():
    lls = get_all_ll()
    errors = get_all_error()
    lls = np.array(lls)
    errors = np.array(errors)
    print('shape of lls: {}\tshape of errors: {}'.format(lls.shape, errors.shape))
    return lls, errors