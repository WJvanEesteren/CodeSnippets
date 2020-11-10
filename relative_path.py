from os.path import join, dirname, realpath, abspath

#refer to file in current directory
results_path = join(dirname(realpath(__file__)), 'results')

#refer to file in one directory higher
path = abspath(join(realpath(dirname(__file__)),'..', 'test.py'))

print(results_path)
print(path)