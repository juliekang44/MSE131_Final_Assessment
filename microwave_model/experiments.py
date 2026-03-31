import os
import numpy as np
from simulation import run_simulation
from datetime import datetime

# Number of Monte Carlo replications
REPLICATIONS = 30  

# Map for time window options
TIME_WINDOWS = {
    "off-peak": (0, 720),      # 8am–8pm without lunch rush
    "peak": (210, 360),        # 11:30–2pm
    "full-day": (0, 720)
}


def choose_time_window():
    print("Select simulation time window:")
    print("1: Off-Peak (before lunch or after lunch)")
    print("2: Peak Hours (11:30am - 2:00pm)")
    print("3: Full Day (8am-8pm)")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        return TIME_WINDOWS["off-peak"], "Off-Peak"
    elif choice == "2":
        return TIME_WINDOWS["peak"], "Peak-Hours"
    else:
        return TIME_WINDOWS["full-day"], "Full-Day"


def run_monte_carlo(time_window):
    # override global SIM_TIME to match selected window
    from parameters import SIM_TIME
    sim_start, sim_end = time_window
    SIM_TIME_LOCAL = sim_end - sim_start

    waits = []
    flows = []
    utils = []

    building_waits = {}

    for _ in range(REPLICATIONS):
        # randomized seed for each replication
        np.random.seed(None)

        results = run_simulation()

        waits.append(results["avg_wait"])
        flows.append(results["avg_flow"])
        utils.append(results["utilization"])

        for b, r in results["buildings"].items():
            building_waits.setdefault(b, []).append(r["Wq"])

    # Confidence interval function
    def ci(data):
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        margin = 1.96 * std / np.sqrt(len(data))
        return mean, mean - margin, mean + margin, std

    wait_mean, wait_lo, wait_hi, wait_std = ci(waits)
    flow_mean, flow_lo, flow_hi, flow_std = ci(flows)
    util_mean, util_lo, util_hi, util_std = ci(utils)

    # timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results/microwave_results_{timestamp}.txt"

    os.makedirs("results", exist_ok=True)

    with open(filename, "w") as f:
        f.write(f"University of Waterloo Microwave Queue Simulation\n")
        f.write(f"Time Window: {time_label}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"MONTE CARLO RESULTS (95% Confidence Intervals) - {REPLICATIONS} Replications\n")
        f.write("-" * 60 + "\n\n")

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

    print(f"\nSimulation complete! Results saved to {filename}")


if __name__ == "__main__":
    time_window, time_label = choose_time_window()
    run_monte_carlo(time_window)