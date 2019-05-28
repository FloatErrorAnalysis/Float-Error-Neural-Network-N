from subprocess import Popen, PIPE


class Cleaner:

    def exe_cmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        p.wait()

        if p.returncode != 0:
            print('Error : ' + cmd)
            return -1


if __name__ == '__main__':
    cleaner = Cleaner()
    cleaner.exe_cmd('find data/cpp/ -name "*.cpp" |xargs rm -r')
    cleaner.exe_cmd('find data/ll/ -name "*.ll" |xargs rm -r')
    cleaner.exe_cmd('find data/bc/ -name "*.bc" |xargs rm -r')
