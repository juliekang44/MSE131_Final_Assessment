import numpy as np

RANDOM_SEED = 42

# simulation time (8am–8pm)
SIM_TIME = 12 * 60

# microwaves per building
MICROWAVES = {
    "QNC": 1,
    "CPH": 4,
    "DWE": 2,
    "E5": 1,
    "E6": 2,
    "E7": 3
}

# arrivals per minute
ARRIVAL_RATE_BASE = 0.12
LUNCH_MULTIPLIER = 2.5

# service rate (mean 2 minutes)
SERVICE_RATE = 1/2

# max acceptable wait (minutes)
QUEUE_LIMIT = 8