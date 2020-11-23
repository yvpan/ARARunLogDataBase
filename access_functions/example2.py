#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import access_tools as tools
import sys

#this example shows how to use the "access_tools.py" class to search the database for all runs of a certain quality
#you really just need to read the main() function

def main(station,qual):
    database = "/data/exp/ARA/2013/monitoring/aware/output/db/runDataBase2018.sqlite"
    conn = tools.create_connection(database)
    tools.select_all_by_quality(conn,station,qual)

if __name__=='__main__':
	num_args = len(sys.argv)
	if(num_args != 3):
		print("-------")
		print("Not Enough Arguments, Help is Needed!")
		print("Use as: python example2.py STATION QUALITY")
		print("Example: python example1.py ARA04 roofpulse")
		print("-------")
	else:
		quality_list = ['normal','sinewave','surfpulser','roofpulse','deeppulse','calpulse_sweep','spicecore','phasedarray','bad','other']
		station_list = ['ARA01','ARA02','ARA03','ARA04','ARA05']
		station = sys.argv[1]
		qual = sys.argv[2]
		if((station not in station_list)):
			print("-------")
			print("You asked for station:",station)
			print("That is not a valid station!")
			print("Choices are: ",station_list)
			print("-------")
		elif((qual not in quality_list)):
			print("-------")
			print("You asked for quality:",qual)
			print("That is not a valid quality!")
			print("Choices are: ",quality_list)
			print("-------")
		else:
			main(station,qual)
