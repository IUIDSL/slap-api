#node statistics 
edges<-read.table("pathfinder_all.txt",header=F,sep="\t",stringsAsFactors=F)
nodes=unique(c(edges$V1,edges$V2))

compound=c(1:300000)*0
count=0
for (i in 1:length(nodes)){
   edge=unlist(strsplit(nodes[i],"/"))
   nodeClass=paste(edge[-length(edge)],collapse="/")
   node=edge[length(edge)]
   if (nodeClass=="http://chem2bio2rdf.org/pubchem/resource/pubchem_compound"){
	count=count+1
	compound[count]=node
   }
}
compound=compound[compound>0]
pairs=data.frame(cid=compound,target="NR1I2")
write.table(pairs,"pxr_library_all_c2b2r.txt",quote=F,sep="\t",row.names=F,col.names=F)