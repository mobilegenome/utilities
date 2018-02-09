#!/bin/bash
id=$(echo $1 | sed 's/\#.*//g') # repeat id
rmoutfile=$2 # RepeatMasker outfile
grep "$id " $rmoutfile > "$rmoutfile.$id"
