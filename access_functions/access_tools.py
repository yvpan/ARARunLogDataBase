#!/usr/bin/python

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	""" create a database connection to the SQLite database
		specificed by the db_file
	:param db_file: database file
	:return: Connection object or None
	"""

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print (e)

	return None

def select_all_by_quality(conn,station,quality):

	""" create a database connection to the SQLite database
		specificed by the db_file
	:param connection: the Connection object
	:param station: string of the station we care about, e.g. 'ARA04'
	:param quality: string of the quality of the run we want to cut on, e.g. 'roofpulse'
	:return: None
	"""

	cur = conn.cursor()
	cur.execute("SELECT * FROM {tn} WHERE Quality='{qu}'".\
		format(tn=station,qu=quality))
	rows = cur.fetchall()
	num_runs = len(rows)
	print "Found %d runs"%num_runs
	for row in rows:
		print "	Run: ",(row[0])

def is_run_good(conn,station,run):

	""" create a database connection to the SQLite database
		specificed by the db_file
	:param connection: the Connection object
	:param station: string of the station we care about, e.g. 'ARA04'
	:param run: what run are we asking about
	:return: true or false (boolean) or undefined if the query fails
	"""

	cur = conn.cursor()
	try:
		cur.execute("SELECT Quality FROM {tn} WHERE Run={run}".\
			format(tn=station,run=run))
		answer = cur.fetchone()
		val = False
		if(answer[0]=='Normal'): val=True
		return val
	except:
		print "Warning! Query Failed!"
		return 'undefined'