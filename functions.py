import sys
import os

def function_1():
    return sys.version

def function_2(directory):
    path = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(path, os.pardir))
    new_dir_path = os.path.join(parent_dir, directory)
    os.mkdir(new_dir_path)

def function_3():
    path = os.getcwd()
    dir_path = os.path.abspath(os.path.join(path, os.pardir))
    files = os.listdir(dir_path)
    return files

def inputs(command, name):
    if command=='1':
        print(function_1())
    if command=='2':
        function_2(name)
    if command=='3':
        print(*function_3())