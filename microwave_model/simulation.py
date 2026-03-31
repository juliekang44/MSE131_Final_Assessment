import numpy as np
from parameters import *

np.random.seed(RANDOM_SEED)

def arrival_rate(t):
    # lunch rush between 11:30 and 2
    if 210 <= t <= 360:
        return ARRIVAL_RATE_BASE * LUNCH_MULTIPLIER
    return ARRIVAL_RATE_BASE

def simulate_building(servers):
    t = 0
    server_free = np.zeros(servers)

    wait_times = []
    flow_times = []
    busy_time = 0

    while t < SIM_TIME:
        lam = arrival_rate(t)
        t += np.random.exponential(1/lam)

        service = np.random.exponential(1/SERVICE_RATE)

        i = np.argmin(server_free)
        start = max(t, server_free[i])

        wait = start - t
        flow = wait + service

        wait_times.append(wait)
        flow_times.append(flow)

        server_free[i] = start + service
        busy_time += service

    Wq = np.mean(wait_times)
    W = np.mean(flow_times)

    # Little's Law
    Lq = ARRIVAL_RATE_BASE * Wq
    L = ARRIVAL_RATE_BASE * W

    utilization = busy_time / (SIM_TIME * servers)

    return {
        "Wq": Wq,
        "W": W,
        "Lq": Lq,
        "L": L,
        "utilization": utilization,
        "served": len(wait_times)
    }

def run_system(config):
    results = {}

    for building, servers in config.items():
        results[building] = simulate_building(servers)

    return results