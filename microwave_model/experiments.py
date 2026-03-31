import pandas as pd
from simulation import run_system
from parameters import MICROWAVES

def run():
    scenarios = {
        "Baseline": MICROWAVES,
        "Add_E7": {**MICROWAVES, "E7": MICROWAVES["E7"] + 1},
        "Add_E5": {**MICROWAVES, "E5": MICROWAVES["E5"] + 1}
    }

    rows = []

    for name, config in scenarios.items():
        results = run_system(config)

        for b, r in results.items():
            rows.append({
                "scenario": name,
                "building": b,
                **r
            })

    df = pd.DataFrame(rows)

    # identify bottleneck
    bottleneck = df.loc[df["utilization"].idxmax()]

    print("\n=== Bottleneck ===")
    print(bottleneck)

    print("\n=== Full Results ===")
    print(df)

    df.to_csv("results/scenario_results.csv", index=False)

if __name__ == "__main__":
    run()