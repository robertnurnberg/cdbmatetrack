#  Track the mates from matetrack on cdb

Track the number of mates from `ChestUCI_23102018.epd` of Joost VandeVondele' [matetrack](https://github.com/vondele/matetrack)
that are scored correctly on [chessdb.cn](https://chessdb.cn/queryc_en/) (cdb), the largest online database of chess positions and openings.

The file `ChestUCI_23102018_cdbeval.epd` is periodically created with the help of the script `fens2cdb.py` from [cdblib](https://github.com/robertnurnberg/cdblib), and the obtained statistics are written to `cdbmatetrack.csv`.

The file `ChestUCI_23102018.epd` contains 6566 mate problems, ranging from mate in 1 (#1) to #126 for positions with between 4 and 32 pieces. Moreover:
* 5 positions are classified as invalid by cdb. They have 19, 21, 23, 32 and 32 pieces, respectively.
* 866 positions have 7 pieces or fewer.
* Of these 7men positions, 9 are not scored by cdb because they allow castling.

As cdb currently does not store mates scores for 7men EGTB positions, the theoretically maximal number of (best) mates it can find is 5695. Recent SF versions find about 2450 best mates with 1M nodes per position, see [matetrack](https://github.com/vondele/matetrack).

---

<p align="center"> <img src="cdbmatetrack.png?raw=true"> </p>

---

<p align="center"> <img src="cdbmatetrackall.png?raw=true"> </p>
