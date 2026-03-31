# UW Engineering Microwave Queue Simulation Report

## 1. System Selected
- Simulated microwave usage in UW Engineering buildings: QNC, CPH, DWE, E5, E6, E7
- Redirected demand: RCH → E7, E2 → CPH, E3 → CPH
- Focus: queue dynamics, waiting times, utilization, and bottlenecks

## 2. Baseline Model
- Flow: Students arrive → wait → use microwave → leave
- Servers: Microwaves per building
- Uncertainty: Poisson arrivals, exponential service times
- Performance measures: Average waiting time (Wq), system utilization (ρ), throughput, peak queue

## 3. Five Extensions
1. Rush-hour arrivals (11:30am–2pm)
2. Balking behavior if queue > QUEUE_LIMIT
3. Multi-building queues
4. Stochastic Monte Carlo simulation
5. Queue and utilization plots

## 4. Experimental Design
- Scenario comparison: Off-Peak, Peak, Full-Day
- Sensitivity analysis: ARRIVAL_RATE_BASE and SERVICE_RATE
- Outputs: TXT reports, queue plots, utilization bar charts

## 5. Results
- TXT reports with per-building metrics
- Queue vs time plots
- Utilization bar charts highlighting bottleneck

## 6. Interpretation
- Peak hours increase waiting times and queue lengths
- Buildings with fewer microwaves (QNC, E5) are bottlenecks
- Rush hour magnifies system congestion

## 7. Recommendation
- Add microwaves to bottleneck buildings during lunch
- Stagger lunch schedules to reduce peak demand

## 8. Limitation
- Poisson arrivals and exponential service times may not reflect real behavior
- Balking threshold is arbitrary
- Assumes independent building queues

## 9. AI Usage Statement
- AI tools (ChatGPT) were used as a tutor to brainstorm ideas, debug, and explain code
- All code, logic, and results were reviewed and modified by the student

## 10. AI Appendix
| Prompt | AI Output | Revision/Correction |
|--------|-----------|-------------------|
| "How would I begin a Python microwave queue simulation" | Initial simulation code | Adjusted for UW buildings, peak hours, balking |
| "Add queue and utilization plots" | Suggested plotting functions | Added timestamps, multiple buildings, color-coded bottlenecks |
| "Explain Poisson arrivals and exponential service" | Concept explanation | Reworded in report, added building parameters |
| "Make project A++ worthy" | Scenario comparison + stochastic runs | Implemented time window selection, TXT reports, plots |