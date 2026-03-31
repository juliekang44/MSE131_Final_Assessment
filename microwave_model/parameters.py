# parameters.py
# Simulation parameters for UW Engineering Microwave Queue Simulation

import numpy as np

# Random seed for reproducibility (None = true randomness per run)
RANDOM_SEED = None

# Total simulation time in minutes (12 hours: 8am–8pm)
SIM_TIME = 12 * 60

# Microwaves per building
MICROWAVES = {
    "QNC": 1,
    "CPH": 4,
    "DWE": 2,
    "E5": 1,
    "E6": 2,
    "E7": 3
}

# Base arrival rate of students (students per minute)
ARRIVAL_RATE_BASE = 0.12

# Lunch rush multiplier (increases arrivals during 11:30am-2pm)
LUNCH_MULTIPLIER = 2.5

# Service rate: 1/mean service time (mean = 2 minutes)
SERVICE_RATE = 1/2

# Maximum queue length before students leave (balking threshold)
QUEUE_LIMIT = 8