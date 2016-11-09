# Written to parse the PharmGKB annotations file
# written 11-8-16, JLW

import csv,pickle
from collections import defaultdict

f='../data/annotations/var_drug_ann.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

var_to_drug={}
gene_var_chem_anno=defaultdict(list)
for row in dr:
	rsid=row['Variant']
	chem=row['Chemical']
	sig=row['Significance']
	gene=row['Gene']
	sent=row['Sentence']
	
	var_to_drug[rsid]=chem
	gene_dic={'chem':chem,'significance':sig,'sentence':sent,'rsid':rsid}
	gene_var_chem_anno[gene].append(gene_dic)

pickle.dump(var_to_drug,open('../mapped_dics/var_to_drug.pkl','w'))
pickle.dump(gene_var_chem_anno,open('../mapped_dics/gene_var_chem_anno.pkl','w'))
