import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use("style.mplstyle")

df = pd.read_excel("plotdatapractice.xlsx")


sources = ["Solar", "Wind", "Nuclear", "Hydro", "Coal", "Natural Gas", "Other"]
colors = {"Solar": "#FFC919", "Wind": "#63d0ff", "Hydro": "#002b53", "Nuclear": "#7E0080", "Coal": "#D3D3D3", "Natural Gas": "#008111", "Other": "#6A0000"}



fig, ax = plt.subplots(figsize=(6, 4))


ax.stackplot(df.index, df["Solar"], df["Wind"], df["Nuclear"], df["Hydro"], df["Coal"], df["Natural Gas"], df["Other"], labels=sources, colors=[colors[src] for src in sources])

ax.set_xlabel("Hours of the Year"); ax.set_ylabel("Total Generation (MW)")
ax.set_title("ISNE 2019 Generation"); ax.set_xlim(0, 8760); ax.set_ylim(0, 22000)
ax.set_xticks([0, 800, 1600, 2400, 3200, 4000, 4800, 5600, 6400, 7200, 8000, 8760]); ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=45)

ax.legend(loc="upper right", fontsize=10)

plt.show()
