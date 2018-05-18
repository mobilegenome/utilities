#!/bin/bash
#
# Wrapper for fastq-dump (SRA toolkit needs to be installed, path to be adjusted below)
# takes two positional arguments: 1. output directory ($1) 2. Accession number (SRR...) ($2)
~/programs/sratoolkit.2.8.2-1-centos_linux64/bin/fastq-dump --clip --skip-technical --split-3 --split-spot --outdir $1 --gzip --split-files -defline-seq '@$sn[_$rn]/$ri' --defline-qual '+'  $2
