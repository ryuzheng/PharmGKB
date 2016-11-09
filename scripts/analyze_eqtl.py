# written to explore the eqtl 
# 11-4-16, JLW

import csv

f='../data/eqtl-161104-1937-32105.tab.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

for row in dr:
	row['SNP RS']
	row['Gene']
	row['mRNA']
	row['P-value']
	row['R-squared']
	row['Description']
