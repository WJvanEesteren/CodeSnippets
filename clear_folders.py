from os.path import join, dirname, realpath
import os, shutil

def clear():
	"'clears the directory of all files and folders'"
	dirs = ['uploads', 'resizes']
	for i in dirs:
		path = join(dirname(realpath(__file__)), i)
		for filename in os.listdir(path):
			if (filename == ".placeholder"):
				continue
			elif(os.path.isfile(join(path, filename))):
				os.remove(join(path, filename))