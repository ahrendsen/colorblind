# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 15:31:07 2025

@author: karl
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

d = pd.read_csv(
    "colorValuesSpreadsheet.csv",
)

palettes = int(d["Palette Number"].iloc[-1]) + 1
for paletteNumber in range(palettes):
    palette1 = d[d["Palette Number"] == str(paletteNumber)]

    numColors = len(palette1)
    boxDim = 0.5
    fig = plt.figure(figsize=(numColors, 1))

    # fig.suptitle(name)
    ax = fig.add_subplot()
    for i, color in enumerate(palette1["RGB (hex)"]):
        artist = mpatches.Rectangle(
            (boxDim * i, 0),
            boxDim,
            boxDim,
            angle=0 * 180 / 3.14,
            fc="#" + color,
            ec="None",
            ls="--",
        )
        ax.add_artist(artist)

    name = d.iloc[palette1.iloc[0].name - 1]["Palette Number"][1:]
    ax.set_title(name)
    ax.set_axis_off()
    ax.set_xlim([0, boxDim * len(palette1)])
    ax.set_ylim([0, boxDim])

    plt.show()


def gen_matplotlib(df: pd.DataFrame):
    return (df["RGB (hex)"]).values.tolist()


def gen_markdown(df: pd.DataFrame):
    headers = "|" + "|".join(df.columns.values[1:]) + "|"
    separator = (
        "|"
        + "|".join(["---" for _ in range(len(df.columns.values[1:]))])
        + "|"
    )
    table = [
        "|"
        + "|".join(
            [str(x) for x in df.drop("Palette Number", axis=1).iloc[k].values]
        )
        + "|"
        for k in range(len(df))
    ]
    return headers + "\n" + separator + "\n" + "\n".join(table)
