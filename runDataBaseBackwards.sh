#!/bin/bash
for RUN in {1498..3026}
do
    python runDataBaseSqlite.py $RUN ARA05 2018 FILTERED /data/exp/ARA/2013/monitoring/aware/output/ARA05/logs/
done
