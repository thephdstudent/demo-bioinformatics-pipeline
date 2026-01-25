from qc import run_qc
from align import align_reads
from quantify import quantify_genes

def run():
    fastq = "sample.fastq"
    reference = "ref.fa"
    annotation = "genes.gtf"

    bam = "aligned.bam"

    align_reads(fastq, reference, bam)
    counts = quantify_genes(bam, annotation)

    qc_metrics = run_qc("counts.tsv")
    print(qc_metrics)

if __name__ == "__main__":
    run()
