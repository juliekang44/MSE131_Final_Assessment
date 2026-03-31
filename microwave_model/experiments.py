import os
from datetime import datetime
from simulation import run_system, plot_queue_time_series, plot_utilization_bars
from parameters import MICROWAVES, SIM_TIME

OUTPUT_DIR = "results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TIME_WINDOWS = {
    "1": ("Off-Peak (8am–11:30am)", 0, 210),
    "2": ("Peak Hours (11:30am–2pm)", 210, 360),
    "3": ("Full Day (8am–8pm)", 0, SIM_TIME)
}

def select_time_window():
    print("Select simulation time window:")
    print("1: Off-Peak (8am–11:30am)")
    print("2: Peak Hours (11:30am–2pm)")
    print("3: Full Day (8am–8pm)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in TIME_WINDOWS:
            desc, start_min, end_min = TIME_WINDOWS[choice]
            print(f"\nRunning simulation for: {desc} ({start_min}-{end_min} minutes)\n")
            return desc, start_min, end_min
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def save_results_txt(results, sim_desc):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"microwave_results_{timestamp}.txt")
    with open(file_path, "w") as f:
        f.write(f"UW Engineering Microwave Queue Simulation - {sim_desc}\n")
        f.write("="*60 + "\n\n")
        for building, metrics in results.items():
            f.write(f"Building: {building}\n")
            f.write(f" - Average Wait Time (Wq): {metrics['Wq']:.2f} min\n")
            f.write(f" - Average Flow Time (W): {metrics['W']:.2f} min\n")
            f.write(f" - Utilization: {metrics['utilization']:.2f}\n")
            f.write(f" - Throughput (served): {metrics['served']}\n")
            f.write(f" - Peak Queue Length: {metrics['peak_queue']}\n")
            f.write(f" - Students Balked: {metrics['balked']}\n\n")
        f.write("="*60 + "\n")
    print(f"Results saved to {file_path}")

def main():
    sim_desc, start_min, end_min = select_time_window()
    results = run_system(MICROWAVES, sim_start=start_min, sim_end=end_min)
    save_results_txt(results, sim_desc)
    plot_queue_time_series(results, sim_desc=sim_desc)
    plot_utilization_bars(results, sim_desc=sim_desc)

if __name__ == "__main__":
    main()