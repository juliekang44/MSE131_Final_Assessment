# Instructions

1. Install dependencies
pip install -r requirements.txt

2. Run scenario comparison
python microwave_model/experiments.py

3. Run sensitivity analysis
python src/sensitivity.py

Outputs
results/scenario_results.csv
results/sensitivity_results.csv
results/sensitivity_plot.png

Interpretation
Look for:
- highest utilization (bottleneck)
- longest waiting time
- effect of added microwave
- nonlinear growth of wait time