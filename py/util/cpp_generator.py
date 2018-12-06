import os
from py.util.BCTool import generate_bytecode
from py.util.BCTool import exe_cmd


class CppRawGenerator:
    cmd0 = 'cd /Users/py/Downloads/iRRAM-master/examples/'

    cpp_str_prefix = '#include \"cmath\" \nusing namespace std;\n' \
                     'double sqrt_minus_error(double x) {\n'

    cpp_normal_prefix = 'double sqrt_minus_error(double x) {\n'

    cpp_str0 = '   return sqrt(x+1) - sqrt(x);\n' \
               '}'


    error_str0 = '#include \"cmath\"\n' \
                 '#include "iRRAM.h\n' \
                 'using namespace iRRAM;\n'

    error_str2 = 'REAL sqrt_minus_real(const REAL &x) {\n' \
                 '  return REAL(sqrt(x+1)) - REAL(sqrt(x));\n}\n'

    error_str3 = 'void generate_data(double low_bound, double high_bound, double gap) {\n' \
                 '  orstream file("../../dataset/error_sqrt_minus'\

    error_str4 = '.csv", std::ios::out);\n' \
                 '  file << "x,y\\n";\n' \
                 '  int number = static_cast<int>((high_bound - low_bound) / gap);\n' \
                 '  double current_input = low_bound;\n' \
                 '  for (int i = 0; i <= number; i++) {\n' \
                 '      double result_error = sqrt_minus_error(current_input);\n' \
                 '      REAL result_real = sqrt_minus_real(current_input);\n' \
                 '      file << current_input << "," << abs((result_real - REAL(result_error)).as_double()) << "\\n";\n' \
                 '      current_input += gap;\n' \
                 '  }\n' \
                 '}\n' \
                 'void compute() {\n' \
                 '  generate_data(1, 10000, 1);\n' \
                 '}\n'

    cpp_prefix_path = '../../dataset/sqrt_minus'

    file_path_prefix = '../../cpp_raw/'
    # sqrt(n * x  + 1) - sqrt(n * x)

    def generate_sqrt_minus_mul(self, num):
        for i in range(1, num + 1):
            with open(self.file_path_prefix + 'mul/sqrt_minus' + str(i) + '.cpp', 'w') as f:
                tmp = self.cpp_str0.replace('x', str(i) + '*x')
                f.writelines(self.cpp_str_prefix + tmp)

            with open(self.cpp_prefix_path + str(i) + '.cpp', 'w') as f:
                tmp1 = self.error_str0 + self.cpp_normal_prefix + tmp + '\n' + self.error_str2.replace('x', str(i) + '*x') +\
                       self.error_str3 + str(i) + self.error_str4
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

            with open(self.cpp_prefix_path + str(i) + '.cpp', 'w') as f:
                tmp2 = self.error_str2.replace('x', 'x+' + str(i)).replace('x+' + str(i) + '+1', 'x+' + str(i + 1))
                tmp1 = self.error_str0 + self.cpp_normal_prefix + tmp + '\n' + tmp2 +\
                       self.error_str3 + str(i) + self.error_str4
                f.writelines(tmp1)


    def get_error_cpp(self):
        with open(self.cpp_prefix_path + 'sqrt_minus1.cpp') as f:
            cpp_lst = f.readlines()
        return cpp_lst


    def generate_ll(self, aim_dir):
        generate_bytecode(aim_dir)

    # 路径修改 TODO
    def generate_csv(self):
        exe_cmd(self.cmd0)
        for f in os.listdir('/'):
            exe_cmd('make ' + f)




print(os.getcwd())
cpp_gen = CppRawGenerator()
cpp_gen.generate_sqrt_minus_add(3)
