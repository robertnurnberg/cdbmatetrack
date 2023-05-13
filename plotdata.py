import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.ticker import MaxNLocator


class matedata:
    def __init__(self, prefix):
        self.prefix = prefix
        self.date = []  # datetime entries
        self.mates = []  # mates
        self.cmates = []  # correct mates
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
                    self.cmates.append(int(parts[3]))
                    self.wins.append(int(parts[2]) + int(parts[3]) + int(parts[4]))
                    self.connected.append(int(parts[5]))

    def showdata(self):
        print("date: ", self.date)
        print("mates: ", self.mates)
        print("cmates: ", self.cmates)
        print("wins: ", self.wins)
        print("connected: ", self.connected)

    def create_graph(self):
        dotSize, lineWidth = 20, 0.5
        fig, ax1 = plt.subplots()
        mateColor, dateColor, connectedColor = "black", "black", "gray"
        winColor = "yellow"
        cmateColor = "red"
        ax1.set_ylabel("scored positions", color=mateColor)
        ax1.scatter(
            self.date, self.wins, label="TBwins+mates", color=winColor, s=dotSize
        )
        ax1.scatter(self.date, self.mates, label="mates", color=mateColor, s=dotSize)
        ax1.scatter(
            self.date, self.cmates, label="best mates", color=cmateColor, s=dotSize
        )
        ax1.tick_params(axis="y", labelcolor=mateColor)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax1.legend()
        plt.setp(
            ax1.get_xticklabels(),
            rotation=45,
            ha="right",
            rotation_mode="anchor",
            fontsize=6,
        )
        ax2 = ax1.twinx()
        ax2.set_ylabel("positions connected to root", color=connectedColor)
        ax2.scatter(self.date, self.connected, color=connectedColor, s=0.5 * dotSize)
        ax2.tick_params(axis="y", labelcolor=connectedColor)
        # ax2.set_ylim([max(0, min(self.connected)), max(1, max(self.connected))])
        ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.savefig(self.prefix + ".png", dpi=300)


data = matedata("cdbmatetrack")
data.showdata()
data.create_graph()
