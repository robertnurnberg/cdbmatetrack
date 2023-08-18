import argparse, os, datetime

parser = argparse.ArgumentParser(
    description="Extract cdb mate statistic from a ChestUCI type .epd file.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "filename",
    nargs="?",
    help="file with scored FENs",
    default="matetrack_cdbeval.epd",
)
parser.add_argument("--debug", action="store_true")
parser.add_argument("--mateFile", help="output file for found mates", default=None)
parser.add_argument(
    "--nonmateFile",
    help="output file for non-mates with more than 7 pieces",
    default=None,
)
args = parser.parse_args()

mtime = os.path.getmtime(args.filename)
mtime = datetime.datetime.fromtimestamp(mtime).isoformat()
npos, mates, bestMates, TBwins, connected = 0, 0, 0, 0, 0
nonmates, normalevals = 0, 0
mateLines, nonmateLines = [], []
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
            epd, _, cdb = line.partition(" cdb eval: ")
            if "ply" in cdb:
                connected += 1
                cdb, _, _ = cdb.partition(", ply: ")
            else:
                cdb, _, _ = cdb.partition(";")
            if cdb.lstrip("-").isnumeric():
                if abs(int(cdb)) >= 20000:
                    if int(cdb) * bm > 0:
                        TBwins += 1
                    else:
                        print(f"Wrong TB signs for {fen}.")
                else:
                    pc = sum(p in "pnbrqk" for p in fen.lower().split()[0])
                    print(line)
                    _ = input(f"{pc}men")
                    normalevals += 1
                if args.nonmateFile:
                    pc = sum(p in "pnbrqk" for p in fen.lower().split()[0])
                    if pc >= 8:  # no chance in 7men positions anyway
                        nonmateLines.append((abs(int(cdb)), line + "\n"))
                        nonmates += 1
            elif cdb.startswith("M"):
                m = int(cdb[1:])
                if m * bm > 0:
                    mates += 1
                    if 2 * bm - 1 == m:
                        bestMates += 1
                else:
                    print(f"Wrong mate signs for {fen}.")
                if args.mateFile:
                    mateLines.append(
                        (
                            m - (2 * bm - 1),
                            epd + f" cdb: #{(m+1)//2}\n",
                        )
                    )
            elif cdb.startswith("-M"):
                m = -int(cdb[2:])
                if m * bm > 0:
                    mates += 1
                    if 2 * bm == m:
                        bestMates += 1
                else:
                    print(f"Wrong mate signs for {fen}.")
                if args.mateFile:
                    mateLines.append((2 * bm - m, epd + f" cdb: #{m//2}\n"))
            else:
                print(f"Wrong eval type for {fen}.")
            npos += 1

            if args.debug:
                print(line)
                print("fen:", fen)
                print("bm:", bm)
                print("cdb:", cdb)
                print(
                    "mates, bestMates, TBwins, connected:",
                    mates,
                    bestMates,
                    TBwins,
                    connected,
                )
                _ = input("")

print(f"Nonmates: {nonmates}, normalevals: {normalevals}.")
print(f"{mtime},{npos},{mates},{bestMates},{TBwins},{connected}")

if args.mateFile:
    mateLines.sort(key=lambda t: t[0])  # guarantee stable sort
    with open(args.mateFile, "w") as f:
        for _, line in mateLines:
            f.write(line)

if args.nonmateFile:
    nonmateLines.sort(key=lambda t: t[0])  # guarantee stable sort
    with open(args.nonmateFile, "w") as f:
        for _, line in nonmateLines:
            f.write(line)
