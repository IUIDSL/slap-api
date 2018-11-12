args = commandArgs()
fileName=args[length(args)]

query=read.table(paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/",fileName,sep=""),header=F,sep="\t")

rank.query=query[query$V4<0.01 | query$V5>0,]
if (nrow(rank.query)>0){
   rank.query=rank.query[order(rank.query$V4),]
   write.table(rank.query,paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/",fileName,".rank",sep=""),sep="\t",row.names=F,col.names=F,quote=F)
}


#search similar drugs
drug_matrix=read.delim("/var/www/html/rest/Chem2Bio2RDF/slap/data_matrix.txt",header=F,skip=1,row.names=1,sep="\t")
drug_matrix=as.matrix(drug_matrix)

candidate_drugs=NULL
pearsons=NULL
for (i in 1:nrow(drug_matrix)){
	pearson=cor(drug_matrix[i,],query$V3)
	pearson=signif(pearson,digits=3)
	if (pearson>0.75){
		candidate_drugs=c(candidate_drugs,row.names(drug_matrix)[i])
		pearsons=c(pearsons,pearson)
	}
}

if (length(candidate_drugs)>0){

results=data.frame(cid=candidate_drugs,score=pearsons)

drug_disease=read.table("/var/www/html/rest/Chem2Bio2RDF/slap/drug_diseases_group.txt",header=T,sep="\t")
results=merge(results,drug_disease,by.x="cid",by.y="cid")

drug_atc=read.table("/var/www/html/rest/Chem2Bio2RDF/slap/drug_ATC_group.txt",header=T,sep="\t")
results=merge(results,drug_atc,by.x="cid",by.y="cid")

results=results[order(results$score,decreasing=T),]
results=results[,c("cid","name","score","DBID","omim_diseases","atc")]
write.table(results,paste("/var/www/html/rest/Chem2Bio2RDF/slap/temp/",fileName,".similarDrugs",sep=""),sep="\t",row.names=F,col.names=F,quote=F)

#ooutput signature
signatures=data.frame(targets=query$V2, input=query$V3,t(drug_matrix[candidate_drugs,]))
write.table(signatures,paste("/var/lib/tomcat5/webapps/slap/temp/",fileName,".signatures.txt",sep=""),sep="\t",row.names=F,col.names=T,quote=F)

}

