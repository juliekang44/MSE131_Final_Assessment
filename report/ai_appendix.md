# AI Appendix - UW Engineering Microwave Queue Simulation

This appendix documents all major AI usage during the project. The AI (ChatGPT) was used as a tutor, brainstorming assistant, and debugging guide, not as a source of final answers. All code, logic, and analysis were reviewed, verified, and modified.

---

## 1. Prompts Used, AI Outputs, and Student Revisions

| # | Prompt | AI Output Summary | Student Revision / Notes |
|---|--------|-----------------|-------------------------|
| 1 | "How would I begin a Python microwave queue simulation for multiple buildings with varying microwaves?" | Initial code skeleton: Poisson arrivals, exponential service, single server example | Made a system that reflects the microwaves in the UW Engineering buildings, also redirecting the demand from buildings with no microwaves to closest buildings |
| 2 | "Add lunch rush arrivals and peak hours" | Suggested multiplying arrival rate during specified times | Accounted for lunch time demand from 11:30am–2:00pm using LUNCH_MULTIPLIER. User can choose a window of time and stochastic arrivals are verified with np.random.exponential |
| 3 | "Implement balking behavior if queue exceeds a certain length" | Example function to drop customers if queue > limit | created QUEUE_LIMIT which tracks the number of students who balked per building. The .txt report and .png plots include balked counts |
| 4 | "Make a scenario comparison and sensitivity analysis framework" | Example of looping through parameters and generating results table | experiments.py has three scenarios: Off-Peak, Peak, Full Day. sensitivity.py shows varying ARRIVAL_RATE_BASE and SERVICE_RATE. All the results are included in the output and automatic figure saving with timestamps |
| 5 | "Add queue length vs time plotting and utilization bar charts" | Plotting functions using matplotlib | Added plotting for all buildings, hourly aggregation, color-coded bottlenecks; red bars indicate highest utilization; verified labels, legends, and readability |
| 6 | "Explain Poisson arrivals and exponential service times" | Concept explanation | Reworded concept in report.md to tie course concepts together, such as capacity, bottleneck, utilization, waiting time, single vs multiple lines |
| 7 | "Make project A++ worthy with extensions" | Suggested: rush-hour arrivals, balking, multiple servers, stochastic runs, plots | Used ideas to create strong extensions: rush hours, balking, two customer types (fast/slow, priority), random microwave breaks, congestion effect, multi-building queues, stochastic Monte Carlo runs |
| 8 | "How to randomize outputs for each run" | Introduced numpy.random with optional seeds | Removed fixed seed for stochastic Monte Carlo so that each run produces different reports and plots depending on user's choice |
| 9 | "Which metrics to include in microwave queue simulation" | Wq, W, Lq, L, throughput, utilization | Added peak queue length, balked students, per-hour statistics, bottleneck identification; included in reports and plots |
| 10 | "How to write a transparent AI usage statement and appendix" | Draft AI policy | Helped revise and clarify that AI was a tutor and created a detailed ai report to reflect that all code, results, and report reviewed and finalized |
| 11 | "Handle multiple time windows (Off-Peak, Peak, Full Day)" | Example logic using if/else | adjusted arrival rates dynamically per window and queue and utilization plots respect time window for experiments.py |
| 12 | "Save results with timestamps in filename" | Example using datetime.now() | Integrated into experiments.py and sensitivity.py for unique outputs per run |
| 13 | "Incorporate priority customers and congestion effects" | Suggested modifying service time under queue conditions | Priority service and slower service when queue > threshold, this affects flow time and waiting time metrics |
| 14 | "Add random microwave breaks / downtime" | Example downtime code snippet | Added break probability per server and tracked active time vs total available. This is updated in the utilization and bottleneck calculation |
| 15 | "Aggregate queue lengths per hour for plotting" | Suggested resampling or loop aggregation | Hourly aggregation for queue plots where peak queue per hour highlighted. This helps the graph to be more readable |

---

## 2. How AI Was Used

- **Brainstorming**: Model structure, extensions, stochastic simulation, time windows, and performance measures.  
- **Debugging**: Queue arrays, time stepping, server allocation, and handling of balking students.  
- **Plotting guidance**: Matplotlib techniques for hourly queue plots, color-coded bottlenecks, and utilization charts.  
- **Scenario & sensitivity design**: Loops through arrival rates, service times, and time windows; TXT reports with timestamps.  
- **Concept clarification**: Poisson arrivals, exponential service times, stochastic Monte Carlo simulation, bottleneck identification, and utilization metrics.  

---

## 3. Student Revision & Verification Process

- All AI suggestions were **rewritten and validated in Python**.  
- Additional features added **beyond AI output**:  
  - Balking count tracking per building  
  - Hourly queue aggregation for plots  
  - Random microwave breaks / downtime  
  - Priority customers (fast/slow types)  
  - Congestion slows service when the queue exceeds the threshold  
  - Multi-building queues with redirected demand  
- Verified stochastic outputs through multiple test runs.  
- Ensured alignment with course concepts: capacity, bottleneck, utilization, waiting, single vs multiple lines, and the effect of demand intensity.  

---

## 4. AI Policy Compliance

- AI was used transparently and responsibly, strictly as a tutor.  
- I retain full responsibility for all submitted work.  
- Major prompts, outputs, and revisions are documented here.  
- No outputs were copied blindly; all were reviewed, modified, and adapted for UW building simulation requirements.  
- This satisfies course requirements for AI transparency.