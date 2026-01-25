import pandas as pd

def run_qc(counts_file):
    """
    Perform basic QC on a gene counts table.
    """
    df = pd.read_csv(counts_file, sep="\t")

    total_counts = df["counts"].sum()
    detected_genes = (df["counts"] > 0).sum()

    return {
        "total_counts": total_counts,
        "detected_genes": detected_genes
    }
