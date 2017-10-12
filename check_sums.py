import subprocess as sub
import glob,os

fastq_files=glob.glob(os.path.join("Downloads_Fastq", "*.fastq.gz"))

for fq in fastq_files:
    proc = sub.Popen(["md5sum", fq], stdout=sub.PIPE, stderr=sub.STDOUT, shell=False)
    (out, err) = proc.communicate()
    if not err:
        with open("Checksum_Results.txt", "a") as f:
            f.write(out)