#!/bin/bash

python3 ../cdblib/fens2cdb.py --user rob matetrack.epd >matetrack_cdbeval.epd
python3 ../cdblib/cdbbulkpv.py --stable --user rob matetrack.epd >matetrack_cdbpv.epd
python3 cdbmatetrack.py --mateFile matetrack_cdbmates.epd --nonmateFile matetrack_cdbnonmates.epd >>cdbmatetrack.csv
python3 plotdata.py

git add matetrack_cdbeval.epd cdbmatetrack.csv matetrack_cdbmates.epd matetrack_cdbnonmates.epd matetrack_cdbpv.epd
git add cdbmatetrack.png cdbmatetrackall.png
git diff --staged --quiet || git commit -m "update data and plots"
git push origin main >&push.log
