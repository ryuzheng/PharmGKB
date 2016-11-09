# Written to parse the relationships between drugs and
# genes when available
# Written 11-8-16, JLW

import csv, pickle
from collections import defaultdict

f = '../data/relationships/relationships.tsv'
dr = csv.DictReader(open(f,'rU'),delimiter='\t')

chem_to_gene = defaultdict(list)
gene_to_chem = defaultdict(list)
for row in dr:
	et1=row['Entity1_name']
	et1t=row['Entity1_type']
	et2=row['Entity2_name']
	et2t=row['Entity2_type']


	if et1t=='Gene' and et2t=='Chemical':
		gene_to_chem[et1].append(et2)
		chem_to_gene[et2].append(et1)

	if et2t=='Gene' and et1t=='Chemical':
		gene_to_chem[et2].append(et1)
		chem_to_gene[et1].append(et2)

pickle.dump(chem_to_gene,open('../mapped_dics/chem_to_gene.pkl','w'))
pickle.dump(gene_to_chem,open('../mapped_dics/gene_to_chem.pkl','w'))
