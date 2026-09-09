#!/usr/bin/env python3
"""Plot stored comparison metrics; this script does not run a simulation."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from verify_metrics import DATA, verify

OUT = Path(__file__).resolve().parents[1] / "figures"
TEAL, BLUE, AMBER = "#087f74", "#416d99", "#ab641d"

def clean(ax):
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#c9d2db")
    ax.grid(axis="x", color="#e5ebef", zorder=0)
    ax.tick_params(axis="both", length=0, pad=9, colors="#344a5a")
    ax.set_axisbelow(True)

def main():
    verify(DATA)
    with DATA.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    a, b, c, selected = rows
    OUT.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15})
    # Isolate the original B/C question with a zero baseline.
    fig, ax = plt.subplots(figsize=(11, 4.1))
    vals = [float(b["curveRMS"])*1000, float(c["curveRMS"])*1000]
    ax.barh([1, 0], vals, height=.45, color=[TEAL, BLUE], zorder=3)
    ax.set_yticks([1, 0], ["B  Feedback + feedforward", "C  Feedback + integral\n    + feedforward"])
    ax.set_xlim(0, 12.5);ax.set_xticks([0, 3, 6, 9, 12]);ax.set_ylim(-.65, 1.65)
    for y, value in zip([1, 0], vals):
        ax.text(value+.16, y, f"{value:.2f}", va="center", fontsize=19, fontweight="bold")
    ax.set_xlabel("Curve lateral-error RMS [mm]", labelpad=12)
    clean(ax)
    fig.text(.035, .90, "Adding integral action did not reduce curve error here.", fontsize=20, fontweight="bold", color="#142532")
    fig.text(.035, .81, "80 km/h simulation · initial lateral error 1 m · original manual settings", fontsize=13, color="#52606d")
    fig.subplots_adjust(left=.365, right=.97, top=.73, bottom=.22)
    fig.savefig(OUT/"structure-comparison.png", dpi=140, facecolor="white")
    plt.close(fig)
    # Same values in a narrow layout for phones.
    fig, ax = plt.subplots(figsize=(6, 4.8))
    ax.barh([1, 0], vals, height=.35, color=[TEAL, BLUE], zorder=3)
    ax.set_yticks([1, 0], ["B", "C"]);ax.set_xlim(0, 12.5);ax.set_xticks([0, 3, 6, 9, 12]);ax.set_ylim(-.5, 1.65)
    for y, v in zip([1, 0], vals):ax.text(v+.15,y,f"{v:.2f}",va="center",fontsize=18,fontweight="bold")
    ax.set_xlabel("Curve RMS [mm]", labelpad=10);clean(ax)
    fig.text(.06,.91,"B: Feedback + feedforward",fontsize=17,fontweight="bold",color=TEAL)
    fig.text(.06,.845,"C: B + integral action",fontsize=17,fontweight="bold",color=BLUE)
    fig.text(.06,.775,"80 km/h simulation · initial error 1 m",fontsize=12,color="#52606d")
    fig.subplots_adjust(left=.13,right=.96,top=.73,bottom=.19)
    fig.savefig(OUT/"structure-comparison-mobile.png",dpi=140,facecolor="white")
    plt.close(fig)
    # Reported selection is distinct from the A/B/C structure comparison.
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.7))
    for ax, field, factor, label in zip(axes,["curveRMS","dfmax"],[1000,1],["Curve RMS [mm]","Peak front-wheel steer [deg]"]):
        values=[float(b[field])*factor,float(selected[field])*factor]
        bars=ax.barh([1,0],values,height=.38,color=[TEAL,AMBER],zorder=3)
        bars[1].set_hatch("///");bars[1].set_edgecolor("#7e4f20")
        ax.set_yticks([1,0],["B","Reported selection*"]);ax.set_ylim(-.5,1.5)
        ax.set_xlim(0,max(values)*1.27)
        ax.set_title(label,loc="left",fontsize=17,fontweight="bold",pad=14)
        for y,v in zip([1,0],values):ax.text(v+max(values)*.025,y,f"{v:.2f}",va="center",fontweight="bold")
        clean(ax)
    fig.text(.035,.945,"Less steering, with more tracking error than B",fontsize=20,fontweight="bold",color="#142532")
    fig.text(.035,.055,"* Reported Q/R selection; values from stored simulation metrics.",fontsize=12,color="#52606d")
    fig.subplots_adjust(left=.29,right=.97,top=.83,bottom=.15,hspace=.70)
    fig.savefig(OUT/"tradeoff.png",dpi=140,facecolor="white")
    plt.close(fig)

if __name__ == "__main__":
    main()
