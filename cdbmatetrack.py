import argparse, os, datetime

parser = argparse.ArgumentParser(
    description="Extract cdb mate statistic from a ChestUCI type .epd file.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "filename",
    nargs="?",
    help="file with scored FENs",
    default="ChestUCI_23102018_cdbeval.epd",
)
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

mtime = os.path.getmtime(args.filename)
mtime = datetime.datetime.fromtimestamp(mtime).isoformat()
npos, mates, correctMates, TBwins, connected = 0, 0, 0, 0, 0
with open(args.filename) as f:
    for line in f:
        line = line.strip()
        if line:
            if line.startswith("#"):  # ignore comments
                continue
            fen = " ".join(line.split()[:4])
            _, _, bm = line.partition(" bm #")
            bm, _, _ = bm.partition(";")
            bm = int(bm)
            _, _, cdb = line.partition(" cdb eval: ")
            if "ply" in cdb:
                connected += 1
                cdb, _, _ = cdb.partition(", ply: ")
            else:
                cdb, _, _ = cdb.partition(";")
            if cdb.isnumeric():
                if abs(int(cdb)) >= 20000:
                    TBwins += 1
            elif cdb.startswith("M"):
                mates += 1
                if 2 * bm - 1 == int(cdb[1:]):
                    correctMates += 1
            elif cdb.startswith("-M"):
                mates += 1
                if 2 * bm == -int(cdb[2:]):
                    correctMates += 1
            npos += 1

            if args.debug:
                print(line)
                print("fen:", fen)
                print("bm:", bm)
                print("cdb:", cdb)
                print(
                    "mates, correctMates, TBwins, connected:",
                    mates,
                    correctMates,
                    TBwins,
                    connected,
                )
                _ = input("")

print(f"{mtime},{npos},{mates},{correctMates},{TBwins},{connected}")
