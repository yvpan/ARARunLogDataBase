###################################################################
#Push external files to the run log database
#Station Number    Run    Start    End    Run Type    antennaIceA#I1    antennaIceB#I1    opIceA#I1    opIceB#I1    attIceA#I1    attIceB#I1    Run_Start_Type    Run_End_Type    enableExtTrigger#I1    Quality    aComment    uComment
#run as python pushDataBaseSqlite.py ARA01 /home/ypan/doc/logs/a1_2018_log.txt
#Yue
###################################################################
import sys
import sqlite3
from pylab import *

outDir = "/data/exp/ARA/2013/monitoring/aware/output/db/"
station = sys.argv[1]
inDir = sys.argv[2]

inFile = genfromtxt(inDir, dtype = None, delimiter = "\t")
run = [item[0] for item in inFile]
username = [item[1] for item in inFile]
quality = [item[2] for item in inFile]
uComment = [item [3] for item in inFile]

conn = sqlite3.connect(outDir + "/runDataBase2018.sqlite")
c = conn.cursor()
for i in range(len(run)):
    userComments = "User: " + username[i] + "; " + uComment[i]
    print('%d %20s %20s %30s\n' % (int(run[i]), username[i], quality[i], userComments))
    c.execute("SELECT * FROM %s WHERE Run = %d" % (station, int(run[i])))
    data=c.fetchall()
    if len(data)==0:
        c.execute("INSERT INTO %s (Run, RunType, Quality, UserComments) VALUES (%d, 'Data', '%s', '%s')" % (station, int(run[i]), quality[i], userComments))
    else:
        c.execute("UPDATE %s SET Quality = '%s', UserComments = '%s' WHERE Run = %d" % (station, quality[i], userComments, int(run[i])))
    conn.commit()
conn.close()
