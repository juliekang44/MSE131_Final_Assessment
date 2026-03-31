import os
import matplotlib.pyplot as plt
from datetime import datetime
from simulation import run_simulation
from parameters import MICROWAVES

# Monte Carlo replications
REPLICATIONS = 20

TIME_WINDOWS = {
    "off-peak": (0, 720),
    "peak": (210, 360),
    "full-day": (0, 720)
}

def choose_time_window():
    print("Select simulation time window:")
    print("1: Off-Peak")
    print("2: Peak Hours")
    print("3: Full Day")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        return TIME_WINDOWS["off-peak"], "Off-Peak"
    elif choice == "2":
        return TIME_WINDOWS["peak"], "Peak-Hours"
    else:
        return TIME_WINDOWS["full-day"], "Full-Day"

def run_simulation_with_plot(time_window, time_label):
    os.makedirs("results", exist_ok=True)

    # Run one simulation for plotting
    results = run_simulation()

    # --- PLOT QUEUE LENGTHS ---
    plt.figure(figsize=(12, 6))
    for building, r in results["buildings"].items():
        plt.plot(r["times"], r["queue_lengths"], label=building)

    plt.title(f"Microwave Queue Lengths over Time ({time_label})")
    plt.xlabel("Time (minutes from 8am)")
    plt.ylabel("Queue Length")
    plt.legend()
    plt.grid(True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_file = f"results/microwave_queue_plot_{timestamp}.png"
    plt.savefig(plot_file)
    plt.close()

    # --- PLOT UTILIZATION BAR CHART ---
    plt.figure(figsize=(10, 5))
    buildings = list(results["buildings"].keys())
    utils = [r["utilization"] for r in results["buildings"].values()]

    colors = ['red' if b == results["bottleneck"] else 'green' for b in buildings]

    plt.bar(buildings, utils, color=colors)
    plt.title(f"Microwave Utilization by Building ({time_label})")
    plt.ylabel("Utilization")
    plt.ylim(0, 1.0)
    plt.grid(axis='y')

    util_file = f"results/microwave_utilization_{timestamp}.png"
    plt.savefig(util_file)
    plt.close()

    # --- SAVE RESULTS TO TXT ---
    filename = f"results/microwave_results_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Microwave Simulation - {time_label}\n")
        f.write("="*50 + "\n")
        f.write(f"Bottleneck building: {results['bottleneck']}\n\n")

        for b, r in results["buildings"].items():
            f.write(f"{b}:\n")
            f.write(f"  Avg Wait: {r['Wq']:.2f} min\n")
            f.write(f"  Utilization: {r['utilization']:.2f}\n")
            f.write(f"  Peak Queue: {max(r['queue_lengths'])}\n")
            f.write("\n")

    print(f"Simulation complete! TXT saved to {filename}")
    print(f"Queue plot saved to {plot_file}")
    print(f"Utilization plot saved to {util_file}")


if __name__ == "__main__":
    time_window, time_label = choose_time_window()
    run_simulation_with_plot(time_window, time_label)