import os
from simulation import run_simulation
from parameters import *

OUTPUT_FILE = "results/microwave_results.txt"


def run_sensitivity():

    os.makedirs("results", exist_ok=True)

    multipliers = [1.0, 1.5, 2.0, 2.5]

    with open(OUTPUT_FILE, "a") as f:

        f.write("\n\nSENSITIVITY ANALYSIS\n")
        f.write("=" * 60 + "\n")

        for m in multipliers:

            global LUNCH_MULTIPLIER
            LUNCH_MULTIPLIER = m

            results = run_simulation()

            f.write(f"\nLunch Multiplier: {m}\n")
            f.write(f"Avg Wait: {results['avg_wait']:.2f}\n")
            f.write(f"Avg Flow: {results['avg_flow']:.2f}\n")
            f.write(f"Utilization: {results['utilization']:.2f}\n")
            f.write(f"Bottleneck: {results['bottleneck']}\n")