#!/usr/bin/python3
from src.translator import translate_file

from glob import glob

for file in glob('examples/**/*.mce', recursive=True):
	print('File: ' + file)
	translate_file(file)