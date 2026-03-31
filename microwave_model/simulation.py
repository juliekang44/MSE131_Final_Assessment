import numpy as np
from parameters import *

np.random.seed(RANDOM_SEED)


def arrival_rate(t):
    # lunch rush between 11:30 and 2:00
    if 210 <= t <= 360:
        return ARRIVAL_RATE_BASE * LUNCH_MULTIPLIER
    return ARRIVAL_RATE_BASE


def simulate_building(servers):
    t = 0
    server_free = np.zeros(servers)

    wait_times = []
    flow_times = []
    busy_time = 0
    served = 0
    balked = 0

    while t < SIM_TIME:

        lam = arrival_rate(t)
        t += np.random.exponential(1 / lam)

        service = np.random.exponential(1 / SERVICE_RATE)

        i = np.argmin(server_free)
        start = max(t, server_free[i])

        wait = start - t

        # balking
        if wait > QUEUE_LIMIT:
            balked += 1
            continue

        flow = wait + service

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

    utilization = busy_time / (SIM_TIME * servers)
    throughput = served / SIM_TIME

    return {
        "Wq": Wq,
        "W": W,
        "Lq": Lq,
        "L": L,
        "utilization": utilization,
        "throughput": throughput,
        "served": served,
        "balked": balked
    }


def run_simulation():
    results = {}

    for building, servers in MICROWAVES.items():
        results[building] = simulate_building(servers)

    # system aggregates
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