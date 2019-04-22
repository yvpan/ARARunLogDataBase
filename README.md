# ARARunLogDataBase
A database for ARA run information

runDataBaseSqlite.py is used to add infomation to an sqlite database. Run as:
`python runDataBaseSqlite.py ${RUN_NUMBER} ${STATION} ${YEAR} ${RUN_TYPE FILTERED/CALIBRATION/PEDESTAL} ${PATH_TO_CONFIG_FILES}`.
For example, `python runDataBaseSqlite.py 10493 ARA01 2018 FILTERED /home/ypan/doc/temp/run_009503/logs/`.

runDataBaseText.py is used to add information to a txt database. Run as:
`python runDataBaseText.py ${RUN_NUMBER} ${STATION} ${YEAR} ${RUN_TYPE FILTERED/CALIBRATION/PEDESTAL} ${PATH_TO_CONFIG_FILES}`.
For example, `python runDataBaseText.py 10493 ARA01 2018 FILTERED /home/ypan/doc/temp/run_009503/logs/`.

runDataBaseBackwards.sh is used to get previous run information to an sqlite database.

pushDataBaseSqlite.py is used to add additional information from an external file. An external file should include: run_num, username, run_quality and user_commentSome. Each column should be seperated by tab. Sample external files can be found in /logs. Run as:
`python pushDataBaseSqlite.py ${STATION} ${PATH_TO_THE_EXTERNAL_FILE}`.
For example, `python pushDataBaseSqlite.py ARA01 /home/ypan/doc/logs/a1_2018_log.txt`.

A sample database can be found in /database.

## Using the DataBase
For coders, we recommend looking at `access_functions` for how to call information out of the database through the command line and in scripts.

If you want to browse the database in an "Excel" like setting, we recommend downloading [DB Broswer for SQLite](http://sqlitebrowser.org/), which works for PC, Mac, and Linux. This GUI interface is  probably more robust than opening the large `.txt` files are grepping/searching.
