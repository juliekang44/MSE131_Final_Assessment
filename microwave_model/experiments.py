import os
from simulation import run_simulation

OUTPUT_FILE = "results/microwave_results.txt"


def run_baseline():

    os.makedirs("results", exist_ok=True)

    results = run_simulation()

    with open(OUTPUT_FILE, "w") as f:

        f.write("University of Waterloo Engineering Microwave Simulation\n")
        f.write("=" * 60 + "\n\n")

        f.write("BASELINE RESULTS\n")
        f.write("-" * 40 + "\n")

        f.write(f"Average wait time: {results['avg_wait']:.2f} minutes\n")
        f.write(f"Average flow time: {results['avg_flow']:.2f} minutes\n")
        f.write(f"Average utilization: {results['utilization']:.2f}\n")
        f.write(f"Bottleneck building: {results['bottleneck']}\n\n")

        f.write("BUILDING RESULTS\n")
        f.write("-" * 40 + "\n")

        for b, r in results["buildings"].items():
            f.write(f"\n{b}\n")
            f.write(f"  Wait time (Wq): {r['Wq']:.2f}\n")
            f.write(f"  Flow time (W): {r['W']:.2f}\n")
            f.write(f"  Queue length (Lq): {r['Lq']:.2f}\n")
            f.write(f"  In system (L): {r['L']:.2f}\n")
            f.write(f"  Utilization: {r['utilization']:.2f}\n")
            f.write(f"  Throughput: {r['throughput']:.3f}\n")
            f.write(f"  Served: {r['served']}\n")
            f.write(f"  Balked: {r['balked']}\n")


if __name__ == "__main__":
    run_baseline()