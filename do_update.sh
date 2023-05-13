#!/bin/bash

python3 ../cdblib/fens2cdb.py ChestUCI_23102018.epd > ChestUCI_23102018_cdbeval.epd
python3 cdbmatetrack.py >> cdbmatetrack.csv

git add ChestUCI_23102018_cdbeval.epd cdbmatetrack.csv
git diff --staged --quiet || git commit -m "update data"
git push origin main >& push.log
