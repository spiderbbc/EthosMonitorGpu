#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
 

class Handling(object):
	"""docstring for Handling"""
	def __init__(self):
		self.filename = "count.txt"
		self.limit = 5
		self.createFile()

	def createFile(self):
		if not os.path.isfile(self.filename):
			file = open(self.filename,"a+")
			file.write(str(int(0)))
			file.close()
		

	def readTheCounterFile(self):
		file = open(self.filename,"r")
		if file.mode == 'r':
			content = file.read()
			file.close()
			return str(content)

	def addToTheCounterFile(self,counter):
		file = open(self.filename,"r+")
		file.readlines()
		file.seek(0)
		file.write(str(int(counter) + 1))
		file.truncate()
		file.close()

	def resetCounterFile(self):
		file = open(self.filename,"r+")
		number = file.readlines()
		if int(number[0]) == self.limit:
			file.seek(0)
			file.write(str(int(0)))
		
		file.truncate()
		file.close()
		
