import pandas as pd
import numpy as np
from pathlib import Path

# Simulate rover sensor data
def generate_data(n=100):
    np.random.seed(42)
    data = {
        "time": range(n),
        "temperature": np.random.uniform(-20, 40, n),   # °C
        "battery": np.random.uniform(20, 100, n),       # %
        "distance": np.random.uniform(0, 500, n),       # meters
        "speed": np.random.uniform(0, 10, n)            # m/s
    }
    df = pd.DataFrame(data)

    # Resolve output directory relative to the project root (parent of Scripts)
    project_root = Path(__file__).resolve().parent.parent
    out_dir = project_root / "Data"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "rover_data.csv"

    df.to_csv(out_file, index=False)
    print(f"✅ Simulated rover data saved in {out_file}")


if __name__ == "__main__":
    generate_data()
