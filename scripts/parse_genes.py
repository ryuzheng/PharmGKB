# Written to parse the genes file from PharmGKB
# written 11-8-16, JLW

import csv,pickle,sys
csv.field_size_limit(sys.maxsize)

f='../data/genes.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

pharmGKB_genes_to_symbol={}
pharmGKB_genes_to_CPIC={}
pharmGKB_genes_to_var={}
for row in dr:
	gs=row['Symbol']
	pid=row['PharmGKB Accession Id']
	cpic=row['Has CPIC Dosing Guideline']
	vin=row['Has Variant Annotation']
	
	pharmGKB_genes_to_symbol[pid]=gs
	pharmGKB_genes_to_CPIC[gs]=cpic
	pharmGKB_genes_to_var[gs]=vin

pickle.dump(pharmGKB_genes_to_symbol,open('../mapped_dics/pharmGKB_genes_to_symbol.pkl','w'))
pickle.dump(pharmGKB_genes_to_CPIC,open('../mapped_dics/pharmGKB_genes_to_CPIC.pkl','w'))
pickle.dump(pharmGKB_genes_to_var,open('../mapped_dics/pharmGKB_genes_to_var.pkl','w'))
	

	
