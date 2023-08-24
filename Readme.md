#  Track the mates from matetrack on cdb

Track the number of mates from `matetrack.epd` of Joost VandeVondele' [matetrack](https://github.com/vondele/matetrack)
that are scored correctly on [chessdb.cn](https://chessdb.cn/queryc_en/) (cdb), the largest online database of chess positions and openings.

The files [`matetrack_cdbeval.epd`](matetrack_cdbeval.epd)
and [`matetrack_cdbpv.epd`](matetrack_cdbpv.epd) are created daily with
the help of the scripts `fens2cdb.py` and `cdbbulkpv.py` from [cdblib](https://github.com/robertnurnberg/cdblib), respectively, and the obtained mate statistics are written to [`cdbmatetrack.csv`](cdbmatetrack.csv).

The file [`matetrack.epd`](matetrack.epd) contains 6560 mate problems, ranging from mate in 1 (#1) to #126 for positions with between 4 and 32 pieces. Moreover:
* 865 positions have 7 pieces or fewer.
* Of these 7men positions, 9 are not scored by cdb because they allow castling.

As cdb currently does not store mate scores for 7men EGTB positions, the theoretically maximal number of (best) mates it can find within this test suite is 5695. Note that this is an upper bound. The currently achievable number of (best) mates may in fact be lower, and relies on the cdb worker's ability to resolve mating lines that end in 7men EGTB positions. 
Recent SF versions find about 3600 mates (and 2500 best mates) with 1M nodes per position, see [matetrack](https://github.com/vondele/matetrack).

The two files [`matetrack_cdbmates.epd`](matetrack_cdbmates.epd) and [`matetrack_cdbnonmates.epd`](matetrack_cdbnonmates.epd) contain the positions for which cdb reports a mate and a non-mate score, respectively, where the latter file excludes positions with 7 pieces or fewer. Both files are sorted: [`matetrack_cdbmates.epd`](matetrack_cdbmates.epd) by difference in mate score between cdb's mate and the best mate, and [`matetrack_cdbnonmates.epd`](matetrack_cdbnonmates.epd) by absolute value of the cdb eval.

---

<p align="center"> <img src="cdbmatetrack.png?raw=true"> </p>

---

<p align="center"> <img src="cdbmatetrackall.png?raw=true"> </p>
