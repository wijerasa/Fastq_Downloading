from multiprocessing import Pool
import subprocess as sub
import os,shutil


def run(url):
    proc = sub.Popen(['wget', url, '-P', 'Downloads_Fastq'], stdout=sub.PIPE, stderr=sub.STDOUT, shell=False)
    (out, err) = proc.communicate()
    if not err:
        print 'Sample {0} download is complete'.format(url)
    else:
        print err

if __name__ == '__main__':
    if os.path.isdir("Downloads_Fastq"):
        shutil.rmtree("Downloads_Fastq")
        os.mkdir("Downloads_Fastq")
    else:
        os.mkdir("Downloads_Fastq")

    with open("fastq_urls.txt", "r") as f:
        url_list = f.read().splitlines()
    p=Pool(28)
    p.map(run, url_list)
