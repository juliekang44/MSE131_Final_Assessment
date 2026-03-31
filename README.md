# MSE131_Final_Assessment: UW Engineering Microwave Queue Simulation

This project simulates microwave usage across University of Waterloo Engineering buildings, tracking **queues, waiting times, utilization, and bottlenecks**.

---

## Buildings Included

- QNC: 1 microwave  
- CPH: 4 microwaves  
- DWE: 2 microwaves  
- E5: 1 microwave  
- E6: 2 microwaves  
- E7: 3 microwaves  

**Buildings without microwaves (redirected demand):**  
- RCH → E7  
- E2 → CPH  
- E3 → CPH  

---

## Model Features

- **Poisson arrivals** with stochastic timing  
- **Exponential service times** with variable heating durations  
- **Multiple servers** (microwaves) per building  
- **Lunch rush spike** (11:30am–2pm)  
- **Balking behavior**: students leave if queue exceeds limit  
- **Stochastic Monte Carlo runs** for variability  
- **Queue and utilization plotting** (visualization of bottlenecks)  
- **Scenario comparisons**: Off-Peak, Peak Hours, Full Day  
- **Sensitivity analysis**: change arrival and service rates  

---

## Extensions Added

1. Rush-hour arrivals (11:30am–2pm)  
2. Balking if queue exceeds `QUEUE_LIMIT`  
3. Multi-building queue system  
4. Stochastic simulation for variability  
5. Queue and utilization plotting with color-coded bottlenecks  

---

## Performance Measures

- **Wq**: Average waiting time  
- **W**: Average flow time (waiting + service)  
- **Utilization (ρ)**: Fraction of time microwaves are busy  
- **Throughput**: Customers served per minute  
- **Peak queue length**  
- **Number of students who balked**  
