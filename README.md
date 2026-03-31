# MSE131_Final_Assessment: UW Engineering Microwave Queue Simulation

This project simulates microwave usage across University of Waterloo Engineering buildings, tracking **queues, waiting times, utilization, and bottlenecks**.

---

## **Buildings Included**

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

## **Model Features**

- **Poisson arrivals** with stochastic timing  
- **Exponential service times** with variable heating durations  
- **Multiple servers** (microwaves) per building  
- **Lunch rush spike** (11:30am–2pm)  
- **Balking behavior**: students leave if queue exceeds limit  
- **Multiple customer types**: fast and slow users, priority customers  
- **Random microwave breaks** to simulate downtime  
- **Congestion effect**: slower service when queue is long  
- **Stochastic Monte Carlo runs** for variability  
- **Queue and utilization plotting** (color-coded bottlenecks)  
- **Scenario comparisons**: Off-Peak, Peak Hours, Full Day  
- **Sensitivity analysis** (change arrival rates and service times)  

---

## **Extensions Added**

1. Rush-hour arrivals (11:30am–2pm)  
2. Balking if queue exceeds `QUEUE_LIMIT`  
3. Multi-building queue system  
4. Two customer types: fast/slow + priority  
5. Random microwave breaks (downtime)  
6. Congestion slows service when queues are high  
7. Stochastic Monte Carlo simulation for variability  
8. Queue and utilization plotting  

---

## **Performance Measures**

- **Wq**: Average waiting time  
- **W**: Average flow time (waiting + service)  
- **Utilization (ρ)**: Fraction of time microwaves are busy  
- **Throughput**: Customers served per hour  
- **Peak queue length**  
- **Number of students who balked**  

---

## **Outputs**

- TXT reports per scenario  
- Queue vs hour plots (`PNG`)  
- Utilization bar charts highlighting bottlenecks