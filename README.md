# Network Anomaly Detection

A Python script that finds two kinds of problems in network monitoring data: sudden latency spikes and service outages.

## How it works

**Part A: latency spikes (statistical)**
- Calculates the mean and standard deviation of latency readings
- Converts each reading to a Z-score and flags anything beyond 3 standard deviations

**Part B: outages (rule-based)**
- Marks a reading as "down" when throughput falls below 5 Mbps
- Finds where each run of consecutive "down" readings starts and ends
- Reports runs of 2 or more readings as outages (with their length in minutes) and single readings as brief blips

## Example results (sample data)
- 🚩 09:40: 180 ms latency (Z-score 4.79)
- 🚨 Outage from 08:25 lasting 15 minutes
- ⚠️ Brief blip at 09:00

## How to run
```bash
python network_anomalies.py
```

## What I learned
- Using vectorized NumPy math to calculate Z-scores for every reading at once
- Using `np.where()` to get the positions of readings that meet a condition
- Finding where runs begin and end: pad the True/False array with zeros, use `np.diff()`, and look for +1 (start) and -1 (end)
- Why padding matters: it makes outages at the very start or end of the data detectable
- Combining two different detection methods in one monitoring script
- Converting a reading's index into a clock time with a helper function

## Limitations
- A large spike inflates the standard deviation it is measured against, so multiple spikes can hide each other.
- All data is fictional sample data, with readings every 5 minutes starting at 08:00.

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
