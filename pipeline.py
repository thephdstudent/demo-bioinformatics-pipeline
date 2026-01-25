import sys
import pandas as pd

def load_counts(file_path):
    return pd.read_csv(file_path, sep="\t")

def normalize_counts(df):
    if "counts" not in df.columns:
        raise ValueError("Missing 'counts' column")
    df["normalized"] = df["counts"] / df["counts"].sum()
    return df

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    counts = load_counts(input_file)
    normalized = normalize_counts(counts)

    normalized.to_csv(output_file, sep="\t", index=False)
# TODO: add better CLI argument parsing
