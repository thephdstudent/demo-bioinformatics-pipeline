import pandas as pd

def quantify_genes(bam_file, annotation_gtf):
    """
    Quantify genes from BAM file.
    """
    # Placeholder for featureCounts output
    df = pd.DataFrame({
        "gene": ["GeneA", "GeneB", "GeneC"],
        "counts": [100, 50, 0]
    })
    return df
