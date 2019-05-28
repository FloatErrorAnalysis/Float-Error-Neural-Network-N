class CppRawGenerator:
    data_path = './data/cpp/'

    cpp_head = '#include \"cmath\" \nusing namespace std;\n'

    cpp_main = 'int main() {\n'

    cpp_var_x = '   double x = 0;\n'

    cpp_var_a = '   double a = x+1;\n'

    cpp_var_b = '   double b = x;\n'

    cpp_content = '   double result = sqrt(a) - sqrt(b);\n' \
                  '   return 0;\n' \
                  '}'

    # sqrt(x + n + 1) - sqrt(x + n)
    def generate_add(self, num):
        for i in range(1, num + 1):
            with open(self.data_path + 'sqrt_minus' + str(i) + '_add.cpp', 'w') as f:
                cpp_str_a = self.cpp_var_a.replace('x+1', 'x+' + str(i+1))
                cpp_str_b = self.cpp_var_b.replace('x', 'x+' + str(i))
                cpp_str = self.cpp_head + self.cpp_main + self.cpp_var_x + cpp_str_a + cpp_str_b + self.cpp_content
                f.writelines(cpp_str)

    # sqrt(n * x  + 1) - sqrt(n * x)
    def generate_mul(self, num):
        for i in range(1, num + 1):
            with open(self.data_path + 'sqrt_minus' + str(i) + '_mul.cpp', 'w') as f:
                cpp_str_a = self.cpp_var_a.replace('x', 'x*' + str(i))
                cpp_str_b = self.cpp_var_b.replace('x', 'x*' + str(i))
                cpp_str = self.cpp_head + self.cpp_main + self.cpp_var_x + cpp_str_a + cpp_str_b + self.cpp_content
                f.writelines(cpp_str)


if __name__ == '__main__':
    generator = CppRawGenerator()
    num = 10
    generator.generate_add(num)
    generator.generate_mul(num)
