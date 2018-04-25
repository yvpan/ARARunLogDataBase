###################################################################
#Record processed runs information
#Station Number    Run    Start    End    Run Type    antennaIceA#I1    antennaIceB#I1    opIceA#I1    opIceB#I1    attIceA#I1    attIceB#I1    Run_Start_Type    Run_End_Type    enableExtTrigger#I1    Quality    aComment    uComment
#run as python runDataBaseTest2.py 10493 ARA01 2018 FILTERED/CALIBRATION/PEDESTAL/HOUSEKEEPING /home/ypan/doc/temp/run_009503/logs/
#Yue
###################################################################
import re
import sys
import sqlite3
import os.path

outDir = "/data/exp/ARA/2013/monitoring/aware/output/db/"
run = sys.argv[1]
station = sys.argv[2]
year = sys.argv[3]
runType = sys.argv[4]
inDir = sys.argv[5]
runLong = "%06d" % int(run)

if runType == "FILTERED" or runType == "CALIBRATION":
    runType2 = "Data"
    if os.path.isfile(inDir + "/runStart.run" +  runLong + ".dat"):
        inFile = open(inDir + "/runStart.run" +  runLong + ".dat", "r")
        startTime = re.findall(r"\d\d\d\d\d\d\d\d\d\d", inFile.read())[0]
        inFile.close()
        inFile = open(inDir + "/runStart.run" +  runLong + ".dat", "r")
        startType = re.findall(r"Message: .*", inFile.read())[0].split(":", 1)[1]
        inFile.close()
    else:
        startTime = 0
        startType = "N/A"
    if os.path.isfile(inDir + "/runStop.run" +  runLong + ".dat"):
        inFile = open(inDir + "/runStop.run" +  runLong + ".dat", "r")
        endTime = re.findall(r"\d\d\d\d\d\d\d\d\d\d", inFile.read())[0]
        inFile.close()
        inFile = open(inDir + "/runStop.run" +  runLong + ".dat", "r")
        endType = re.findall(r"Message: .*", inFile.read())[0].split(":", 1)[1]
        inFile.close()
    else:
        endTime = 0
        endType = "N/A"
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    anteIceA = re.findall(r"antennaIceA#I1=\d", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    anteIceB = re.findall(r"antennaIceB#I1=\d", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    opIceA = re.findall(r"opIceA#I1=\d", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    opIceB = re.findall(r"opIceB#I1=\d", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    attIceA = re.findall(r"attIceA#I1=\d+", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    attIceB = re.findall(r"attIceB#I1=\d+", inFile.read())[0].split("=")[1]
    inFile.close()
    inFile = open(inDir + "/configFile.run" +  runLong + ".dat", "r")
    extTrig = re.findall(r"enableExtTrigger#I1=\d", inFile.read())[0].split("=")[1]
    inFile.close()
    quality = "Normal"
    aComment = "N/A"
    uComment = "N/A"
    print('%5s %6s %12s %12s %10s %2s %2s %2s %2s %2s %2s %20s %20s %2s %12s %30s %30s\n' % (station, str(run), str(startTime), str(endTime), runType2, anteIceA, anteIceB, opIceA, opIceB, attIceA, attIceB, startType, endType, extTrig, quality, aComment, uComment))

    conn = sqlite3.connect(outDir + "/runDataBase2018.sqlite")
    c = conn.cursor()
    c.execute("INSERT INTO %s VALUES (%d,%d,%d,'%s',%d,%d,%d,%d,%d,%d,'%s','%s',%d,'%s','%s','%s')" % (station, int(run), int(startTime), int(endTime), runType2, int(anteIceA), int(anteIceB), int(opIceA), int(opIceB), int(attIceA), int(attIceB), startType, endType, int(extTrig), quality, aComment, uComment))
#    c.execute('INSERT INTO ? VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (station, int(run), int(startTime), int(endTime), runType2, int(anteIceA), int(anteIceB), int(opIceA), int(opIceB), int(attIceA), int(attIceB), startType, endType, int(extTrig), quality, aComment, uComment))
    conn.commit()
    conn.close()

elif runType == "PEDESTAL":
    runType2 = "Pedestal"
    startTime = "N/A"
    startType = "N/A"
    endTime = "N/A"
    endType = "N/A"
    anteIceA = "N/A"
    anteIceB = "N/A"
    opIceA = "N/A"
    opIceB = "N/A"
    attIceA = "N/A"
    attIceB = "N/A"
    extTrig = "N/A"
    quality = "Normal"
    aComment = "N/A"
    uComment = "N/A"
    print('%5s %6s %12s %12s %10s %2s %2s %2s %2s %2s %2s %20s %20s %2s %12s %30s %30s\n' % (station, str(run), str(startTime), str(endTime), runType2, anteIceA, anteIceB, opIceA, opIceB, attIceA, attIceB, startType, endType, extTrig, quality, aComment, uComment))

    conn = sqlite3.connect(outDir + "/runDataBase2018.sqlite")
    c = conn.cursor()
    c.execute("INSERT INTO %s VALUES (%d,%d,%d,'%s',%d,%d,%d,%d,%d,%d,'%s','%s',%d,'%s','%s','%s')" % (station, int(run), int(startTime), int(endTime), runType2, int(anteIceA), int(anteIceB), int(opIceA), int(opIceB), int(attIceA), int(attIceB), startType, endType, int(extTrig), quality, aComment, uComment))
#    c.execute('INSERT INTO ? VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (station, int(run), int(startTime), int(endTime), runType2, int(anteIceA), int(anteIceB), int(opIceA), int(opIceB), int(attIceA), int(attIceB), startType, endType, int(extTrig), quality, aComment, uComment))
    conn.commit()
    conn.close()

else:
    print "Wrong Run Type or Housekeeping!"
