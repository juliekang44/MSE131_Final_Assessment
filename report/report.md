## UW Engineering Microwave Queue Simulation Report

# 1. System Selected

- The simulation examines how microwaves are used in UW engineering buildings, including QNC, CPH, DWE, E5, E6, and E7.
- For buildings with no microwaves, students are redirected from RCH to E7, while students from E2 and E3 go to CPH.
- The main goal is to study queue dynamics, wait times, system usage, and to identify bottlenecks.

---

# 2. Baseline Model

- The process is as follows: students arrive, wait, and then use the microwave.  
- Arrivals are modeled using a Poisson process, and service times are modeled as exponential.
- Performance is measured by the average wait time in the queue (Wq), system utilization (ρ), throughput, and the maximum queue length.

---

# 3. Extensions

1. Rush hour is from 11:30 am to 2 pm, when most students have lunch, so the arrival rate is the highest.
2. Students are expected to leave the queue if it is too long (QUEUE_LIMIT).
3. The simulation also includes queues that link different buildings.
4. There are two types of customers: fast and slow, with priority given to fast users.
5. Microwaves occasionally break down or experience random downtime.
6. In the model, service times slow down as queues grow.
7. A Monte Carlo simulation is used to show possible variations in the system.
8. Plots are created to show queue patterns and system usage.

---

# 4. Experimental Design

- The simulation compares different time periods, including off-peak, peak, and the entire day.
- A sensitivity analysis is performed on the basic arrival and service rates.
- The results included a TXT report, hourly queue plots, and bar charts showing microwave usage.

---

# 5. Results

- TXT reports summarize the main statistics for each building. Hourly plots show how queues change during the day.
- Bar charts display utilization and highlight bottlenecks.

---
# 6. Interpretation

- Wait times and queue lengths increase during peak hours.
- Buildings with fewer microwaves, like E5 and QNC, have the most bottlenecks.
- Priority rules and crowding affect both flow times and queue lengths.

---

# 7. Recommendation

- Add more microwaves to busy buildings during lunchtime.
- Staggering lunch schedules can help reduce peak demand.
- Giving priority to quick users in key buildings may improve efficiency.

---

# 8. Limitation

- Using Poisson arrivals and exponential service times might not fully reflect real-life conditions.
- The balking threshold is selected without a specific rationale.
- The model assumes each building has its own queue and does not account for congestion between buildings.

---

# 9. AI Usage Statement

- AI tools such as ChatGPT were used as a tutor for brainstorming, debugging, and explaining code. The student reviewed and revised all code, logic, and results.
- AI was not used to produce any final outputs or reports. The student ensured all results were correct.

---

# 10. AI Appendix
- Please check ai_appendix.md