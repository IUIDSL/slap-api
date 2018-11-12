#!/usr/bin/python
import commands
import urllib
from xml.dom import minidom
import odbc6
import pathfinder_rank5
import ppPairPrediction2
import pathfinder_rank_advanced



#print infile

#print("Cc1ccc(cc1)C(C)C".isdigit() )

#print(ppPairPrediction2.submitJobs("0.397580624623pxr.txt"))
#print(odbc4.checkTarget("Heat shock protein HSP 60"))

cid="3333333"
gene="AAAAAAAAa"
#print(odbc6.fetchTargetRelatedTargets("NEK4"))
#gene=odbc5.getGeneByName("PXR")
startname = "http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/"+str(cid)
endname = "http://chem2bio2rdf.org/uniprot/resource/gene/"+gene
#results =  pathfinder_rank4.generalSearch(startname, endname, '', 3, '')
#print(results)

print(odbc6.checkCompound("CN1CC[C@@H]([C@@H](C1)O)c2c(cc(c3c2oc(cc3=O)c4ccccc4Cl)O)O")) #expect 2244
#print(odbc6.getNeighbors("C1=C(C=CC=N1)N2C3=C4C=C(C=CC4=NC=C3N(C2=O)C)C5=CC(=CN=C5)COC"))
print(odbc6.checkCompound("ccc12CCC(CC1CCC3C2CCC4(C3CCC4=O)C)O")) #null
#print(odbc4.checkCompound("C=C1[C@H]2C[C@H](C3[C@](C1=O)(C2)C(=O)OC[C@@]13CCC[C@@]2(C1C(=O)CO2)C)O")) #2244
#print(odbc2.checkCompound("CCC12CCC(CC1CCC3C2CCC4(C3CCC4=O)C)O")) #null
#file1 = "/var/www/html/rest/Chem2Bio2RDF/slap/Dicts/target2id.txt"
#nodeMap = odbc6.getNeighbors("CCCCCC12CCC(CC1CCC3C2CCC4(C3CCC4=O)C)O")
#print nodeMap
#cid="http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/225" 	


#print(odbc6.getGeneByUniprot("P05177"))
#print(odbc.checkTarget("PXR"))
#print(odbc.checkTarget("O75469"))
#print(len(odbc.checkTarget("NR1I2111")))

#s="http://dddd/upload_randdd.file"
#print(s[(s.find("upload_")+7):len(s)])

#output = commands.getoutput('ps -A | grep R').split("\n")
#print(output)
#print(len(output))

startname="http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4"
endname="http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284"
nodeNeighbors={}

network={('http://bio2rdf.org/GO/GO:0016874', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0544147482263', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0005792'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0410124779492', ('http://bio2rdf.org/GO/GO:0015908', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0851373022978', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0006629'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0296025738874', ('http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa04920', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000479226231734', ('http://bio2rdf.org/GO/GO:0005792', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0410124779492', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0004467'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.000110027791106', ('http://chem2bio2rdf.org/uniprot/resource/gene/PPARD', 'http://bio2rdf.org/GO/GO:0015908'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0851373022978', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.000110027791106', ('http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa03320', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000544677003865', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://chem2bio2rdf.org/hgnc/resource/gene_family/ACS'): 'http://chem2bio2rdf.org/hgnc/resource/Gene_Family_Name\t0.0115446558799', ('http://bio2rdf.org/GO/GO:0007584', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00644022290265', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/PTGS2'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.140439832446', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0007584'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00644022290265', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0005778'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00238163271492', ('http://bio2rdf.org/GO/GO:0004467', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.000110027791106', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0005777'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0119669712662', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa00071'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000202387426357', ('http://bio2rdf.org/GO/GO:0005778', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00238163271492', ('http://chem2bio2rdf.org/uniprot/resource/gene/FADS1', 'http://bio2rdf.org/GO/GO:0007584'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0277188543683', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/FADS1'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.0277188543683', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/PPARG'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.0005206791406', ('http://chem2bio2rdf.org/uniprot/resource/gene/SLC8A1', 'http://bio2rdf.org/GO/GO:0007584'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.101462685638', ('http://bio2rdf.org/GO/GO:0006629', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0296025738874', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/SLC8A1'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.101462685638', ('http://chem2bio2rdf.org/hgnc/resource/gene_family/ACS', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/hgnc/resource/Gene_Family_Name\t0.0115446558799', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa04920'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000479226231734', ('http://chem2bio2rdf.org/uniprot/resource/gene/PPARG', 'http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/5591'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.0005206791406', ('http://chem2bio2rdf.org/uniprot/resource/gene/PPARG', 'http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa03320'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.336829750479', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa03320'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000544677003865', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/446284', 'http://chem2bio2rdf.org/uniprot/resource/gene/PPARD'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.0851373022978', ('http://chem2bio2rdf.org/kegg/resource/kegg_pathway/hsa00071', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/kegg/resource/protein\t0.000202387426357', ('http://chem2bio2rdf.org/uniprot/resource/gene/PTGS2', 'http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/5591'): 'http://chem2bio2rdf.org/chemogenomics/resource/expression\t0.140439832446', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0016874'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0544147482263', ('http://chem2bio2rdf.org/uniprot/resource/gene/ACSL3', 'http://bio2rdf.org/GO/GO:0005741'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00816457146107', ('http://bio2rdf.org/GO/GO:0005777', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.0119669712662', ('http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/5591', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/chemogenomics/resource/chemogenomics\t0.0005206791406', ('http://bio2rdf.org/GO/GO:0005741', 'http://chem2bio2rdf.org/uniprot/resource/gene/ACSL4'): 'http://chem2bio2rdf.org/uniprot/resource/GO_ID\t0.00816457146107'}

#node neighbors
for (node1,node2) in network.keys():
	if node1 in nodeNeighbors.keys():
		nodeNeighbors[node1]=nodeNeighbors[node1]+"\t"+node2
	else:
		nodeNeighbors[node1]=node2

	if node2 in nodeNeighbors.keys():
		nodeNeighbors[node2]=nodeNeighbors[node2]+"\t"+node1
	else:
		nodeNeighbors[node2]=node1		

#find parents
nodeParents={}
nodeChildren={}

for i in range(1,len(nodeNeighbors.keys())):
	node1=nodeNeighbors.keys()[i-1]
	neighbors1=nodeNeighbors[node1].split("\t").sort()
	class1=node1.split("/")
	class1=class1[len(class1)-2]

	#only node with 2 neighbors have parent; and node could not be grandparent
	if nodeNeighbors[node1].count("\t")==1 and node1!=startname and node1 !=endname and node1 not in nodeParents.keys():
		#find other nodes
		for j in range(i+1,len(nodeNeighbors.keys())+1):
			node2=nodeNeighbors.keys()[j-1]
			if nodeNeighbors[node2].count("\t")==1  and node2!=startname and node2 !=endname:
				class2=node2.split("/")
				class2=class2[len(class2)-2]
				#same class
				if class1==class2:
					neighbors1=sorted(nodeNeighbors[node1].split("\t"))
					neighbors2=sorted(nodeNeighbors[node2].split("\t"))

					#same neighbors
					if "".join(neighbors1)=="".join(neighbors2):
						#consider node1 is the parent of node2 
						nodeParents[node2]=node1
			
						#node 2 is the child of node1
						if node1 in nodeChildren.keys():
							nodeChildren[node1]=nodeChildren[node1]+"\t"+node2
						else:
							nodeChildren[node1]=node2

#if node has no child and itself is not a child
for node in nodeNeighbors.keys():
	if node not in nodeParents.keys() and node not in nodeChildren.keys():
		nodeChildren[node]=node	
						

#convert  network to graphml format
def convertNetwork2Graphml(startname,endname,network,nodes,nodeParents,nodeChildren):
	result="<graphml>"+"\n"
	result=result+"\t"+"<key id=\"label\" for=\"all\" attr.name=\"label\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"class\" for=\"all\" attr.name=\"class\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"uri\" for=\"all\" attr.name=\"uri\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"startnode\" for=\"all\" attr.name=\"startnode\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"evidence\" for=\"all\" attr.name=\"evidence\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"weight\" for=\"all\" attr.name=\"weight\" attr.type=\"double\"/>"+"\n"
	result=result+"\t"+"<key id=\"childnodes\" for=\"all\" attr.name=\"childnodes\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"nodesize\" for=\"all\" attr.name=\"nodesize\" attr.type=\"double\"/>"+"\n"

	result=result+"\t"+"<graph edgedefault=\"undirected\">"+"\n"

	#only show the nodes which are parents
	for node in nodeChildren.keys():
		result=result+"\t"+"<node id=\""+node+"\">"+"\n"
		strNode=node.split("/")

		children_number=0
		if nodeChildren[node]!=node:
			result=result+"\t\t"+"<data key=\"childnodes\">"+nodeChildren[node]+"</data>"+"\n"	
			children_number=nodeChildren[node].count("\t")+1	
			result=result+"\t\t"+"<data key=\"label\">"+strNode[len(strNode)-1]+"("+str(children_number)+")"+"</data>"+"\n"
		else:
			result=result+"\t\t"+"<data key=\"label\">"+strNode[len(strNode)-1]+"</data>"+"\n"
		
		result=result+"\t\t"+"<data key=\"class\">"+strNode[len(strNode)-2]+"</data>"+"\n"

		if node==startname or node==endname:
			result=result+"\t\t"+"<data key=\"nodesize\">"+"5"+"</data>"+"\n"
		elif children_number>0:
			result=result+"\t\t"+"<data key=\"nodesize\">"+"3"+"</data>"+"\n"
		else:
			result=result+"\t\t"+"<data key=\"nodesize\">"+"1"+"</data>"+"\n"
							
		if node==startname or node==endname:
			result=result+"\t\t"+"<data key=\"startnode\">"+"yes"+"</data>"+"\n"
		else:
			result=result+"\t\t"+"<data key=\"startnode\">"+"no"+"</data>"+"\n"
	
		result=result+"\t"+"</node>"+"\n"

	for (node1,node2) in network.keys():
		if node1 not in nodeChildren.keys() or node2 not in nodeChildren.keys():
			continue
		
		strEdge=network[node1,node2].split("\t")
		weight=float(strEdge[1])

		# if child weight<parent node, give to parent node. We wanna this edge weight to be minimum so that will not be filtered out 
		if node1 in nodeChildren.keys():
			for child in nodeChildren[node1].split("\t"):
				tempWeight=float(network[child,node2].split("\t")[1])
				if tempWeight<weight:
					weight=tempWeight

		if node2 in nodeChildren.keys():
			for child in nodeChildren[node2].split("\t"):
				#print node2+"\t"+child+"\t"+node1
				tempWeight=float(network[node1,child].split("\t")[1])
				if tempWeight<weight:
					weight=tempWeight
				
		result=result+"\t"+"<edge source=\""+node1+"\" target=\""+node2+"\">"+"\n"

		#weight
		result=result+"\t\t"+"<data key=\"weight\">"+strEdge[1]+"</data>"+"\n"
		
		#add edge type
		strEdges=strEdge[0].split("/")
		if strEdges[len(strEdges)-1]=="" :
			result=result+"\t\t"+"<data key=\"label\">"+strEdges[len(strEdges)-2]+"</data>"+"\n"
		else:
			result=result+"\t\t"+"<data key=\"label\">"+strEdges[len(strEdges)-1]+"</data>"+"\n"
		
		result=result+"\t\t"+"<data key=\"uri\">"+strEdge[0]+"</data>"+"\n"
		
		#add evidence
		if strEdges[len(strEdges)-1]=="chemogenomics" :
			strNode1=node1.split("/")
			strNode2=node2.split("/")
			#print(strNode2[len(strNode2)-2])
			if strNode2[len(strNode2)-2] == "gene":
				result=result+"\t\t"+"<data key=\"evidence\">"+"http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/cid_gene/"+strNode1[len(strNode1)-1]+":"+strNode2[len(strNode2)-1]+"</data>"+"\n"
			else:
				result=result+"\t\t"+"<data key=\"evidence\">"+"http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/cid_gene/"+strNode2[len(strNode2)-1]+":"+strNode1[len(strNode1)-1]+"</data>"+"\n"
		
		
		result=result+"\t"+"</edge>"+"\n"

	result=result+"\t"+"</graph>"+"\n"
	result=result+"</graphml>"+"\n"
	
	return(result)

result=convertNetwork2Graphml(startname,endname,network,nodeNeighbors.keys(),nodeParents,nodeChildren)
result=result.replace("\n","\\\n")

#print(result)
z_score=2196.68490639
p_value=1.14895307912e-04
z_score=round(z_score,2)
if p_value>1e-5:
	p_value=round(p_value,5)
print(z_score)
print(p_value)
