"""Fetch UCI dataset 551 and save annual CSV files for the original notebook."""
from pathlib import Path
from ucimlrepo import fetch_ucirepo

root = Path(__file__).resolve().parents[1]
output = root / "dataset"
output.mkdir(parents=True, exist_ok=True)

dataset = fetch_ucirepo(id=551)
frame = dataset.data.original
if frame is None:
    raise RuntimeError("UCI did not return the full data table.")
if "year" not in frame.columns:
    raise RuntimeError("Dataset must include a year column to recover annual CSVs.")
for year, group in frame.groupby("year"):
    if int(year) not in range(2011, 2016):
        continue
    path = output / f"gt_{int(year)}.csv"
    group.drop(columns="year").to_csv(path, index=False)
    print(f"Saved {len(group):,} observations to {path}")
