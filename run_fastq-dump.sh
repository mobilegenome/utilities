#!/bin/bash
~/programs/sratoolkit.2.8.2-1-centos_linux64/bin/fastq-dump --clip --skip-technical --split-3 --split-spot --outdir $1 --gzip --split-files -defline-seq '@$sn[_$rn]/$ri' --defline-qual '+' -X 10000000 $2
