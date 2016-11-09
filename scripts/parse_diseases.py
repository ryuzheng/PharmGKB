# Written to create a dicionary of PharmGKB-> disease indentifiers
# written 11-8-16, JLW

import csv, pickle

f='../data/diseases/diseases.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

pharmGKB_to_disease={}
for row in dr:
	pid=row['PharmGKB Accession Id']
	nm=row['Name']
	pharmGKB_to_disease[pid]=nm

pickle.dump(pharmGKB_to_disease,open('../mapped_dics/pharmGKB_to_disease.pkl','w'))
