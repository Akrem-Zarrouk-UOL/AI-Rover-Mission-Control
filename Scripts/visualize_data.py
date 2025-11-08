import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Resolve the expected CSV path relative to project root (parent of Scripts)
project_root = Path(__file__).resolve().parent.parent
candidates = [project_root / "Data" / "rover_data.csv", project_root / "data" / "rover_data.csv"]

csv_path = None
for p in candidates:
	if p.exists():
		csv_path = p
		break

if csv_path is None:
	print("ERROR: Could not find 'rover_data.csv'. Checked these locations:")
	for p in candidates:
		print(f" - {p}")
	print("Run Scripts/simulate_rover_data.py to create the file, or pass a different path.")
	sys.exit(1)

df = pd.read_csv(csv_path)
print(f"Loaded data from {csv_path}")

# Simple visualization of temperature and battery over time
plt.figure(figsize=(10, 5))
plt.plot(df["time"], df["temperature"], label="Temperature (°C)")
plt.plot(df["time"], df["battery"], label="Battery (%)")
plt.xlabel("Time")
plt.ylabel("Sensor readings")
plt.title("Rover Sensor Data Over Time")
plt.legend()
plt.tight_layout()
plt.show()
