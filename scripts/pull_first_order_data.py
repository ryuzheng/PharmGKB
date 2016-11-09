# written to pull interesting first-order relationships
# for a given gene target using mapped_dics
# written 11-8-16, JLW

import pickle

gene='FAAH'

# mined resources
qf = '../mapped_dics/gene_to_rsid_eQTL.pkl'# gene symbol to list of rsid, source =NIH eQTLs
qd = pickle.load(open(qf,'rU'))

rf = '../mapped_dics/rsid_g_pval_rsqr.pkl' # rsid to [geneSym,p-value,R^2]
rd = pickle.load(open(rf,'rU'))

sf = '../mapped_dics/pharmGKB_to_disease.pkl' # PharmGKB identifiers to disease name
sd = pickle.load(open(sf,'rU'))

vf = '../mapped_dics/pharmGKB_genes_to_var.pkl' # Gene symbols to Yes/No about clinical variations
vd = pickle.load(open(vf,'rU'))

cf = '../mapped_dics/gene_to_chem.pkl' # gene symbol to chemical names
cd = pickle.load(open(cf,'rU'))

rsids=qd[gene]
clin_var=vd[gene]
for r in rsids:
	rd[r]
chem=cd[gene]
