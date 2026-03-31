# AI Appendix - UW Engineering Microwave Queue Simulation

This appendix documents all major AI usage during the project. The AI (ChatGPT) was used **as a tutor, brainstorming assistant, and debugging guide**, not as a source of final answers. All code, logic, and analysis were **reviewed, verified, and modified by the student**.

---

## 1. Prompts Used, AI Outputs, and Student Revisions

| # | Prompt | AI Output Summary | Student Revision / Notes |
|---|--------|-----------------|-------------------------|
| 1 | "How would I begin a Python microwave queue simulation for multiple buildings with varying microwaves?" | Initial code skeleton: Poisson arrivals, exponential service, single server example | Converted to multi-building system; added building microwave counts per UW Engineering layout; incorporated redirected demand for buildings without microwaves |
| 2 | "Add lunch rush arrivals and peak hours" | Suggested multiplying arrival rate during specified times | Added 11:30am–2:00pm lunch rush using `LUNCH_MULTIPLIER`; implemented time window selection for Off-Peak, Peak, Full Day; stochastic arrivals verified with `np.random.exponential` |
| 3 | "Implement balking behavior if queue exceeds a certain length" | Example function to drop customers if queue > limit | Incorporated `QUEUE_LIMIT`; tracked number of students who balked per building; updated TXT report and plots to include balked counts |
| 4 | "Make a scenario comparison and sensitivity analysis framework" | Example of looping through parameters and generating results table | Built `experiments.py` for scenario comparison (Off-Peak, Peak, Full Day); built `sensitivity.py` for varying `ARRIVAL_RATE_BASE` and `SERVICE_RATE`; included TXT output and automatic figure saving with timestamps |
| 5 | "Add queue length vs time plotting and utilization bar charts" | Plotting functions using matplotlib | Added plotting for **all buildings**, hourly aggregation, color-coded bottlenecks; red bars indicate highest utilization; verified labels, legends, and readability |
| 6 | "Explain Poisson arrivals and exponential service times" | Concept explanation | Reworded in **report.md**; tied to course concepts: capacity, bottleneck, utilization, waiting time, single vs multiple lines |
| 7 | "Make project A++ worthy with extensions" | Suggested: rush-hour arrivals, balking, multiple servers, stochastic runs, plots | Implemented 6–7 strong extensions: rush hours, balking, two customer types (fast/slow, priority), random microwave breaks, congestion effect, multi-building queues, stochastic Monte Carlo runs; explained in report how each affects output |
| 8 | "How to randomize outputs for each run" | Introduced `numpy.random` with optional seeds | Removed fixed seed for stochastic Monte Carlo; each run produces different TXT reports and plots; optional reproducibility via `RANDOM_SEED` parameter |
| 9 | "Which metrics to include in microwave queue simulation" | Wq, W, Lq, L, throughput, utilization | Added **peak queue length**, **balked students**, **per-hour statistics**, **bottleneck identification**; included in reports and plots |
| 10 | "How to write a transparent AI usage statement and appendix" | Draft AI policy | Revised for project-specific use; clarified AI was a tutor; all code, results, and report reviewed and finalized by student |
| 11 | "Handle multiple time windows (Off-Peak, Peak, Full Day)" | Example logic using if/else | Implemented in `experiments.py`; adjusted arrival rates dynamically per window; queue and utilization plots respect time window |
| 12 | "Save results with timestamps in filename" | Example using `datetime.now()` | Integrated into `experiments.py` and `sensitivity.py`; ensures unique TXT and PNG outputs per run |
| 13 | "Incorporate priority customers and congestion effects" | Suggested modifying service time under queue conditions | Implemented priority service and slower service when queue > threshold; affects flow time and waiting time metrics; included in report interpretation |
| 14 | "Add random microwave breaks / downtime" | Example downtime code snippet | Added break probability per server; tracked active time vs total available; updated utilization calculation and bottleneck visualization |
| 15 | "Aggregate queue lengths per hour for plotting" | Suggested resampling or loop aggregation | Implemented hourly aggregation for queue plots; peak queue per hour highlighted; ensures readable x-axis for plots |

---

## 2. How AI Was Used

- **Brainstorming**: Model structure, extensions, stochastic simulation, time windows, and performance measures.  
- **Debugging**: Queue arrays, time stepping, server allocation, and handling of balking students.  
- **Plotting guidance**: Matplotlib techniques for hourly queue plots, color-coded bottlenecks, utilization charts.  
- **Scenario & sensitivity design**: Loops through arrival rates, service times, and time windows; TXT reports with timestamps.  
- **Concept clarification**: Poisson arrivals, exponential service times, stochastic Monte Carlo simulation, bottleneck identification, utilization metrics.  

---

## 3. Student Revision & Verification Process

- All AI suggestions were **rewritten and validated in Python**.  
- Additional features added **beyond AI output**:  
  - Balking count tracking per building  
  - Hourly queue aggregation for plots  
  - Random microwave breaks / downtime  
  - Priority customers (fast/slow types)  
  - Congestion slowing service when queue exceeds threshold  
  - Multi-building queues with redirected demand  
- Verified **stochastic outputs** through multiple test runs.  
- Ensured alignment with **course concepts**: capacity, bottleneck, utilization, waiting, single vs multiple lines, effect of demand intensity.  

---

## 4. AI Policy Compliance

- AI was used **transparently and responsibly**, strictly as a tutor.  
- Student **retains full responsibility** for all submitted work.  
- Major prompts, outputs, and revisions documented here.  
- No outputs were copied blindly; all were reviewed, modified, and adapted for UW building simulation requirements.  
- This satisfies course requirements for AI transparency.