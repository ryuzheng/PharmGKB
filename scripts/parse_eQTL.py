# Written to parse the eQTL file from NCBI browser
# written 11-8-16, JLW

import csv,pickle
from collections import defaultdict

f='../data/eqtl-161104-1937-32105.tab.tsv'
dr=csv.DictReader(open(f,'rU'),delimiter='\t')

#['#', 'Analysis ID', 'SNP RS', 'SNP Chr.', 'SNP Position', 'Probe GI', 'Probe Chr.', 'Probe Position', 'Gene', 'Gene ID', 'mRNA', 'P-value', 'R-squared', 'Description']
rs_to_gene_eQTL={}
gene_to_rsid_eQTL=defaultdict(list)
rsid_g_pval_rsqr=defaultdict(list)

for row in dr:
	rs=row['SNP RS']
	g=row['Gene']
	mRNA=row['mRNA']
	pv=row['P-value']
	rsq=row['R-squared']

	rs_to_gene_eQTL[rs]=g
	gene_to_rsid_eQTL[g].append(rs)
	rsid_g_pval_rsqr[rs]=[g,pv,rsq]

# output and save mappings
pickle.dump(rs_to_gene_eQTL,open('../mapped_dics/rs_to_gene_eQTL.pkl','w'))
pickle.dump(gene_to_rsid_eQTL,open('../mapped_dics/gene_to_rsid_eQTL.pkl','w'))
pickle.dump(rsid_g_pval_rsqr,open('../mapped_dics/rsid_g_pval_rsqr.pkl','w'))



