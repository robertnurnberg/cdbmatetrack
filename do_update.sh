#!/bin/bash

temp_file="_tmp_matetrack_cdbeval.epd"

if [ -f "$temp_file" ]; then
    echo "$temp_file already exists. Exiting."
    exit 0
fi

python3 ../cdblib/fens2cdb.py --user rob matetrack.epd >"$temp_file"
python3 ../cdblib/cdbbulkpv.py --stable --user rob matetrack.epd >matetrack_cdbpv.epd

mv "$temp_file" matetrack_cdbeval.epd

python3 cdbmatetrack.py --mateFile matetrack_cdbmates.epd --nonmateFile matetrack_cdbnonmates.epd >>cdbmatetrack.csv
python3 plotdata.py

git add matetrack_cdbeval.epd cdbmatetrack.csv matetrack_cdbmates.epd matetrack_cdbnonmates.epd matetrack_cdbpv.epd
git add cdbmatetrack.png cdbmatetrackall.png
git diff --staged --quiet || git commit -m "update data and plots"
git push origin main >&push.log
