from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA = BASE_DIR / 'data' / 'iris.csv'


def output_data(data, species):
    sorted_data = data.sort_values(by='Sepal.Length', ascending=False)
    filename = f"{species.lower().replace(' ', '_')}.csv"
    output_path = BASE_DIR / 'data' / '2-1' / filename
    sorted_data.to_csv(output_path, index=False)


def analyze_species(data):
    numeric_cols = data.select_dtypes(include='number').columns
    if numeric_cols.empty:
        return pd.DataFrame()

    stats = data[numeric_cols].agg(['sum', 'mean', 'std', 'var', 'max', 'min'])
    return stats


df = pd.read_csv(DATA)

if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

for species, group in df.groupby('Species'):
    unique_group = group.drop_duplicates()
    res = analyze_species(unique_group)
    print(species)
    print(res)
    output_data(unique_group, species)
    print()
