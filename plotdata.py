import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.ticker import MaxNLocator


class matedata:
    def __init__(self, prefix):
        self.prefix = prefix
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
                    self.mates.append(int(parts[2]))
                    self.bmates.append(int(parts[3]))
                    self.wins.append(int(parts[2]) + int(parts[3]) + int(parts[4]))
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
            ax2.scatter(
                self.date, self.connected, color=connectedColor, s=0.5 * dotSize
            )
            ax2.tick_params(axis="y", labelcolor=connectedColor)
            ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.savefig(self.prefix + ("all" if plotAll else "") + ".png", dpi=300)


if __name__ == "__main__":
    data = matedata("cdbmatetrack")
    data.create_graph(plotAll=False)
    data.create_graph(plotAll=True)
