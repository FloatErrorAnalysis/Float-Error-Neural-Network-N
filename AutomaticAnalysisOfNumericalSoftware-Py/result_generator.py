class ResultGenerator:

    def add(self, num, result):
        with open('./data/result/result_add_' + str(num) + '.txt', 'w') as f:
            for i in range(1, num + 1):
                f.write(str(result - i) + '\n')

    def mul(self, num, result):
        with open('./data/result/result_mul_' + str(num) + '.txt', 'w') as f:
            for i in range(1, num + 1):
                f.write(str(result / i) + '\n')


if __name__ == '__main__':
    generator = ResultGenerator()
    generator.add(1000, 100000000)
    generator.mul(1000, 100000000)
