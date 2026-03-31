# simulation.py
# Core simulation logic for microwave queues

import numpy as np
from parameters import *

# Set random seed
np.random.seed(RANDOM_SEED)

def arrival_rate(t):
    """
    Return arrival rate (students per minute) at time t (minutes from 8am).
    Includes lunch rush multiplier between 11:30am-2pm.
    """
    if 210 <= t <= 360:  # lunch rush
        return ARRIVAL_RATE_BASE * LUNCH_MULTIPLIER
    return ARRIVAL_RATE_BASE

def simulate_building(servers, sim_time=SIM_TIME):
    """
    Simulate one building with 'servers' microwaves.
    Returns performance metrics and queue history for plotting.
    """
    t = 0
    server_free = np.zeros(servers)

    wait_times = []
    flow_times = []
    busy_time = 0
    served = 0
    balked = 0

    times = []
    queue_lengths = []

    while t < sim_time:
        lam = arrival_rate(t)
        t += np.random.exponential(1 / lam)  # stochastic arrival
        service = np.random.exponential(1 / SERVICE_RATE)  # stochastic service

        i = np.argmin(server_free)  # next available microwave
        start = max(t, server_free[i])
        wait = start - t

        # Balking: leave if queue too long
        if wait > QUEUE_LIMIT:
            balked += 1
            continue

        flow = wait + service

        # Queue length = number of busy servers at current time
        queue = sum(server_free > t)
        times.append(t)
        queue_lengths.append(queue)

        wait_times.append(wait)
        flow_times.append(flow)

        server_free[i] = start + service
        busy_time += service
        served += 1

    if served == 0:
        served = 1  # avoid division by zero

    Wq = np.mean(wait_times)
    W = np.mean(flow_times)
    utilization = busy_time / (sim_time * servers)
    throughput = served / sim_time

    return {
        "Wq": Wq,
        "W": W,
        "utilization": utilization,
        "throughput": throughput,
        "served": served,
        "balked": balked,
        "times": times,
        "queue_lengths": queue_lengths
    }

def run_simulation():
    """
    Run the simulation for all buildings.
    Returns system-wide and per-building metrics.
    """
    results = {}
    for building, servers in MICROWAVES.items():
        results[building] = simulate_building(servers)

    avg_wait = np.mean([r["Wq"] for r in results.values()])
    avg_flow = np.mean([r["W"] for r in results.values()])
    avg_util = np.mean([r["utilization"] for r in results.values()])
    bottleneck = max(results, key=lambda x: results[x]["utilization"])

    return {
        "avg_wait": avg_wait,
        "avg_flow": avg_flow,
        "utilization": avg_util,
        "bottleneck": bottleneck,
        "buildings": results
    }