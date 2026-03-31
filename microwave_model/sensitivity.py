# sensitivity.py
# Sensitivity analysis for UW Engineering microwave simulation

import os
from simulation import run_simulation
from parameters import ARRIVAL_RATE_BASE, SERVICE_RATE

OUTPUT_FOLDER = "results"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def run_sensitivity():
    """
    Runs sensitivity analysis by varying ARRIVAL_RATE_BASE and SERVICE_RATE
    and outputs TXT reports comparing system performance.
    """
    arrival_rates = [0.08, 0.12, 0.16]  # students per minute (low, medium, high)
    service_rates = [1/3, 1/2, 1/1.5]  # mean service times 3, 2, 1.5 min

    with open(f"{OUTPUT_FOLDER}/sensitivity_results.txt", "w") as f:
        f.write("Microwave Simulation Sensitivity Analysis\n")
        f.write("="*50 + "\n\n")

        # Vary arrival rate
        f.write("### Varying Arrival Rate (ARRIVAL_RATE_BASE)\n")
        for rate in arrival_rates:
            # Temporarily override global parameter
            from parameters import ARRIVAL_RATE_BASE as original_rate
            import parameters
            parameters.ARRIVAL_RATE_BASE = rate

            results = run_simulation()
            f.write(f"Arrival Rate: {rate:.2f} students/min\n")
            f.write(f"Average wait: {results['avg_wait']:.2f} min\n")
            f.write(f"Average flow: {results['avg_flow']:.2f} min\n")
            f.write(f"Utilization: {results['utilization']:.2f}\n")
            f.write(f"Bottleneck: {results['bottleneck']}\n")
            f.write("-"*30 + "\n")

            # Reset to original
            parameters.ARRIVAL_RATE_BASE = original_rate

        # Vary service rate
        f.write("\n### Varying Service Rate (SERVICE_RATE)\n")
        for rate in service_rates:
            from parameters import SERVICE_RATE as original_service
            import parameters
            parameters.SERVICE_RATE = rate

            results = run_simulation()
            f.write(f"Service Rate: {rate:.2f} per min (mean {1/rate:.2f} min)\n")
            f.write(f"Average wait: {results['avg_wait']:.2f} min\n")
            f.write(f"Average flow: {results['avg_flow']:.2f} min\n")
            f.write(f"Utilization: {results['utilization']:.2f}\n")
            f.write(f"Bottleneck: {results['bottleneck']}\n")
            f.write("-"*30 + "\n")

            # Reset to original
            parameters.SERVICE_RATE = original_service

    print(f"Sensitivity analysis complete. See {OUTPUT_FOLDER}/sensitivity_results.txt")

if __name__ == "__main__":
    run_sensitivity()