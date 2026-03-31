import numpy as np
import matplotlib.pyplot as plt
from parameters import MICROWAVES, ARRIVAL_RATE_BASE, LUNCH_MULTIPLIER, SERVICE_RATE, QUEUE_LIMIT, SIM_TIME
from datetime import datetime

# Optional: remove seed for stochastic runs
# np.random.seed(42)

def arrival_rate(t, base_rate=ARRIVAL_RATE_BASE):
    """Dynamic arrival rate with lunch rush multiplier."""
    if 210 <= t <= 360:  # 11:30am–2pm
        return base_rate * LUNCH_MULTIPLIER
    return base_rate

def simulate_building(servers, sim_start=0, sim_end=SIM_TIME, arrival_rate_override=None, service_rate_override=None):
    """Simulate a single building microwave queue."""
    t = sim_start
    server_free = np.zeros(servers)
    wait_times = []
    flow_times = []
    busy_time = 0
    queue_lengths = []
    balked = 0

    while t < sim_end:
        lam = arrival_rate(t) if arrival_rate_override is None else arrival_rate_override
        dt = np.random.exponential(1 / lam) if lam > 0 else 1
        t += dt
        service = np.random.exponential(1 / SERVICE_RATE if service_rate_override is None else 1 / service_rate_override)

        # Determine the server with earliest free time
        i = np.argmin(server_free)
        start = max(t, server_free[i])
        wait = start - t
        flow = wait + service

        # Balking if queue too long
        current_queue = sum([1 if server_free[j] > t else 0 for j in range(servers)])
        if current_queue >= QUEUE_LIMIT:
            balked += 1
            continue

        wait_times.append(wait)
        flow_times.append(flow)
        queue_lengths.append(current_queue)
        server_free[i] = start + service
        busy_time += service

    Wq = np.mean(wait_times) if wait_times else 0
    W = np.mean(flow_times) if flow_times else 0
    Lq = (ARRIVAL_RATE_BASE if arrival_rate_override is None else arrival_rate_override) * Wq
    L = (ARRIVAL_RATE_BASE if arrival_rate_override is None else arrival_rate_override) * W
    utilization = busy_time / (sim_end * servers)
    peak_queue = max(queue_lengths) if queue_lengths else 0

    return {
        "Wq": Wq,
        "W": W,
        "Lq": Lq,
        "L": L,
        "utilization": utilization,
        "served": len(wait_times),
        "peak_queue": peak_queue,
        "balked": balked,
        "queue_lengths": queue_lengths
    }

def run_system(config, sim_start=0, sim_end=SIM_TIME, arrival_rate_override=None, service_rate_override=None):
    """Simulate all buildings and return results dict."""
    results = {}
    for building, servers in config.items():
        results[building] = simulate_building(
            servers,
            sim_start=sim_start,
            sim_end=sim_end,
            arrival_rate_override=arrival_rate_override,
            service_rate_override=service_rate_override
        )
    return results

def plot_queue_time_series(results, sim_desc="Simulation"):
    """Plot queue length vs time per building (in hours)."""
    plt.figure(figsize=(10,6))
    for building, data in results.items():
        queue_len = data["queue_lengths"]
        if queue_len:
            times = np.linspace(0, len(queue_len), len(queue_len)) * (SIM_TIME / len(queue_len)) / 60
            plt.plot(times, queue_len, label=building)
    plt.xlabel("Time (hours)")
    plt.ylabel("Queue Length")
    plt.title(f"Queue Length vs Time - {sim_desc}")
    plt.legend()
    plt.grid(True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(f"results/queue_plot_{sim_desc.replace(' ','_')}_{timestamp}.png")
    plt.close()

def plot_utilization_bars(results, sim_desc="Simulation"):
    """Plot building utilization bar chart with bottleneck highlighted."""
    buildings = list(results.keys())
    utilizations = [results[b]["utilization"] for b in buildings]
    max_util = max(utilizations)
    colors = ['red' if u == max_util else 'blue' for u in utilizations]

    plt.figure(figsize=(10,6))
    plt.bar(buildings, utilizations, color=colors)
    plt.ylabel("Utilization")
    plt.title(f"Building Utilization - {sim_desc}")
    for i, u in enumerate(utilizations):
        plt.text(i, u + 0.01, f"{u:.2f}", ha='center')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(f"results/utilization_bar_{sim_desc.replace(' ','_')}_{timestamp}.png")
    plt.close()