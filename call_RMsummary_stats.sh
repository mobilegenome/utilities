#!/bin/bash

# reads 
cat $1 |\
awk ' function basename(file) 
	{ 
	sub(".*/", "", file); 
	return file 
	} 
	{ 
	fname=basename($4);
	gsub(".fastq.gz",".fasta.out.summary",fname);
	gsub(".fq.gz",".fa.out.summary",fname);
	print $1, $2"_"$3, $1"/"$2"_"$3"/"fname
}'
