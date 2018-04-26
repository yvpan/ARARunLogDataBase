# ARARunLogDataBase
A database for ARA run information

runDataBaseSqlite.py is used to add infomation to an sqlite database. Run as 
python runDataBaseSqlite.py ${RUN_NUMBER} ${STATION} ${YEAR} ${RUN_TYPE FILTERED/CALIBRATION/PEDESTAL} ${PATH_TO_CONFIG_FILES}.
For example, python runDataBaseSqlite.py 10493 ARA01 2018 FILTERED /home/ypan/doc/temp/run_009503/logs/.

runDataBaseText.py is used to add information to a txt database. Run as 
python runDataBaseText.py ${RUN_NUMBER} ${STATION} ${YEAR} ${RUN_TYPE FILTERED/CALIBRATION/PEDESTAL} ${PATH_TO_CONFIG_FILES}.
For example, python runDataBaseText.py 10493 ARA01 2018 FILTERED /home/ypan/doc/temp/run_009503/logs/

runDataBaseBackwards.sh is used to get previous run information to an sqlite database.

pushDataBaseSqlite.py is used to add additional information from an external file. Some sample external files can be found in /logs. Each column should be seperated by tab. Run as 
python pushDataBaseSqlite.py ${STATION} ${PATH_TO_THE_EXTERNAL_FILE}.
For example, python pushDataBaseSqlite.py ARA01 /home/ypan/doc/logs/a1_2018_log.txt

A sample database can be found in /database.
