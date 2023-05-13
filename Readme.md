#  Track the mates from matetrack on cdb

Track the number of mates from `ChestUCI_23102018.epd` of 
Joost VandeVondele' [matetrack](https://github.com/vondele/matetrack)
that are scored correctly on [chessdb.cn](https://chessdb.cn/queryc_en/) (cdb), the largest online database of chess positions and openings.

The file `ChestUCI_23102018.epd` contains 6566 mate problems, ranging from #1 
to #126. Note that 5 of the positions in `ChestUCI_23102018.epd` are classified
as invalid by cdb.

The file `ChestUCI_23102018_cdbeval.epd` is periodically created with the help of the script `fens2cdb.py` from [cdblib](https://github.com/robertnurnberg/cdblib), and the obtained statistics are written to `cdbmatetrack.csv`.
