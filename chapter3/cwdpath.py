# coding: utf-8
import os
os.getcwd()
os.chdir('/home/kshopki/diveintopython/chapter3')
os.getcwd()
os.path.join(os.getcwd(), "cwdpath.py")
os.path.expanduser('~')
os.path.split("/home/kshopki/file.py")
(filename, extension) = os.path.splitext('file.py')
filename
extension
import glob
glob.glob('/home/kshopki/diveintopython/chapter1/*.py')
os.stat('cwdpath.py')
import time
time.localtime(os.stat('cwdpath.py').st_mtime)
os.path.realpath('cwdpath.py')
