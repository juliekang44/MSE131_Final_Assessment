import numpy as np
from parameters import *

np.random.seed(None)  # remove fixed seed for full randomness

def arrival_rate(t):
    # lunch rush between 11:30 and 2
    if 210 <= t <= 360:
        return ARRIVAL_RATE_BASE * LUNCH_MULTIPLIER
    return ARRIVAL_RATE_BASE

def simulate_building(servers, sim_time=SIM_TIME):
    t = 0
    server_free = np.zeros(servers)

    wait_times = []
    flow_times = []
    busy_time = 0
    served = 0
    balked = 0

    # Track queue length over time
    times = []
    queue_lengths = []

    queue = 0  # current queue length

    while t < sim_time:
        lam = arrival_rate(t)
        t += np.random.exponential(1 / lam)
        service = np.random.exponential(1 / SERVICE_RATE)

        # Choose earliest free server
        i = np.argmin(server_free)
        start = max(t, server_free[i])
        wait = start - t

        # Balking
        if wait > QUEUE_LIMIT:
            balked += 1
            continue

        flow = wait + service

        # update queue length
        queue = sum(server_free > t)  # servers busy at current time
        times.append(t)
        queue_lengths.append(queue)

        wait_times.append(wait)
        flow_times.append(flow)

        server_free[i] = start + service
        busy_time += service
        served += 1

    if served == 0:
        served = 1

    Wq = np.mean(wait_times)
    W = np.mean(flow_times)
    Lq = ARRIVAL_RATE_BASE * Wq
    L = ARRIVAL_RATE_BASE * W
    utilization = busy_time / (sim_time * servers)
    throughput = served / sim_time

    return {
        "Wq": Wq,
        "W": W,
        "Lq": Lq,
        "L": L,
        "utilization": utilization,
        "throughput": throughput,
        "served": served,
        "balked": balked,
        "times": times,
        "queue_lengths": queue_lengths
    }

def run_simulation():
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