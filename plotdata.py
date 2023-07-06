import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.ticker import MaxNLocator


class matedata:
    def __init__(self, prefix, egtb=None, wcr=None):
        self.prefix = prefix
        self.egtb, self.wcr = egtb, wcr
        self.date = []  # datetime entries
        self.mates = []  # mates
        self.bmates = []  # best mates
        self.wins = []  # mates + tb wins
        self.connected = []  # positions connected to root
        with open(prefix + ".csv") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Time"):
                    continue
                if line:
                    parts = line.split(",")
                    self.date.append(datetime.fromisoformat(parts[0]))
                    self.total = int(parts[1])
                    self.mates.append(int(parts[2]))
                    self.bmates.append(int(parts[3]))
                    self.wins.append(int(parts[2]) + int(parts[4]))
                    self.connected.append(int(parts[5]))

    def showdata(self):
        print("date: ", self.date)
        print("mates: ", self.mates)
        print("bmates: ", self.bmates)
        print("wins: ", self.wins)
        print("connected: ", self.connected)

    def create_graph(self, plotAll=False):
        dotSize, lineWidth = 20, 0.5
        fig, ax1 = plt.subplots()
        yColor, dateColor, connectedColor = "black", "black", "lightgray"
        bmateColor, mateColor, winColor = "limegreen", "blue", "navy"
        ax1.scatter(
            self.date, self.bmates, label="best mates", color=bmateColor, s=dotSize
        )
        ax1.scatter(self.date, self.mates, label="mates", color=mateColor, s=dotSize)
        ax1.plot(self.date, self.bmates, color=bmateColor, linewidth=lineWidth)
        ax1.plot(self.date, self.mates, color=mateColor, linewidth=lineWidth)
        if plotAll:
            ax1.scatter(
                self.date, self.wins, label="TBwins+mates", color=winColor, s=dotSize
            )
            ax1.plot(self.date, self.wins, color=winColor, linewidth=lineWidth)
            maxPossible = self.total - self.wcr
        else:
            maxPossible = self.total - self.egtb
        if max(self.mates) > 0.8 * maxPossible:
            ax1.axhline(
                maxPossible, color=yColor, linestyle="dashed", linewidth=lineWidth / 2
            )
            yt = list(ax1.get_yticks())
            ax1.set_yticks([t for t in yt if t < maxPossible] + [maxPossible])
        ax1.set_ylabel("# of positions", color=yColor)
        ax1.tick_params(axis="y", labelcolor=yColor)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax1.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.13))
        plt.setp(
            ax1.get_xticklabels(),
            rotation=45,
            ha="right",
            rotation_mode="anchor",
            fontsize=6,
        )
        if plotAll and self.connected[-1]:
            ax2 = ax1.twinx()
            ax2.set_ylabel("connected to root", color=connectedColor)
            ax2.scatter(self.date, self.connected, color=connectedColor, s=dotSize / 4)
            ax2.plot(
                self.date,
                self.connected,
                color=connectedColor,
                linewidth=lineWidth / 2,
            )
            ax2.tick_params(axis="y", labelcolor=connectedColor)
            ax2.set_ylim([0, max(self.connected) * 1.1])
            ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.savefig(self.prefix + ("all" if plotAll else "") + ".png", dpi=300)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot data stored in e.g. cdbmatetrack.csv.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "filename",
        nargs="?",
        help="file with statistics over time",
        default="cdbmatetrack.csv",
    )
    parser.add_argument("--egtb", help="number of EGTB positions", default=866)
    parser.add_argument(
        "--wcr", help="number of EGTB positions w/ castling rights", default=9
    )
    args = parser.parse_args()

    prefix, _, _ = args.filename.partition(".")
    data = matedata(prefix, args.egtb, args.wcr)
    data.create_graph(plotAll=False)
    data.create_graph(plotAll=True)
