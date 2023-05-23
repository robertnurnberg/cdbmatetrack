#!/bin/bash

python3 ../cdblib/fens2cdb.py ChestUCI_23102018.epd > ChestUCI_23102018_cdbeval.epd
python3 cdbmatetrack.py --mateFile ChestUCI_23102018_cdbmates.epd --nonmateFile ChestUCI_23102018_cdbnonmates.epd >> cdbmatetrack.csv
python3 plotdata.py

git add ChestUCI_23102018_cdbeval.epd cdbmatetrack.csv ChestUCI_23102018_cdbmates.epd ChestUCI_23102018_cdbnonmates.epd
git add cdbmatetrack.png cdbmatetrackall.png
git diff --staged --quiet || git commit -m "update data and plots"
git push origin main >& push.log
