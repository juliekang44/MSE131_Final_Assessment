# AI Appendix - UW Engineering Microwave Queue Simulation

This appendix documents all major AI usage during the project. The AI (ChatGPT) was used **as a tutor and brainstorming assistant**, not as a source of final answers. All code, logic, and analysis were **reviewed, verified, and modified by the student**.

---

## 1. Prompts Used, AI Outputs, and Revisions

| # | Prompt | AI Output Summary | Student Revision / Notes |
|---|--------|-----------------|-------------------------|
| 1 | "How would I begin a Python microwave queue simulation for multiple buildings with varying microwaves?" | Initial code skeleton: Poisson arrivals, exponential service, single server example | Converted to multi-building system; added building microwave counts per UW Engineering layout; incorporated redirected demand for buildings without microwaves |
| 2 | "Add lunch rush arrivals and peak hours" | Suggested multiplying arrival rate during specified times | Added 11:30am–2:00pm lunch rush, using `LUNCH_MULTIPLIER`; verified that Poisson process generates stochastic arrivals; implemented time window selection for Off-Peak, Peak, Full Day |
| 3 | "Implement balking behavior if queue exceeds a certain length" | Example function to drop customers if queue > limit | Incorporated `QUEUE_LIMIT`; tracked number of students who balked per building; updated performance measures and reports to include balking statistics |
| 4 | "Make a scenario comparison and sensitivity analysis framework" | Example of looping through parameters and generating results table | Built `experiments.py` for scenario comparison (Off-Peak, Peak, Full Day); built `sensitivity.py` for varying `ARRIVAL_RATE_BASE` and `SERVICE_RATE`; added TXT report output with timestamps |
| 5 | "Add queue length vs time plotting and utilization bar charts" | Plotting functions using matplotlib | Added plotting for **all buildings**, including color-coded bottlenecks (red bars for highest utilization); saved figures in `results/` folder with unique timestamps; verified labels, legends, and readability |
| 6 | "Explain Poisson arrivals and exponential service times in simple terms" | Text explanation of stochastic processes | Reworded in **report.md**; tied to course concepts: capacity, bottleneck, utilization, waiting time |
| 7 | "How to make the project A++ worthy with five extensions" | Suggested: rush-hour arrivals, balking, multiple servers, stochastic runs, plots | Implemented all five: (1) peak arrivals, (2) balking, (3) multi-building queues, (4) stochastic Monte Carlo, (5) queue and utilization plots; explained impact of each extension in report |
| 8 | "How to randomize outputs each run and include stochastic results" | Introduced random seeds or `numpy.random` | Implemented `np.random.seed()` optional for reproducibility; removed fixed seed for stochastic Monte Carlo runs to ensure different results each run |
| 9 | "What metrics should be included in a microwave queue simulation" | Wq, W, Lq, L, throughput, utilization | Added **peak queue**, **balked students**, **bottleneck identification**; included in TXT outputs and plots |
| 10 | "How to write a transparent AI usage statement and appendix" | Example AI policy | Modified for project-specific language; clarified that AI was **only a tutor**, all final decisions and code revisions done by student; included major prompts and revisions in table |
| 11 | "How to handle multiple time windows (Off-Peak, Peak, Full Day)" | Example logic using if/else | Implemented in `experiments.py`; adjusted arrival rate dynamically per selected window; queue plots also respect time window |
| 12 | "How to save results with timestamps in filename" | Example using `datetime.now()` | Integrated into `experiments.py` and `sensitivity.py`; ensures each run generates unique TXT and PNG files |

---

## 2. How AI Was Used

- **Brainstorming model structure**: AI helped outline the simulation logic (arrival, queue, service, flow).  
- **Debugging**: AI suggested code corrections when queue arrays or time steps caused errors.  
- **Plotting guidance**: AI suggested matplotlib techniques for queue length vs time and utilization bar charts.  
- **Scenario and sensitivity analysis design**: AI proposed how to systematically vary parameters and output results.  
- **Concept explanation**: AI clarified Poisson and exponential distributions, stochastic simulation, and queueing theory measures.  

---

## 3. Student Revision and Verification Process

- All AI-generated code snippets were **rewritten and tested** in Python to meet UW building specifications.  
- Added extra features not in AI outputs:  
  - Balking count tracking  
  - Red color-coded bottleneck in plots  
  - Multiple time windows with stochastic Monte Carlo runs  
  - TXT outputs with detailed statistics for each building  
- Verified **results accuracy** using small test runs.  
- Ensured **alignment with course concepts**: capacity, bottleneck, utilization, waiting, single vs multiple lines, effect of demand intensity.  

---

## 4. AI Policy Compliance

- AI was used **transparently and responsibly**, only as a tutor.  
- The student **remains fully responsible** for all submitted work.  
- Major prompts, outputs, and revisions are documented here.  
- No AI-generated outputs were copied blindly; all were reviewed, modified, and adapted.  
- This documentation satisfies the course requirement for AI transparency.