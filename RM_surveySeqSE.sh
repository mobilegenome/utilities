#!/bin/bash

# subsamples FastQ dataset to FastA and runs RepeatMasker
# set $PROJECT_DIR or direct to library file
# set number of reads below (as *2)
# TODO: quality filter

tax=$1
id=$2
acc=$3
path=$4
lib="$PROJECT_DIR/data/libraries/LATEST/custom_lib.cetartiodactyla.fa"
fqname=$(basename $path)
faname=${fqname/"q.gz"/"a"}


mkdir -p "$tax"
cd $tax
mkdir -p "${id}_${acc}"
cd "${id}_${acc}"
zcat $4 |sed -n '1~4s/^@/>/p;2~4p' | head -n 2000000 | awk '/^>/{print ">" ++i; next}{print}' >  $faname
~/programs/RepeatMasker/RepeatMasker	-lib $lib \
				 	-pa 4 \
					-e crossmatch \
					-align \
					-html \
					-gff $faname
cd ..; 
