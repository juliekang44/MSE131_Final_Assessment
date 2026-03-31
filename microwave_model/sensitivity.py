import os
from datetime import datetime
from simulation import run_system, plot_queue_time_series, plot_utilization_bars
from parameters import MICROWAVES

OUTPUT_DIR = "results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Predefined options
ARRIVAL_RATES = [0.08, 0.12, 0.16]  # students per minute
SERVICE_RATES = [1/3, 1/2, 1/1.5]   # mean service times: 3 min, 2 min, 1.5 min

def select_option(prompt, options):
    """Prompt user to select an option; repeat until valid."""
    while True:
        print(prompt)
        for i, val in enumerate(options, start=1):
            if "SERVICE" in prompt.upper():
                print(f"{i}: {val:.3f} per minute (mean service {1/val:.1f} min)")
            else:
                print(f"{i}: {val:.2f} students per minute")
        choice = input("Enter the number corresponding to your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice)-1]
        else:
            print(f"Invalid input. Please enter a number between 1 and {len(options)}.\n")

def save_results_txt(results, arrival_rate, service_rate):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(
        OUTPUT_DIR, f"sensitivity_arrival_{arrival_rate}_service_{service_rate}_{timestamp}.txt"
    )
    with open(file_path, "w") as f:
        f.write(f"Sensitivity Analysis - Arrival Rate: {arrival_rate}, Service Rate: {service_rate}\n")
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
    print(f"\nResults saved to {file_path}\n")

def run_sensitivity():
    print("=== Sensitivity Analysis - Interactive ===\n")
    
    # User selects arrival rate
    arrival_rate = select_option("Select an arrival rate (students per minute):", ARRIVAL_RATES)
    
    # User selects service rate
    service_rate = select_option("Select a service rate (per minute, mean service = 1 / rate minutes):", SERVICE_RATES)
    
    print(f"\nRunning simulation for arrival rate = {arrival_rate}, service rate = {service_rate}...\n")
    
    # Run the simulation only for chosen parameters
    results = run_system(MICROWAVES, arrival_rate_override=arrival_rate, service_rate_override=service_rate)
    
    # Save results
    save_results_txt(results, arrival_rate, service_rate)
    
    # Plot queue vs time
    plot_queue_time_series(results, sim_desc=f"Arrival {arrival_rate}, Service {service_rate}")
    
    # Plot utilization
    plot_utilization_bars(results, sim_desc=f"Arrival {arrival_rate}, Service {service_rate}")
    
    print("Simulation complete. Plots saved in results/ folder.\n")

if __name__ == "__main__":
    run_sensitivity()