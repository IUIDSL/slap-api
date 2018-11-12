from math import *
import sbv
import os, sys
import sendEmail

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


def getPathScore1(weightMap, pathline, sep = " ", ntopic = 50):
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

def rankPath(infile, sep = " ", ntopic = 50):
	mypath = {}
	#weightMap = getWeightMap("Dicts/pair_weight.txt", idx = (0,1), sep = "\t", skip = 1)

	for line in infile:
		line = line.strip()       	
		#score = getPathScore1(weightMap,line, sep, ntopic)
		if line not in mypath:
			mypath[line] = 0 #score	
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

def generalSearch(startname, endname, op=2, maxL=3, path2 = "Dicts/Chem2Bio2Rdf/"):
        file1 = "node2id.txt"
        sep1 = " "
        skip1 = 1
        idx1 = (1, 0)
        file2 = "all.txt"
        sep2 = "-->"
        idx2 = (0, 1)
        skip2 = 0
	#print startname, endname
	startid = findNodeID(startname, path2+file1, sep = " ")
	#print startid
	endid = findNodeID(endname, path2+file1, sep=" ")
	#print endid
        commandline =  "./findPath_m "+path2+" "+str(op)+" "+str(startid)+" "+str(endid)+" "+str(maxL)
        print commandline
        
	output1 = os.popen(commandline)
	output2 = reformatePath(output1)
        output1.close()
	mypath = rankPath(output2, sep = " ", ntopic = 50)
	#print mypath.values()
        output3 = writeDict(mypath, reverse = True, sep = '\t', n = len(mypath))
        #output4 = getPathName(output3, path2+file2)
        #output5 = path2js(output4,  n = m)
	return output3

