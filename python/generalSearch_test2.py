import pathfinder_m
import pathfinder_rank
import pp
import ppDrugTargetPrediction
import pathfinder_rank_advanced
import odbc6

def main():
	originalname = "http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/CHEBI:155189"
	cid=456201
	smiles=odbc6.getSMILESByCID(cid)
	cids=odbc6.getNeighbors(smiles)
	startnames=[]
	for cid in cids:
		startnames.append("http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/"+str(cid))

	originalendname = "http://chem2bio2rdf.org/uniprot/resource/gene/NR1I2"
	genes=['NR1I2','VDR', 'NR1I3' ,'NR1H3', 'NR1H2', 'ECR', 'NR1H4']
	endnames=[]
	for gene in genes:
		endnames.append("http://chem2bio2rdf.org/uniprot/resource/gene/"+gene)

	path2 = ""
	maxL = 3
	op = 2

	result=pathfinder_rank_advanced.generalSimilarSearch(originalname ,startnames, originalendname ,endnames, op, maxL, path2)

	for line in result:
		print line

main()
