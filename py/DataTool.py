def find_max(n_max, filename):
    dic = []
    # initialize
    for _ in range(n_max + 1):
        dic.append([0, 0])

    # read raw data
    for line in open('../data_raw/' + filename):
        if 'x,y' in line:
            continue
        input = float(line.split(',')[0])
        error = float(line.split(',')[1])
        element = [input, error]
        for i in reversed(range(n_max)):
            if dic[i][1] < error:
                temp = dic[i]
                dic[i] = element
                dic[i + 1] = temp
            else:
                break

    # write data into file
    f = open('../data_set/output/' + str(n_max) + '_max_' + filename, 'w')  # 若是'wb'就表示写二进制文件
    f.write('x,y\n')  # head
    for item in dic:
        f.write(str(item[0]) + ',' + str(item[1]) + '\n')
    f.close()
    print('Complete')


if __name__ == '__main__':
    find_max(5, 'error_sqrt_minus3.csv')
