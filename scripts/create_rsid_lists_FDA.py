# Written to find any dbSNPs for a pilot gene's 
# first-neighbor interaction neighborhood
# written 10-31-16, JLW

import csv, pickle
from collections import defaultdict

# genes for pilot study
genef='../data/preclinical_targets.txt'
genes=[a.strip() for a in open(genef,'rU').readlines()]

# rsids as pulled from PharmGKB
rsidf='../data/rsid/rsid.tsv'
ks=['RSID','Gene IDs','Gene Symbols','PharmGKB ID','Location']

# organize rsids by gene
rs_by_gene=defaultdict(list)
rsr=csv.DictReader(open(rsidf,'rU'),delimiter='\t')
for r in rsr:
	rs_by_gene[r['Gene Symbols']].append(r['RSID'])

# output rsid list for each gene
for g in genes:
	rs=rs_by_gene[g]
	outf=open('../results/'+g+'_firstNeighbor_rsids.txt','w')
	for rsid in rs:
		outf.write('\t'.join([g,rsid])+'\n')
	# open first-neighbors file
	fnf='../results/'+g+'_interactome_binding.txt'
	fnd=[l.strip().split('\t') for l in open(fnf,'rU').readlines()]
	all_int=[a for [a,b,c] in fnd]+[b for [a,b,c] in fnd]
	fns=list(set(all_int))
	fns.remove(g)
	for fn in fns:
		rs=rs_by_gene[fn]
		for rsid in rs:
			outf.write('\t'.join([fn,rsid])+'\n')
	outf.close()

