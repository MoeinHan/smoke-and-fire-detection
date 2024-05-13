import time

from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from itertools import count
import matplotlib
from pathlib import Path
import os
plt.style.use("fivethirtyeight")
plt.style.use('dark_background')
matplotlib.use('TkAgg')
index = count()


time.sleep(3)
plt.figure(figsize=(17,5))
path = Path('./runs/detect/exp')
# exist_ok = False
sep=''
path = Path(path)  # os-agnostic
p_old = path
if path.exists():
    path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')

    # Method 1
    for n in range(2, 9999):
        p = f'{path}{sep}{n}{suffix}'  # increment path
        if os.path.exists(p):
            p_old = p
            # break
path = Path(p_old)
# csv_file_name = os.listdir('./runs/detect/')
# print(sorted(csv_file_name))
def animate(i):
    conf_list = pd.read_csv(path.joinpath('conf_list.csv'))
    # print(conf_list[:,0])
    plt.cla()
    plt.grid(False)
    # plt.figure(figsize=(19,7))
    plt.plot(conf_list["fire"], label="fire", color="red",fillstyle='full',linewidth=1)
    plt.plot(conf_list["smoke"], label="smoke", color="orange",linewidth=1,fillstyle='full')
    # plt.plot(conf_list["walk"], label="walk", color="green",linewidth=1,fillstyle='full')
    # plt.plot(conf_list["run"], label="run", color="green")
    # plt.plot(conf_list["sit"], label="sit", color="green")

    plt.legend(loc="upper left")
    # plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, frames=np.arange(5, 10), interval=1)

plt.tight_layout()
plt.show()