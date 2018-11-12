from math import *
import sbv
import os, sys
import sendEmail
import rpy2.robjects as robjects

def getMap(filename, idx = (0, 1), sep = '\t', skip = 1):
	authormap = {}
	infile = open(filename, "r")
	while(skip > 0):
		#get the total number of authors/words/confs:
		line = infile.readline()
		skip -= 1

	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			mykey = tmp[idx[0]]
			myvalue = tmp[idx[1]]
			#remove prefix
			if "__" in mykey:
				mykey = mykey.split("__")[1]
			if "__" in myvalue:
				myvalue = myvalue.split("__")[1]
			if mykey not in authormap:
				authormap[mykey] = myvalue

	infile.close()
	return authormap

def getWeightMap(filename, idx = (0, 1), sep = '\t', skip = 1):
	pathMap = {}
	infile = open(filename, "r")

	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			mykey = tmp[0]
			myvalue = tmp[3]
			#remove prefix
			if mykey not in pathMap :
				pathMap [mykey] = myvalue

	infile.close()
	return pathMap 

#make pattern weight mean hash table
def getPatternWeightMeanMap(filename, sep = '\t'):
	pathMap = {}
	infile = open(filename, "r")

	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			mykey = tmp[0]
			myvalue = tmp[1]
			#remove prefix
			if mykey not in pathMap :
				pathMap [mykey] = myvalue

	infile.close()
	return pathMap 

#make pattern weight sd  table
def getPatternWeightSDMap(filename, sep = '\t'):
	pathMap = {}
	infile = open(filename, "r")

	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			mykey = tmp[0]
			myvalue = tmp[2]
			#remove prefix
			if mykey not in pathMap :
				pathMap [mykey] = myvalue

	infile.close()
	return pathMap 

def reformatePath(infile):
	path = ""
	flag = False
	outfile = []

	for line in infile:
        	line = line.strip()
        	if line == "find ans":
                	if path != "":
                        	outfile.append(path+'.')
                	flag = True
                	path = ""
        	elif flag:
                	tmp = line.split(" ")
                	path += tmp[1]+" "

	outfile.append(path+".")
	return outfile

def path2pair(pairs, pathline, sep = " ", end = '.'):
        # nodea relation nodeb relation nodec .
        pathline = pathline.strip()
        #print pathline
        tmp = pathline.split(sep)
        i = 0
        n = len(tmp)
        while(i<(n-3)):
                item1 = tmp[i]
                relation = tmp[i+1]
                item2 = tmp[i+2]
                #print item1, item2, relation
                i += 2
                if (item1, item2) not in pairs:
                        pairs[(item1, item2)] = relation
        return pairs

def path2network(pathfile, networkfile):
        infile = open(pathfile, "r")
        outfile = open(networkfile, "w")
        pairs = {}
        for line in infile:
                pairs = path2pair(pairs, line)

        for key in pairs:
                outfile.write('\t'.join(key)+'\t'+pairs[key]+'\n')
        infile.close()
        outfile.close()

def getDict(filename, sep = "-->"):
	mydict = {}
	infile = open(filename, "r")
	
	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			itemname = tmp[0]
			item = tmp[1]
			(itemtype, itemid) = item.split("__")
			if itemid not in mydict:
				mydict[itemid] = (itemname, itemtype)
	infile.close()
	return mydict

def getNode(networkfile):
	nodes = []
	infile = open(networkfile, "r")
	for line in infile:
		line = line.strip()
		tmp = line.split('\t')
		if len(tmp) > 1:
			item1 = tmp[0]
			item2 = tmp[1]
			if item1 not in nodes:
				nodes.append(item1)
			if item2 not in nodes:
				nodes.append(item2)

	infile.close()
	return nodes

def node2file(nodes, nodefile, dictfile):
	mydict = getDict(dictfile)
	outfile = open(nodefile, "w")
	for item in nodes:
		(itemname, itemtype) = (item, "unknown")
		if item in mydict:
			(itemname, itemtype) = mydict[item]
		outfile.write(item+'\t'+itemname+'\t'+itemtype+'\n')
	outfile.close()

def network2node(networkfile, nodefile, dictfile):
	nodes = getNode(networkfile)
	node2file(nodes, nodefile, dictfile)

def getPathName(infile, dictfile):
	mydict = getDict(dictfile)
	outfile = []
	for line in infile:
		re = ""
		line = line.strip()
		tmp = line.split(" ")
		if len(tmp) > 1:
			for i in range(0, len(tmp), 2):
				item = tmp[i]
				relation = tmp[i+1]
				if item in mydict:
					item = mydict[item][0].strip()
					#avoid long name
					x = item.split(" ")
					if len(x) > 3:
						item = "-".join(x[:3])
					elif len(x) > 1:
						item = "-".join(x)
				if i < (len(tmp)-2):
					re += item+" "+relation+" "
				else:
					re += item+ " "+relation
			outfile.append(re)
	return outfile


def getPathName_m(infile, dictfile):
	mydict = getDict(dictfile)
	outfile = []
	for line in infile:
		re = ""
		line = line.strip()
		tmp = line.split(" ")
		if len(tmp) > 1:
			for i in range(0, len(tmp), 2):
				item = tmp[i]
				relation = tmp[i+1]
				if item in mydict:
					itemname = mydict[item][0].strip()
					itemtype = mydict[item][1].strip()
					#avoid long name
					x = itemname.split(" ")
					if len(x) > 3:
						itemname = "-".join(x[:3])
					elif len(x) > 1:
						itemname = "-".join(x)
				else:
					itemname = "*"
					itemtype = "*"
				newitem = itemtype+"__"+item+":"+itemname
				if i < (len(tmp)-2):
					re += newitem+" "+relation+" "
				else:
					re += newitem+ " "+relation
			outfile.append(re)
	return outfile

def getPathScore(pathline, sep = " ", ntopic = 50):
	score = 0
        path1 = "dicts/"
        mapfile = "authormap.txt"
        probfile = "model-final"+str(ntopic)+".theta_ak"        
	rankmap = getRankMap(path1+mapfile, idx = (0,1), sep = "\t", skip = 1)
	pathline = pathline.strip()
	#print pathline
	tmp = pathline.split(sep)
	i = 0
	n = len(tmp)
	while(i<(n-3)):
		item1 = tmp[i]
		relation = tmp[i+1]
		item2 = tmp[i+2]
		sKL = 50 
               	if item1 in authormap and item2 in authormap:
                      	idx1 = int(authormap[item1])
                      	idx2 = int(authormap[item2])
                      	prob1 = getProbability(idx1, path1+probfile)
                      	prob2 = getProbability(idx2, path1+probfile)
                      	sKL = round(skldivergence(prob1, prob2),3)
			#print idx1, idx2, item1, item2, sKL
		score += sKL
		i += 2

	return score

def getPathScore1(weightMap, pathline, sep = " "):
	score = 0
	pathline = pathline.strip()
	#print pathline
	tmp = pathline.split(sep)
	i = 0
	n = len(tmp)
	weight=0
	while(i<(n-3)):
		item1 = tmp[i].split("/")
		item1=item1[len(item1)-1]
		relation = tmp[i+1].split("/")
		#relation = relation[len(relation)-1]
		if relation[len(relation)-1] == "":  #like .. hprd/
			relation= relation[len(relation)-2]
		else:
			relation = relation[len(relation)-1]
			
		item2 = tmp[i+2].split("/")
		item2 = item2[len(item2)-1]
		path_id=item1+"$"+relation+"$"+item2
 		
		sKL = 50 
		if relation == "neighbor":
			weight=weight+log(1-(0.7/0.15)*(1-float(weightMap[path_id])))
		else:
			weight=weight+log(float(weightMap[path_id]))
		i += 2

	return weight

def rankPath(infile, path2="", sep = " "):
	mypath = {}
	weightMap = getWeightMap(path2+"dicts/pair_weight.txt", idx = (0,1), sep = "\t", skip = 1)

	for line in infile:
		line = line.strip()       	
		score = getPathScore1(weightMap,line, sep)
		if line not in mypath:
			mypath[line] = score	
	return mypath

def writeDict(D, reverse = True, sep = '\t', n = -1):
	result = []
	i = 0
	if (n < 0):
		n = len(D)

	for (key, value) in sbv.sbv0(D,reverse):
		i += 1
		result.append(str(value)+sep+str(key))
		if i > n:
			break	
	return result

#input pathlist, output my path and it p value
def getPathPvalue(mypath,path2=""):
	result = []
	newpath = {}
	r = robjects.r

	expectMeanTable=getPatternWeightMeanMap(path2+"dicts/pattern_distribution.txt",sep="\t")
	expectSDTable=getPatternWeightSDMap(path2+"dicts/pattern_distribution.txt",sep="\t")

	z_score=0
	for key in mypath.keys():
		edges=key.split(" ")
		#if weight smaller than -10, ignore it, go to next path
		if (mypath[key])<-10:
			continue

		#if direct link, break 
		if (len(edges)<5): 
			newpath = {} #reinitiate 
			newpath[key]=0

			z_score=1000 #default, very high confidence
			break

		#find pattern
		i=1
		n=len(edges)
		pattern=""
		while(i<n-1):
			pattern=pattern+" "+edges[i]
			i += 2
		#print pattern
		#estimate z score
		if pattern in expectMeanTable:
			expected_mean=expectMeanTable[pattern]
			
			expected_sd=expectSDTable[pattern]
		else:
			expected_mean=-9.2
			expected_sd=2
		if mypath[key]>expected_mean :
			z_score=z_score+(mypath[key]-expected_mean)/expected_sd
			p_value=r.pnorm(mypath[key],mean=expected_mean,sd=expected_sd)
			newpath[key]=1-2*p_value[0]
	result.append(z_score)
	result.append(newpath)
	return result

#convert path to network using cutoff
def makeNetwork(newpath,cutoff=0):
	pairs = {}
	for key in newpath.keys():
		if newpath[key]<cutoff :
			edges=key.split(" ")
			pairs=path2pair(pairs, key)
	return(pairs)

#convert  network to graphml format
def convertNetwork2Graphml(network):
	result="<graphml>"+"\n"
	result=result+"\t"+"<key id=\"label\" for=\"all\" attr.name=\"label\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"class\" for=\"all\" attr.name=\"class\" attr.type=\"string\"/>"+"\n"
	result=result+"\t"+"<key id=\"uri\" for=\"all\" attr.name=\"uri\" attr.type=\"string\"/>"+"\n"

	result=result+"\t"+"<graph edgedefault=\"undirected\">"+"\n"

	nodes = []
	for (node1,node2) in network.keys():
		nodes.append(node1)
		nodes.append(node2)
	nodes=set(nodes)
	for node in nodes:
		result=result+"\t"+"<node id=\""+node+"\">"+"\n"
		strNode=node.split("/")
		
		result=result+"\t\t"+"<data key=\"label\">"+strNode[len(strNode)-1]+"</data>"+"\n"
		result=result+"\t\t"+"<data key=\"class\">"+strNode[len(strNode)-2]+"</data>"+"\n"
		result=result+"\t"+"</node>"+"\n"

	for (node1,node2) in network.keys():
		result=result+"\t"+"<edge source=\""+node1+"\" target=\""+node2+"\">"+"\n"
		strEdge=network[node1,node2]
		strEdges=strEdge.split("/")
		if strEdges[len(strEdges)-1]=="" :
			result=result+"\t\t"+"<data key=\"label\">"+strEdges[len(strEdges)-2]+"</data>"+"\n"
		else:
			result=result+"\t\t"+"<data key=\"label\">"+strEdges[len(strEdges)-1]+"</data>"+"\n"
			
		if strEdges[len(strEdges)-1]=="chemogenomics" :
			strNode1=node1.split("/")
			strNode2=node2.split("/")
			result=result+"\t\t"+"<data key=\"uri\">"+"http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/cid_gene/"+strNode1[len(strNode1)-1]+":"+strNode2[len(strNode2)-1]+"</data>"+"\n"
		else :
			result=result+"\t\t"+"<data key=\"uri\">"+strEdge+"</data>"+"\n"
		
		result=result+"\t"+"</edge>"+"\n"

	result=result+"\t"+"</graph>"+"\n"
	result=result+"</graphml>"+"\n"
	
	return(result)

def findNodeID(nodename, filename, sep = " "):
	nodeID = ""
	infile = open(filename, "r")
	for line in infile:
		line = line.strip()
		tmp = line.split(sep)
		if len(tmp) > 1:
			if tmp[1] == nodename:
				nodeID = tmp[0]
				break

	if len(nodeID) == 0:
		print nodename, "not involved in the network. Please try again!"
		#exit(1)
	return nodeID

def name2id(name2node, node2id, startname):
        startid = ""
	startnode = ""
        if startname in name2node.keys():
        	startnode = name2node[startname]
        elif startname in name2node.values():
        	startnode = startname
        else:
        	print "Node not find!"
                        

	if startnode in node2id and startnode != "":
        	startid = node2id[startnode]
        else:
        	print "Node not in the network!"

	return (startid, startnode)


def generalSearch2(startname, endname, op=2, maxL=3, path2 = ""):
	file1 = "/var/www/html/rest/Chem2Bio2RDF/slap/dicts/node2id.txt"

	#print startname, endname
	startid = findNodeID(startname, file1, sep = " ")
	#print startid
	endid = findNodeID(endname,file1, sep=" ")
	result=[]

	#if neither start node nor end node is in network, return null
	if (len(startid) ==0 or len(endid) ==0) :
		result.append(0)
		return result

	#print endid
        commandline =  "."+path2+"/findPath_m "+path2+"dicts/"+" "+str(op)+" "+str(startid)+" "+str(endid)+" "+str(maxL)
        
	output1 = os.popen(commandline)
	output2 = reformatePath(output1)

		#no path found
	if output2[0]=='.':
		result.append(1)
		return result

	mypath = rankPath(output2, path2, sep=" ") #weight

	#mypath = sbv.sbv0(mypath,reverse =True) #order the paths based on weight

	output3 = getPathPvalue(mypath,path2) #p value and z score

	z_score=output3[0]

	output4=makeNetwork(output3[1],0.5)
	
	#print mypath.values()
        #output3 = writeDict(mypath, reverse = True, sep = '\t', n = len(mypath))
        #output4 = getPathName(output3, path2+file2)
        #output5 = path2js(output4,  n = m)
	if z_score>300 :
		result.append("strong")
	elif z_score<=300 and z_score>56 :
		result.append("weak")
	elif z_score<=56 and z_score>0 :
		result.append("negative")
	elif z_score<=0 :
		result.append("unkown")

	result.append(z_score)
	result.append(convertNetwork2Graphml(output4))
	result.append(output3[1])

	return result


def generalSearchBatchCIDs(originalname, startnames, endname, op=2, maxL=3, path2 = "dicts/Chem2Bio2Rdf/"):

	result=[]
  	network={}
	paths ={}
	file1 = "node2id.txt"
	z_score=0

	endid = findNodeID(endname, path2+file1, sep=" ")
	
	for startname in startnames:
		#print startname, endname
		startid = findNodeID(startname, path2+file1, sep = " ")
	
		#if neither start node nor end node is in network, return null
		if len(startid) ==0 or len(endid) ==0 :
			continue
	
        	commandline =  "./findPath_m "+path2+" "+str(op)+" "+str(startid)+" "+str(endid)+" "+str(maxL)
        
		output1 = os.popen(commandline)
		output2 = reformatePath(output1)

		#no path found
		if output2[0]=='.':
			continue

		mypath = rankPath(output2, sep = " ", ntopic = 50) #weight

		output3 = getPathPvalue(mypath) #p value and z score
		#append paths
		for key in output3[1].keys() :
			newkey = " "+originalname+" "+"http://chem2bio2rdf.org/pubchem/resource/neighbor"+" "+key
			paths[newkey] = output3[1][key]

		z_score=z_score+output3[0]

	output4=makeNetwork(paths,0.5)

	if z_score>300 :
		result.append("strong")
	elif z_score<=300 and z_score>56 :
		result.append("weak")
	elif z_score<=56 and z_score>0 :
		result.append("negative")
	elif z_score<=0 :
		result.append("unkown")

	result.append(z_score)
	result.append(output4)
	result.append(paths)
	return result