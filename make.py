#!/usr/bin/env python

import subprocess

def shell_exec(command):
	subprocess.call(command, shell=True)
	
def header_print(text):
	print("+\t" + text + "\t")
	
shell_exec("pdflatex mfh.tex")
