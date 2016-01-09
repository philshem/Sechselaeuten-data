# -*- coding: utf-8 -*-

# download historical weather from meteoswiss and print as csv (tab seperated)

import requests

delim ='\t'

# url for historical zurich weather data
url = 'http://www.meteoswiss.admin.ch/product/output/climate-data/homogenous-monthly-data-processing/data/homog_mo_SMA.txt'
r = requests.get(url).text.encode('utf-8')

# loop over lines in text file. find data header line number
for idx, val in enumerate(r.split('\r\n')):
	if val.startswith('Year'):
		print delim.join(val.split()) #print csv header
		start = idx
		break

# read remaining lines as data
data = r.split('\n')[start+1:-1]

# print with same delimiter
for d in data:
	print delim.join(d.split())


