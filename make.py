import subprocess
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='hello world build')
parser.add_argument('--debug', '-d',  default='',  help='',  nargs='?')
parser.add_argument('--solu', '-s',  default='',  help='Solution name',  nargs='?')
parser.add_argument('--generate', '-g',  default='Unix Makefiles',  help='CMake generator (e.g., Ninja, Unix Makefiles, Xcode)',  nargs='?')
args = parser.parse_args()

def run_time_bash(cmd):
    scan=subprocess.Popen(cmd,bufsize=0,stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    while True:
        nextline=scan.stdout.readline()
        log = nextline.strip()
        if log: yield log
        if nextline=='' and scan.poll()!=None:
            return

if __name__ == "__main__":
    os.chdir('./')
    if not os.path.exists('./build'):
        os.mkdir('build')
    os.chdir('./build')

    build_type = 'Release' if args.debug == 'false' else 'Debug'

    # 设置环境变量
    os.environ["PATH"] = "/Applications/CMake.app/Contents/bin:" + os.environ["PATH"]


    cmake_cmd = 'cmake -G "{0}" -DCMAKE_BUILD_TYPE={1} -Dsolu={2} ..'.format(args.generate, build_type, args.solu)
    for log in run_time_bash(cmake_cmd):
        print(log)

    if not os.path.exists('./bin'):
        os.mkdir('./bin/')

    for log in run_time_bash('cmake --build .'):
        print(log)
