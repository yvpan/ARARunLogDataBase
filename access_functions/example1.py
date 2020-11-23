#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import access_tools as tools
import sys

#this example shows how to use the "access_tools.py" class to check if a run is good for analysis
#you really just need to read the main() function

def main(station,run):
	#database = "../database/runDataBase2018.sqlite"
        database = "/data/exp/ARA/2013/monitoring/aware/output/db/runDataBase2018.sqlite"
        conn = tools.create_connection(database)
        is_good = tools.is_run_good(conn,station,run)
        print("Run {} is good for analysis?: {} ".format(int(run), is_good))

if __name__=='__main__':
    num_args = len(sys.argv)
    if(num_args != 3):
        print("-------")
        print("Not Enough Arguments, Help is Needed!")
        print("Use as: python example1.py STATION RUN")
        print("Example: python example1.py 'ARA04' 3277")
        print("-------")
    else:
        station_list = ['ARA01','ARA02','ARA03','ARA04','ARA05']
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        if((arg1 not in station_list)):
            print("-------")
            print("You asked for station:",arg1)
            print("That is not a valid station!")
            print("Choices are: ",station_list)
            print("-------")
        else:
            station = arg1
            run = arg2
            main(station,run)
