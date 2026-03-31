import os
import numpy as np
from simulation import run_simulation

OUTPUT_FILE = "results/microwave_results.txt"
REPLICATIONS = 50


def run_monte_carlo():

    os.makedirs("results", exist_ok=True)

    waits = []
    flows = []
    utils = []

    building_waits = {}

    for _ in range(REPLICATIONS):

        results = run_simulation()

        waits.append(results["avg_wait"])
        flows.append(results["avg_flow"])
        utils.append(results["utilization"])

        for b, r in results["buildings"].items():
            building_waits.setdefault(b, []).append(r["Wq"])

    def ci(data):
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        margin = 1.96 * std / np.sqrt(len(data))
        return mean, mean - margin, mean + margin, std

    wait_mean, wait_lo, wait_hi, wait_std = ci(waits)
    flow_mean, flow_lo, flow_hi, flow_std = ci(flows)
    util_mean, util_lo, util_hi, util_std = ci(utils)

    with open(OUTPUT_FILE, "w") as f:

        f.write("University of Waterloo Microwave Queue Simulation\n")
        f.write("=" * 60 + "\n\n")

        f.write("MONTE CARLO RESULTS (95% Confidence Intervals)\n")
        f.write("-" * 50 + "\n")

        f.write(f"Replications: {REPLICATIONS}\n\n")

        f.write("SYSTEM METRICS\n")
        f.write(f"Average Wait Time: {wait_mean:.2f} minutes\n")
        f.write(f"95% CI: [{wait_lo:.2f}, {wait_hi:.2f}]\n")
        f.write(f"Std Dev: {wait_std:.2f}\n\n")

        f.write(f"Average Flow Time: {flow_mean:.2f} minutes\n")
        f.write(f"95% CI: [{flow_lo:.2f}, {flow_hi:.2f}]\n")
        f.write(f"Std Dev: {flow_std:.2f}\n\n")

        f.write(f"Utilization: {util_mean:.2f}\n")
        f.write(f"95% CI: [{util_lo:.2f}, {util_hi:.2f}]\n")
        f.write(f"Std Dev: {util_std:.2f}\n\n")

        f.write("\nBUILDING WAIT TIMES (with CI)\n")
        f.write("-" * 50 + "\n")

        for b, data in building_waits.items():
            m, lo, hi, s = ci(data)

            f.write(f"\n{b}\n")
            f.write(f"  Mean Wait: {m:.2f}\n")
            f.write(f"  95% CI: [{lo:.2f}, {hi:.2f}]\n")
            f.write(f"  Std Dev: {s:.2f}\n")


if __name__ == "__main__":
    run_monte_carlo()