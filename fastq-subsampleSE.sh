#!/bin/bash
mkdir -p $1
cd $1

in1=$2
fname1=$(basename $in1)
out1=$(echo $fname1 |  sed 's/\.f.*q\.gz/\.subsample.fq.gz/g')
zcat $in1 | head -40000000 | gzip > $out1

cd ..
