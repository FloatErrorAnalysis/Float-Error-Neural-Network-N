import os
from subprocess import Popen, PIPE


def generate_bytecode(path):
    # read into files
    files = os.listdir(path)

    for f in files:
        if os.path.isfile(path + '/' + f):
            # get filename without extension
            index = f.rfind('.')
            name = f[:index]

            # def ll&bc dir
            dir_ll = '../../cpp_ll/'
            dir_bc = '../../cpp_bc/'

            # use llvm-clang to compile the source file
            exe_cmd('clang -O0 -emit-llvm ' + path + f + ' -S -o ' + dir_ll + name + '.ll')
            exe_cmd('llvm-as ' + dir_ll + name + '.ll -o ' + dir_bc + name + '.bc')


def exe_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    p.wait()

    if p.returncode != 0:
        print('Error : ' + cmd)
        return -1


if __name__ == '__main__':
    print(os.getcwd())
    generate_bytecode('../cpp_raw/')
