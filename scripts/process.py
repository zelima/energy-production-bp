#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import urllib
import datetime
import csv
import xlrd


source = 'http://www.bp.com/content/dam/bp/excel/energy-economics/statistical-review-2016/bp-statistical-review-of-world-energy-2016-workbook.xlsx'

def setup():
	'''Crates the archive directory if one doesn't exist
	
	'''
	if not os.path.exists('archive'):
		os.mkdir('archive')

def retrieve(source):
	'''Downloades xls data to archive directory
	
	'''
	urllib.urlretrieve(source,'archive/external-data.xls')

			
if __name__ == '__main__':
	setup()
	retrieve(source)
	