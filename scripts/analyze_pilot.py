# written to collect data about pilot genes from FDA
# written 10-26-16, JLW

import pickle 
from find_pathways_by_gene import create_gene_summary

genef='../data/preclinical_targets.txt'
genes=[a.strip() for a in open(genef,'rU').readlines()]

for g in genes:
	create_gene_summary(g)
