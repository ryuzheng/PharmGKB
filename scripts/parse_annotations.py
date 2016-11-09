# Written to parse the PharmGKB annotations file
# written 11-8-16, JLW

import csv,pickle

f='../data/annotations/var_drug_ann.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

var_to_drug={}
for row in dr:
	rsid=row[]
	chem=row[]
	sig=row['Significance']
	gene=row['Gene']
	sent=row['Sentence']
