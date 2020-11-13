import os
from os.path import join, realpath, dirname 

def get_files(folder):
    try:
        for f in os.listdir(folder):
            if not f.startswith('.'):
                full_name = join(folder, f)
                if os.path.isdir(full_name):
                    get_files(full_name)
                else:
                    print(full_name)
    except OSError:
        Exception("We encountered an error")

path = dirname(realpath(__file__))
get_files(path)
