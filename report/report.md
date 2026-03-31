# UW Engineering Microwave Queue Simulation Report

## 1. System Selected
- Simulated microwave usage in UW Engineering buildings: QNC, CPH, DWE, E5, E6, E7  
- Redirected demand: RCH → E7, E2 → CPH, E3 → CPH  
- Focus: queue dynamics, waiting times, utilization, and bottlenecks

---

## 2. Baseline Model
- Flow: Students arrive → wait → use microwave → leave  
- Servers: Microwaves per building  
- Uncertainty: Poisson arrivals, exponential service times  
- Performance measures: Average waiting time (Wq), system utilization (ρ), throughput, peak queue

---

## 3. Extensions (6–7)
1. Rush-hour arrivals (11:30am–2pm)  
2. Balking if queue > `QUEUE_LIMIT`  
3. Multi-building queues with redirected demand  
4. Two customer types: fast and slow, priority customers  
5. Random microwave breaks (downtime)  
6. Congestion slows service when queues are long  
7. Stochastic Monte Carlo simulation for variability  

---

## 4. Experimental Design
- Scenario comparison: Off-Peak, Peak, Full-Day  
- Sensitivity analysis: ARRIVAL_RATE_BASE and SERVICE_RATE  
- Outputs: TXT reports, hourly queue plots, utilization bar charts

---

## 5. Results
- TXT reports with per-building metrics  
- Hourly queue plots  
- Utilization bar charts highlighting bottleneck

---

## 6. Interpretation
- Peak hours increase waiting times and queue lengths  
- Buildings with fewer microwaves (QNC, E5) are bottlenecks  
- Priority and congestion rules influence flow time and queue lengths

---

## 7. Recommendation
- Add microwaves to bottleneck buildings during lunch  
- Stagger lunch schedules to reduce peak demand  
- Consider priority access for fast/short tasks in critical buildings

---

## 8. Limitation
- Poisson arrivals and exponential service times may not reflect real behavior  
- Balking threshold is arbitrary  
- Assumes independent building queues, no inter-building congestion

---

## 9. AI Usage Statement
- AI tools (ChatGPT) were used as a **tutor** to brainstorm ideas, debug, and explain code  
- All code, logic, and results were reviewed and modified by the student  
- AI was **not used to generate final outputs or reports**; student verified all correctness

---

## 10. AI Appendix
| Prompt | AI Output | Revision/Correction |
|--------|-----------|-------------------|
| "Python microwave queue simulation starter code" | Initial simulation functions | Adjusted for UW buildings, multiple servers, stochastic arrivals |
| "Add priority customer and two types" | Example code snippet | Integrated into service time function and queue handling |
| "Plot queue and utilization per hour" | Matplotlib plotting code | Modified for hourly aggregation, color-coded bottleneck |
| "Add extensions: breaks, congestion, balking" | Suggested code structure | Implemented all extensions with parameterized probabilities |
| "Make scenario comparison and sensitivity analysis" | Example loops | Rewrote `experiments.py` and `sensitivity.py` for full automation |
| "Explain Poisson arrivals and exponential service" | Concept notes | Reworded for report and linked to performance measures |
| "Make project A++ worthy" | Idea list | Added multi-building queues, stochastic simulation, detailed reporting |
| "AI usage policy statement" | Draft policy | Refined to indicate tutoring, verification, and responsible use |