import numpy as np

# Optional random seed (comment out for stochastic Monte Carlo runs)
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Simulation time in minutes (8am–8pm)
SIM_TIME = 12 * 60  # 720 minutes

# Microwave servers per building
MICROWAVES = {
    "QNC": 1,
    "CPH": 4,
    "DWE": 2,
    "E5": 1,
    "E6": 2,
    "E7": 3
}

# Redirected demand for buildings without microwaves
REDIRECTED = {
    "RCH": "E7",
    "E2": "CPH",
    "E3": "CPH"
}

# Base arrival rate (students/min)
ARRIVAL_RATE_BASE = 0.12

# Rush-hour multiplier (11:30am–2pm)
LUNCH_MULTIPLIER = 2.5

# Service rate: mean service time = 2 min → lambda = 1/2
SERVICE_RATE = 1/2  # per minute

# Maximum queue length before balking
QUEUE_LIMIT = 8

# Customer types: Normal (90%) or Large Order (10%), large orders take 1.5x service time
CUSTOMER_TYPE_PROBS = [0.9, 0.1]
CUSTOMER_SERVICE_MULT = [1.0, 1.5]