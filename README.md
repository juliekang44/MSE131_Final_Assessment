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
- **Randomized stochastic runs** for different results each run  
- **Queue and utilization plotting** (visualization of bottlenecks)  
- **Scenario comparisons**: Off-Peak, Peak Hours, Full Day  
- **Sensitivity analysis** (change arrival rates and service rates)  

---

## **Assumptions**

- First-Come-First-Served (FCFS) discipline  
- Poisson arrivals and exponential service times approximate student behavior  
- Independent queues per building  
- Balking occurs at configurable queue threshold (`QUEUE_LIMIT`)  

---

## **Performance Measures**

- **Wq**: Average waiting time (minutes)  
- **W**: Average flow time (waiting + service)  
- **Utilization (ρ)**: Fraction of time microwaves are busy  
- **Throughput**: Customers served per minute  
- **Peak queue length**  
- **Number of students who balked**  

---

## **Extensions Added**

1. Rush-hour arrivals (11:30am–2pm)  
2. Balking if queue exceeds `QUEUE_LIMIT`  
3. Multi-building queue system  
4. Stochastic Monte Carlo simulations  
5. Queue and utilization plotting with color-coded bottlenecks  

---

## **Installation**

Install required packages:

```bash
pip install -r requirements.txt