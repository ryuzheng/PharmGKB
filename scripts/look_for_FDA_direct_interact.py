# Written 10-31-16, JLW to identify first neighbor
# interactions from psicquic interactome in OmicsInte. package

import csv, pickle

intf='../data/iref_mitab_miscore_2013_08_12_interactome.txt'
ints=[l.strip().split('\t') for l in open(intf,'rU').readlines()]

genef='../data/preclinical_targets.txt'
genes=[a.strip() for a in open(genef,'rU').readlines()]

for g in genes:
	g_int=[l for l in ints if g==l[0] or g==l[1]]
	sort_int=sorted(g_int,key=lambda x:x[2],reverse=True)
	outf=open('../results/'+g+'_interactome_binding.txt','w')
	if len(sort_int)>0:
		for l in sort_int:
			outf.write('\t'.join(l)+'\n')
	outf.close()
