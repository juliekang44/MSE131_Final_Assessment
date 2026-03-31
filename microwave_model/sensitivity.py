import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulation import simulate_building
from parameters import MICROWAVES

def run():
    rates = np.linspace(0.05, 0.25, 8)

    rows = []

    for rate in rates:
        from parameters import ARRIVAL_RATE_BASE
        ARRIVAL_RATE_BASE = rate

        for b, m in MICROWAVES.items():
            r = simulate_building(m)

            rows.append({
                "arrival_rate": rate,
                "building": b,
                "Wq": r["Wq"]
            })

    df = pd.DataFrame(rows)
    df.to_csv("results/sensitivity_results.csv", index=False)

    for b in df["building"].unique():
        subset = df[df["building"] == b]
        plt.plot(subset["arrival_rate"], subset["Wq"], label=b)

    plt.xlabel("Arrival rate λ")
    plt.ylabel("Waiting time Wq")
    plt.title("Sensitivity Analysis")
    plt.legend()

    plt.savefig("results/sensitivity_plot.png")
    plt.show()

if __name__ == "__main__":
    run()