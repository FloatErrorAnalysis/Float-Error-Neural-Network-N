import os
import csv
import operator
import numpy as np
from py.util.BCTool import generate_bytecode

cpp_dir_path = '../../cpp_raw/add/'
ll_dir_path = '../../cpp_bc/'


def generate_ll():
    lls = []
    generate_bytecode(cpp_dir_path)
    for ll in sorted(os.listdir(ll_dir_path)):
       # print(ll)
       #  with open(ll_dir_path + ll, 'rb') as f:
       #      lls.append(f)
        with open(ll_dir_path + ll, 'rb') as f:
            byte = f.read(1)
            bytes = []
            while byte:
                byte = f.read(1)
                bytes.append(byte)
            lls.append(bytes)

    return lls


def generate_error():
    error_list = []
    for f in sorted(os.listdir('/root/tmp/dataset/')):
        if f.split('.')[-1] == 'csv':
           # print(get_top5(f))
            error_list.append(get_top5(f))
    return error_list


def get_top5(csv_name):
    reader = csv.reader(open('/root/tmp/dataset/' + csv_name), delimiter=',')
    data_list = dict(reader)
    for k, v in data_list.items():
        data_list[k] = float(v)
    sorted_list = sorted(data_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list[:5]


def read_data():
    lls = generate_ll()
    errors = generate_error()
    print('Length of ll: ' + len(lls))
    lls = np.array(lls)
    errors = np.array(errors)
    print("shape of lls: {}\tshape of errors: {}".format(lls.shape, errors.shape))
    return lls, errors


if __name__ == '__main__':
    read_data()