# written to find pathway ids for a given gene
# written 10-25-16 JLW

import pickle, csv, os
from optparse import OptionParser

# look at stored pathways
path_dir='../pathways/'
pathfs=[fs for fs in os.listdir(path_dir) if os.path.splitext(fs)[1]=='.tsv']

def create_gene_summary(gene):
	### pick a gene
	###gene = 'EDNRA'
	gene_data=[]
	# start summary report
	outf=open('../results/'+gene+'_pathwaySummary.txt','w')
	outf.write('gene name: '+gene+'\n')
	outf.write('\t'.join(['PathwayID','PathwayName','Controller','Control Type','From','To','Genes','Drugs'])+'\n')
	for p in pathfs:
		pathr=csv.DictReader(open(path_dir+p,'rU'),delimiter='\t')
		(pid,frest)=p.split('-')
		pname=frest.split('.')[0]

		for row in pathr:
			if gene in row.values():
				(c,cT,cfrom,cto,cgenes,d)=(row['Controller'],row['Control Type'],row['From'],row['To'],row['Genes'],row['Drugs'])
				path_data = [pid,pname,c,cT,cfrom,cto,cgenes,d]
				outf.write('\t'.join(path_data)+'\n')
				gene_data.append(path_data)
			
		#for row in pathr:
	#		path_data = [(pid,pname,k,v) for (k,v) in row.items() if gene in v]
	#		n=[outf.write('\t'.join(pd)+'\n') for pd in path_data]
	#		if gene in row['Controller']:
	#			(cT,cfrom,cto)=(row['Control Type'],row['From'],row['To'])
	#			path_data.append((pid,pname,cT,cfrom,cto))
	#			outf.write('\t'.join([cT,cfrom,cto])+'\n') 
	#	if len(path_data)>0:
	#		n=[gene_data.append(pd) for pd in path_data]
	outf.close()
	pickle.dump(gene_data,open('../results/'+gene+'_allPathwayData.pkl','w'))

def main():
	parser=OptionParser()
	parser.add_option('-g','--gene',dest='gene',help='HUGO gene symbol for pathway query')
	(options,args) = parser.parse_args()

	create_gene_summary(options.gene)

if __name__ == "__main__":
	main()

