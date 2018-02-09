#!/bin/bash

# Wrapper to run RM buildSummary
# Automatically creates a table of scaffold lengths using samtools faidx

fasin=$1

samtools faidx $fasin 
cut -f1,2 ${fasin}.fai > ${fasin}.tsv


~/programs/RepeatMasker/util/buildSummary.pl	-genome ${fasin}.tsv \
						-useAbsoluteGenomeSize \
						${fasin}.out \
						> ${fasin}.out.summary
# EOF

