#!/bin/bash

###################################
#Push additional information to the aware database
#Yue
#run on cobalt04 every monday at 3am
####################################

source /home/ypan/.bashrc
eval `/cvmfs/icecube.opensciencegrid.org/py2-v2/setup.sh`

cd /home/ypan/bin/ARARunLogDataBase/ARARunLogDataBase/
#git pull
#python pushDataBaseSqlite.py ARA01 ./logs/a1_log.txt
#python pushDataBaseSqlite.py ARA02 ./logs/a2_log.txt
#python pushDataBaseSqlite.py ARA03 ./logs/a3_log.txt
python pushDataBaseSqlite.py ARA04 ./logs/a4_log.txt
python pushDataBaseSqlite.py ARA05 ./logs/a5_log.txt
python pushDataBaseSqlite.py ARA06 ./logs/a6_log.txt
