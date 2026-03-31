# experiments.py
# Runs simulations, generates TXT reports, and creates plots

import os
import matplotlib.pyplot as plt
from datetime import datetime
from simulation import run_simulation

TIME_WINDOWS = {
    "off-peak": (0, 210),  # 8:00am–11:30am
    "peak": (210, 360),    # 11:30am–2:00pm
    "full-day": (0, 720)   # 8:00am–8:00pm
}

def choose_time_window():
    """
    Ask the user to select the time window to simulate.
    """
    print("Select simulation time window:")
    print("1: Off-Peak (8am–11:30am)")
    print("2: Peak Hours (11:30am–2pm)")
    print("3: Full Day (8am–8pm)")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        return TIME_WINDOWS["off-peak"], "Off-Peak"
    elif choice == "2":
        return TIME_WINDOWS["peak"], "Peak-Hours"
    else:
        return TIME_WINDOWS["full-day"], "Full-Day"

def run_simulation_with_plot(time_window, time_label):
    """
    Run the simulation and generate:
    - TXT report
    - Queue length plot
    - Utilization bar chart
    """
    os.makedirs("results", exist_ok=True)
    results = run_simulation()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Queue length plot
    plt.figure(figsize=(12,6))
    for b, r in results["buildings"].items():
        plt.plot(r["times"], r["queue_lengths"], label=b)
    plt.title(f"Queue Length Over Time ({time_label})")
    plt.xlabel("Time (minutes from 8am)")
    plt.ylabel("Queue Length")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"results/microwave_queue_{timestamp}.png")
    plt.close()

    # Utilization plot with bottleneck highlighted
    plt.figure(figsize=(10,5))
    buildings = list(results["buildings"].keys())
    utils = [r["utilization"] for r in results["buildings"].values()]
    colors = ['red' if b==results['bottleneck'] else 'green' for b in buildings]
    plt.bar(buildings, utils, color=colors)
    plt.title(f"Microwave Utilization by Building ({time_label})")
    plt.ylabel("Utilization")
    plt.ylim(0,1)
    plt.grid(axis='y')
    plt.savefig(f"results/microwave_utilization_{timestamp}.png")
    plt.close()

    # Save TXT report
    with open(f"results/microwave_results_{timestamp}.txt", "w") as f:
        f.write(f"Microwave Simulation - {time_label}\n")
        f.write("="*50 + "\n")
        f.write(f"Bottleneck building: {results['bottleneck']}\n\n")
        for b,r in results["buildings"].items():
            f.write(f"{b}:\n")
            f.write(f"  Avg Wait: {r['Wq']:.2f} min\n")
            f.write(f"  Avg Flow: {r['W']:.2f} min\n")
            f.write(f"  Utilization: {r['utilization']:.2f}\n")
            f.write(f"  Throughput: {r['throughput']:.2f} cust/min\n")
            f.write(f"  Peak Queue: {max(r['queue_lengths'])}\n")
            f.write(f"  Balked: {r['balked']}\n\n")

    print("Simulation complete! Files saved in results/")
    print(f"TXT, Queue plot, and Utilization plot generated with timestamp {timestamp}")

if __name__ == "__main__":
    time_window, time_label = choose_time_window()
    run_simulation_with_plot(time_window, time_label)