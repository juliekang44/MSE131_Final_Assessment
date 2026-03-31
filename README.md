# MSE131_Final_Assessment: Waterloo Engineering Building Microwave Queue Simulation

This project models microwave waiting lines across University of Waterloo engineering buildings.

Buildings Included
- QNC (1 microwave)
- CPH (4 microwaves)
- DWE (2 microwaves)
- E5 (1 microwave)
- E6 (2 microwaves)
- E7 (3 microwaves)

Buildings Without Microwaves (redirected demand)
- RCH → E7
- E2 → CPH
- E3 → CPH

Model Features
- Exponential arrival times
- Exponential service times
- Multiple servers (microwaves)
- Lunch rush demand spike
- Student leaving if the queue is long
- Variable heating times
- Sensitivity analysis

Assumptions
- Poisson arrivals
- Exponential service times
- FCFS discipline
- Lunch demand spike
- Students may balk when queue too long

Performance Measures
Wq: average waiting time
W: average flow time
Lq: average queue length
L: average number in system
ρ: utilization
Throughput: customers served


Run experiments:
python microwave_model/experiments.py

