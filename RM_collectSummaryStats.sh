#!/bin/bash

species=$1
sample_id=$2
summary_in=$3

sed -n -e '/Class /,/Total/ p' $summary_in |\
sed  -n '3,1000p' |\
sed 's/total interspersed/total_interspersed/g'|\
awk -v species=${species} -v sample=${sample_id} \
	'{
	OFS="\t";
	if (match($0, "^([A-Za-z]+)",rowstart) ) class=rowstart[1]; gsub("%", "", $4);
	print species,sample,class, $1, $4/100}' |\
grep -v "\-\-" > ${summary_in/.summary/.summary.tsv} 
