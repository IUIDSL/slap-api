# ﻿SLAP SQL


From odbc6.py:


getGeneByName(name)
* "SELECT gene_symbol FROM c2b2r_chembl_08_target_dictionary WHERE UPPER(pref_name) = UPPER('"+name+"')"
* "SELECT \"Approved_Symbol\" FROM \"c2b2r_HGNC\" WHERE UPPER(\"Approved_Name\") = UPPER('"+name+"')"
getGeneByGI(gi)
* "SELECT \"geneSymbol\" FROM \"c2b2r_Gi2UNIPROT_new\",\"c2b2r_GENE2UNIPROT\" WHERE \"c2b2r_GENE2UNIPROT\".uniprot=\"c2b2r_Gi2UNIPROT_new\".uniprot and gi ="+(gi)
getGeneByUniprot(uniprot)
* "SELECT \"geneSymbol\" FROM \"c2b2r_GENE2UNIPROT\" WHERE UPPER(uniprot) = UPPER('"+uniprot+"')"
retrieveCIDsByNameDrugbank(name)
* "select cid from c2b2r_drugbankdrug_042011 where cid is not null and (upper(brand) like upper('%"+str(name)+";%') or upper(name) =upper('"+str(name)+"'))"
getCIDsbySMILES(SMILES)
* "SELECT cid FROM c2b2r_compound_new where md5(std_inchi)=md5('"+inchi+"')”
getSMILESByCID(cid)
* 'SELECT openeye_can_smiles FROM pubchem_compound where cid=' + str(cid)
getOMIMID(disease)
* "SELECT \"Disease_ID\" from c2b2r_omim_disease where \"Name\"='" + str(disease)+"'"
getNeighbors(SMILES)
* SELECT cid, tanimoto(gfp, public166keys(keksmiles('" + SMILES + "')))FROM c2b2r_compound_new WHERE gfpbcnt" + " BETWEEN (nbits_set(public166keys(keksmiles('" + SMILES + "'))) * 0.85)::integer" + " AND (nbits_set(public166keys(keksmiles('" + SMILES + "'))) / 0.85)::integer" + " AND tanimoto(gfp, public166keys(keksmiles('" + SMILES + "'))) > 0.85 ORDER BY tanimoto DESC, cid"
fetchTargetRelatedCompounds(gene)
* 'SELECT \"CID\" FROM c2b2r_chemogenomics where primary_source!=\' CTD \' and med_interested=1 and \"GENE\" in '+targets+' limit 500'
fetchTargetLigands(gene)
* 'SELECT \"CID\",openeye_can_smiles,primary_source FROM c2b2r_chemogenomics, c2b2r_compound_new where c2b2r_chemogenomics.\"CID\"=c2b2r_compound_new.cid and primary_source!=\' CTD \' and med_interested=1 and \"GENE\"=\''+gene+'\''
cidNetworks(input,cids)
* 'SELECT \"GENE\" FROM c2b2r_chemogenomics where primary_source!=\' CTD \' and med_interested=1 and \"CID\"=' + str(cid)
cidNetwork(cid)
* 'SELECT \"GENE\" FROM c2b2r_chemogenomics where primary_source!=\' CTD \' and med_interested=1 and \"CID\"=' + str(cid)
cidNetwork(gene)
* 'SELECT \"CID\" FROM c2b2r_chemogenomics where primary_source!=\' CTD \' and med_interested=1 and \"GENE\"=\''+gene+'\' limit 100'




Tables:
1. c2b2r_chembl_08_target_dictionary
2. c2b2r_chemogenomics
3. c2b2r_compound_new
4. c2b2r_drugbankdrug_042011
5. c2b2r_Gi2UNIPROT_new
6. c2b2r_GENE2UNIPROT
7. c2b2r_HGNC
8. c2b2r_omim_disease
9. pubchem_compound
