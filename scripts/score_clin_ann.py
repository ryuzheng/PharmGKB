# Written to parse the relationships between drugs and
# genes when available
# Written 11-16-16, JLW

import csv, pickle, math

# define constants for later
(kp,ke)=(1.0,1.0)
bmax = 7 # max number of publications
evi_dic = {'1A':0.99,'1B':0.86625,'2A':0.7425,'2B':0.61875,'3':0.4950,'4':0.2475}
gscm_evi = sum(evi_dic.values())

def pub_score(plist):
        pn = len(plist)
        if pn > bmax:
                pn=bmax
        b = bmax
        sp=math.log(pn+1,b+1)

        return sp

def evidence_score(evi):
	a = evi_dic[evi]
	b = a + gscm_evi

	se = math.log(a+1,b+1)
	return se
	

def miscore(d): # pass the method a dictionary of data for the interaction
        plist = d['pub'] # publication list
        sp = pub_score(plist)

        evi = d['evi'] # type of evidence
        se = evidence_score(evi)

        smi = (kp*sp + ke*se)*(1/(kp+ke))
        return smi



f='../data/annotations/clinical_ann_metadata.tsv'
dr = csv.DictReader(open(f,'rU'),delimiter='\t')


drug_gene_dic = {}
int_scores = {}
for row in dr:
#['Genotype-Phenotype IDs', 'Variant Annotations IDs', 'Level of Evidence', 'Related Chemicals', 'PMIDs', 'Related Diseases', 'Evidence Count', 'Variant Annotations', 'Race', 'Location', 'Annotation Text', 'Gene', 'Clinical Annotation Types', 'Clinical Annotation Id']
	int_data = {}
	loc = row['Location'] #RSID number

	pmids = row['PMIDs']
	int_data['pub'] = pmids.replace('"','').split(',') # split out and save all PubMedIds

	evi_lvl = row['Level of Evidence']
	int_data['evi'] = evi_lvl

	# split if there are multiple chemicals
	chems = row['Related Chemicals']
	if ',' in chems:
		chems = chems.replace('"','').split(',')
	else:
		chems=[chems] # make sure it's a list for further output

	# split if multiple genes
	gene = row['Gene']
	if gene=='':
		print('Found annotation without gene association: ',row['Clinical Annotation Id'])
		continue
	if ',' in gene:
		gene = gene.replace('"','').split(',')
	else:
		gene=[gene]

	# create interaction for drug->rsid
	smi = miscore(int_data)
	for c in chems:
		for g in gene:
			int_scores[(c,loc)] = smi 
			int_scores[(g,loc)] = 0.99
			drug_gene_dic[(c,loc,g)] = smi 

# save and write output
pickle.dump(drug_gene_dic,open('../mapped_dics/drugLocGene_fromClinnAnn.pkl','wb'))
pickle.dump(int_scores,open('../mapped_dics/clinAnn_drugToRSID_scores.pkl','wb'))
outf = open('../results/drug_loc_gene_scored_interactions.txt','w')
for ((a,b),smi) in int_scores.items():
	outf.write('\t'.join([a,b,str(smi)])+'\n')
outf.close()
