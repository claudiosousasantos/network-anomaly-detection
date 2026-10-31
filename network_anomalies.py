import numpy as np

# One reading every 5 minutes, starting at 08:00 (24 readings = 2 hours)
latency_ms = np.array([
    38, 40, 42, 39, 41, 37, 40, 43, 39, 41,
    38, 40, 42, 39, 41, 40, 38, 42, 40, 39,
    180, 41, 40, 39
])

throughput_mbps = np.array([
    102, 98, 105, 99, 101, 0, 0, 0, 97, 103,
    100, 99, 0, 104, 101, 98, 100, 102, 99, 101,
    103, 98, 100, 99
])

def index_to_time(i):
    minutes = i * 5
    hour = 8 + minutes // 60
    minute = minutes % 60
    return f"{hour:02d}:{minute:02d}"

mean_latency = np.mean(latency_ms)
std_latency = np.std(latency_ms)

z_scores = (latency_ms - mean_latency) / std_latency

threshold = 3
is_anomaly = np.abs(z_scores) > threshold

anomaly_positions = np.where(is_anomaly)[0]

for i in anomaly_positions:
    print(f"🚩 Latency spike at {index_to_time(i)}: {latency_ms[i]} ms (Z-score {z_scores[i]:.2f})")