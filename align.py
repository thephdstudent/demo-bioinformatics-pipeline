import subprocess

def align_reads(fastq, reference, output_bam):
    """
    Align reads to reference genome.
    """
    cmd = f"bwa mem {reference} {fastq} | samtools sort > {output_bam}"
    subprocess.run(cmd, shell=True)
