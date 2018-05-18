#!/usr/bin/python

__author__ = 'Fritjof Lammers'

'''
This program counts phylogenetic content in terms of numbers of phylogenetic informative sites for a pair of sequences. 
'''


import argparse
import os
import random
from Bio import AlignIO
from Bio import Align
from Bio import SeqIO
from collections import Counter


def phylo_sites(alignment):
    ID =  alignment[0].id
    n = len(alignment)
    sites = []
    for i in xrange(0, len(alignment[0])):
        column = list(alignment[:, i])
        if 2 <= len(set(column)) < len(column): # is site phyologentically informative
            if len([e for e in Counter(column).values() if e>=2]) >=2:
                sites.append(i)
        else:
            continue

    return sites

def genetic_distance(alignment, taxa):
    ID =  alignment[0].id
    selected_alignment = []
    n = len(alignment)
    for record in alignment:
        if record.id.split("_")[0] in taxa:
            selected_alignment.append(record)

    alignment = Align.MultipleSeqAlignment(selected_alignment)

    sites = []
    for i in xrange(0, len(alignment[0])):
        column = list(alignment[:, i])
        if len(set(column)) == 2: # is site phyologentically informative
            sites.append(i)
        elif len(set(column)) == 1:
            continue
        else:
            print "Something's wrong with\n%s" %",".join(column)

    return sites

def main():
    fname_list = [os.path.join(options.input_path,fpath) for fpath in os.listdir(options.input_path) if fpath.endswith(".fasta")]
    fout = open(options.output_file, "w")
    if options.taxa:
        print "*** You selected taxa for pairwise comparison: %s\n" %",".join(options.taxa)
    if options.random:
        print "*** You selected a randomized survey on",
        if options.random < 1:
            random_count = len(fname_list)*options.random
            print "%i fragments (%g * %i). \n" %(int(random_count),options.random, len(fname_list) )
        else:
            random_count = int(options.random)
            print "%i fragments.\n" %int(random_count)

        fname_list = random.sample(fname_list, int(random_count))
    for fpath in fname_list:
        print fpath
        fname = os.path.basename(fpath)
        alignment = AlignIO.read(fpath, "fasta")
        pi_sites = phylo_sites(alignment)
        if options.taxa:
            dis_sites = genetic_distance(alignment, options.taxa)
            fout.write("%s\tpi_sites\t%i\n" %(fname, len(pi_sites)))
            fout.write("%s\tdistance(%s)\t%i\n" %(fname, "-".join(options.taxa),len(dis_sites)))

        else:
            fout.write("%s\tpi_sites\t%i\n" %(fname, len(pi_sites)))

    fout.close()
    print "END"
    return 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-i', '--input_path', required=True, action="store", help='Path to input files (genome fragments). Must be a folder with .fasta files containing the aligned genomic sequences. ')
    parser.add_argument('-o', '--output_file', required=True, action="store", help='Output file')
    parser.add_argument('-t', '--taxa', required=False, action="append", help='selected taxa for genetic distance calculation (optional) [random]')
    parser.add_argument('-r', '--random', required=False, action="store", type = float, help='Number of randomly selected fragments. Can also be percentage (as decimal)')

    options = parser.parse_args()

    main()
