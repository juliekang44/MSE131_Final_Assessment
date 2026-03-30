import numpy as np

RANDOM_SEED = 42

SIM_TIME = 12 * 60  # minutes (8am–8pm)

MICROWAVES = {
    "QNC": 1,
    "CPH": 4,
    "DWE": 2,
    "E5": 1,
    "E6": 2,
    "E7": 3
}

ARRIVAL_RATE_BASE = 0.12  # students per minute
LUNCH_MULTIPLIER = 2.5

SERVICE_RATE = 1/2  # mean 2 minutes

QUEUE_LIMIT = 8