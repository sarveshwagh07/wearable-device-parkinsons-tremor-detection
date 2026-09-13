import numpy as np
import pandas as pd
from pathlib import Path

RNG = np.random.default_rng(42)
FS = 100
DURATION = 5
N = FS * DURATION

def make_signal(tremor=False):
    t = np.arange(N) / FS
    signal = 0.25 * np.sin(2*np.pi*1.2*t) + 0.08 * RNG.normal(size=N)
    if tremor:
        freq = RNG.uniform(4.0, 6.0)
        signal += 0.45 * np.sin(2*np.pi*freq*t)
    return signal

rows = []
for label in [0, 1]:
    for sample_id in range(150):
        s = make_signal(tremor=bool(label))
        for i, value in enumerate(s):
            rows.append((sample_id, i / FS, value, label))

out = Path("data")
out.mkdir(exist_ok=True)
pd.DataFrame(rows, columns=["sample_id", "time_s", "accel_x", "label"]).to_csv(
    out / "synthetic_accelerometer.csv", index=False
)
print("Saved synthetic_accelerometer.csv")
