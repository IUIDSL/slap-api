import pathfinder_m
import pathfinder_rank

def main():
    startname = "http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/5591" #15074
    endname = "http://chem2bio2rdf.org/uniprot/resource/gene/PPARG"
    path2 = ""
    maxL = 3
    op = 2
    #startname = raw_input("Please enter the start name: \n")
    #endname = raw_input("Please enter the end name: \n")
    result =  pathfinder_rank.generalSearch(startname, endname, op, maxL, path2)
    #if neither start node nor end node in network, result[0]=0, if no path find, result[0]=1
    #otherwise: 
    #reult[0] #result: strong, weak, negative unknown
    #result[1] #: z score
    #result[2]  #: network
    #result[3] #: path along with p value

    #newnetwork=pathfinder_rank.makeNetwork(result[3],0.05) #use to make new network
    #print len(result[3].keys())
    for line in result:
   	 print line

main()
