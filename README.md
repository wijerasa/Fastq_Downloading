# Fastq Downloading

## What this does:

Python scripts given here will download 'fastq' files from remote server to "Downloads_Fastq" folder in your local server.
Then calculate "md5sum" for each "fastq" file in the "Downloads_Fastq" folder and report the output.

## Scripts

1. download_fastq.py - Download "fastq" files, multiprocessing implemented.
2. check_sums.py - Run "md5sum" on all the files stored in 'Downloads_Fastq" folder

## Inputs
3. fastq_urls.txt - Each line represent unique URL to a "fastq" file.

## Outputs
4. Downloads_Fastq - Folder contains downloaded "fastq" files
5. Checksum_Results.txt - Results from "md5sum"

## How to run

### Step 1:

Clone the git repository to your local server

```bash
git clone https://github.com/wijerasa/Fastq_Downloading.git
cd Fastq_Downloading

```

### Step 2:

Edit "fastq_urls.txt" for the URLs for your "fastq" files.

Ex:
```

http://test.org/v1/AUTH_huda/JDEkc1ZwdTZmaHM/CBTAUANXX_s3_1_illumina12index_9_SL267844.fastq.gz
http://test.org/v1/AUTH_huda/JDEkc1ZwdTZmaHM/CBTAUANXX_s3_2_illumina12index_9_SL267844.fastq.gz
http://test.org/v1/AUTH_huda/JDEkc1ZwdTZmaHM/CBTAUANXX_s3_2_illumina12index_1_SL267821.fastq.gz
http://test.org/v1/AUTH_huda/JDEkc1ZwdTZmaHM/CBTAUANXX_s3_1_illumina12index_1_SL267821.fastq.gz

```

### Step 3:

Execute,

```bash
python download_fastq.py
```

This will create the "Downloads_Fastq" folder

### Step 4:

```bash
python check_sums.py
```

This will create "Checksum_Results.txt" file
