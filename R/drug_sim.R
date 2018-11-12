args = commandArgs()
cid2=args[length(args)]
cid1=args[length(args)-1]

#cid1=3446
#cid2=5719

#check referred drug
drug_matrix=read.delim("/var/www/html/rest/Chem2Bio2RDF/slap/data_matrix.txt",header=F,skip=1,row.names=1,sep="\t")
drug_matrix=as.matrix(drug_matrix)
referred_drugs=row.names(drug_matrix)
if (sum(referred_drugs==cid1)>0){
	cid1_slap=drug_matrix[which(referred_drugs==cid1),]
}else{
	query=read.table(paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/drug.",cid1,sep=""),header=F,sep="\t")
	cid1_slap=query$V3
}

if (sum(referred_drugs==cid2)>0){
	cid2_slap=drug_matrix[which(referred_drugs==cid2),]
}else{
	query=read.table(paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/drug.",cid2,sep=""),header=F,sep="\t")
	cid2_slap=query$V3
}

#referred targets
targets=read.table("/var/www/html/rest/Chem2Bio2RDF/slap/referred_targets.txt",stringsAsFactors=F)

pearson=cor(cid1_slap,cid2_slap)
pearson=signif(pearson,digits=3)

write.table(data.frame(targets=targets$V1,cmpd1=cid1_slap,cmpd2=cid2_slap,pearson=pearson),paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/",cid1,"_",cid2,sep=""),row.names=F,col.names=T,quote=F,sep="\t")

