# Written to search the list of RSIDs and return locations
# written 10-27-16, JLW

import csv, pickle
from collections import defaultdict
from functools import partial

rsf='../data/rsid/rsid.tsv'
rsr=csv.DictReader(open(rsf,'rU'),delimiter='\t')

rs_dic=defaultdict(partial(defaultdict,list))
for row in rsr:
	# key the dictionary by gene name
	(gene,rs,gids,pids,loc)=(row['Gene Symbols'],row['RSID'],row['Gene IDs'],row['PharmGKB ID'],row['Location'])
	rs_dic[gene]['RSID'].append(rs)
	rs_dic[gene]['Gene IDs'].append(gids)
	rs_dic[gene]['PharmGKB'].append(pids)
	rs_dic[gene]['Location'].append(loc)

def find_rsids(g):
	rs=rs_dic[g][RSID]
	outf=open('../results/'+g+'_rsids.txt','w')
	outf.write('gene name: \n')
	outf.write('\n'.join(rs))
	outf.close()
	return rs

def main():
        parser=OptionParser()
        parser.add_option('-g','--gene',dest='gene',help='HUGO gene symbol for pathway query')
        (options,args) = parser.parse_args()
 
        find_rsids(options.gene)
 
if __name__ == "__main__":
        main()

