import os
from py.util.BCTool import generate_bytecode
from py.util.BCTool import exe_cmd
import time


class CppRawGenerator:
    cmd0 = 'cd /root/tmp/examples/'

    cpp_str_prefix = '#include \"cmath\" \nusing namespace std;\n' \
                     'double sqrt_minus_error(double x) {\n'

    cpp_normal_prefix = 'double sqrt_minus_error(double x) {\n'

    cpp_str0 = '   return sqrt(x+1) - sqrt(x);\n' \
               '}'

    error_str0 = '#include \"cmath\"\n' \
                 '#include "iRRAM.h\"\n' \
                 'using namespace iRRAM;\n'

    error_str2_1 = 'REAL sqrt_minus_real(const REAL &x) {\n'

    error_str2_2 = '  return REAL(1) / (REAL(sqrt(x + 1)) + REAL(sqrt(x)));\n}\n'

    error_str3 = 'void generate_data(double low_bound, double high_bound, double gap) {\n' \
                 '  orstream file("/root/tmp/dataset/'\

    error_str4 = '.csv", std::ios::out);\n' \
                 '  int number = static_cast<int>((high_bound - low_bound) / gap);\n' \
                 '  double current_input = low_bound;\n' \
                 '  for (int i = 0; i <= number; i++) {\n' \
                 '      double result_error = sqrt_minus_error(current_input);\n' \
                 '      REAL result_real = sqrt_minus_real(current_input);\n' \
                 '      file << current_input << "," << abs(REAL(result_real) - REAL(result_error)).as_double() << "\\n";\n' \
                 '      current_input += gap;\n' \
                 '  }\n' \
                 '}\n' \
                 'void compute() {\n' \
                 '  generate_data(0, 10000, 1);\n' \
                 '}\n'

    cpp_prefix_path = '../../dataset/sqrt_minus'

    file_path_prefix = '../../cpp_raw/'
    # sqrt(n * x  + 1) - sqrt(n * x)

    def generate_sqrt_minus_mul(self, num):
        for i in range(1, num + 1):
            with open(self.file_path_prefix + 'mul/sqrt_minus' + str(i) + '.cpp', 'w') as f:
                tmp = self.cpp_str0.replace('x', str(i) + '*x')
                f.writelines(self.cpp_str_prefix + tmp)

            # csv cpp
            # 需要修改本机对应的路径
            with open(self.cpp_prefix_path + str(i) + '.cpp', 'w') as f:
                tmp1 = self.error_str0 + self.cpp_normal_prefix + tmp + '\n' + self.error_str2_1 + \
                       self.error_str2_2.replace('x', str(i) + '*x') + self.error_str3 + str(i) + self.error_str4
                f.writelines(tmp1)

    # sqrt(x + n + 1) - sqrt(x + n)
    def generate_sqrt_minus_add(self, num):
        for i in range(1, num + 1):
            with open(self.file_path_prefix + 'add/sqrt_minus' + str(i) + '.cpp', 'w') as f:
                cpp_str = self.cpp_str0.replace('x', 'x+' + str(i))
                cpp_str = cpp_str.replace('x+' + str(i) + '+1', 'x+' + str(i + 1)) + '\n'
                tmp = cpp_str
                cpp_str = self.cpp_str_prefix + cpp_str
                f.writelines(cpp_str)


            # csv cpp
            # 需要修改本机对应的路径
            with open('/root/tmp/examples/sqrt_minus' + str(i) + '.cpp', 'w') as f:
                tmp2 = self.error_str2_1 + self.error_str2_2.replace('x', 'x+' + str(i)).replace('x+' + str(i) + '+1', 'x+' + str(i + 1))
                tmp1 = self.error_str0 + self.cpp_normal_prefix + tmp + '\n' + tmp2 +\
                       self.error_str3 + str(i) + self.error_str4
                f.writelines(tmp1)

    def get_error_cpp(self):
        with open(self.cpp_prefix_path + 'sqrt_minus1.cpp') as f:
            cpp_lst = f.readlines()
        return cpp_lst


    def generate_add_ll(self):
        generate_bytecode('../../cpp_raw/add/')

    # 路径修改 TODO
    def generate_csv(self):
        # 编译
        for f in os.listdir('/root/tmp/examples/'):
            postfix = f.split('.')[-1]
            if postfix == 'cpp':
                print(f)
             #   exe_cmd('cd /root/tmp/examples')
                exe_cmd(self.cmd0 + '\n make ' + '/root/tmp/examples/' + f.split('.')[0])
                time.sleep(1)

        # 执行
        for f in os.listdir('/root/tmp/examples/'):
            print('Execute csv...')
            if 'sqrt_minus' in f.split('.')[0] and '.' not in f:
                print(f)
                exe_cmd(self.cmd0 + '\n./' + f)


print(os.getcwd())
cpp_gen = CppRawGenerator()
cpp_gen.generate_sqrt_minus_add(30)
cpp_gen.generate_add_ll()
cpp_gen.generate_csv()
