import os
import time
from subprocess import Popen, PIPE


class BitCodeGenerator:

    def generate_bitcode(self, path):
        # read into files
        files = os.listdir(path)

        for f in files:
            if os.path.isfile(path + '/' + f):
                # get filename without extension
                index = f.rfind('.')
                name = f[:index]

                # def ll&bc dir
                dir_ll = './data/ll/'
                dir_bc = './data/bc/'

                # use llvm-clang to compile the source file
                self.exe_cmd('clang -O0 -emit-llvm ' + path + f + ' -S -o ' + dir_ll + name + '.ll')
                time.sleep(0.2)
                self.exe_cmd('llvm-as ' + dir_ll + name + '.ll -o ' + dir_bc + name + '.bc')
                time.sleep(0.2)

    def exe_cmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        p.wait()

        if p.returncode != 0:
            print('Error : ' + cmd)
            return -1


if __name__ == '__main__':
    generator = BitCodeGenerator()
    generator.generate_bitcode('data/cpp/')
