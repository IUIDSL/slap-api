-- Example queries as needed by odbc6.py.
SELECT gene_symbol, pref_name
FROM c2b2r_chembl_08_target_dictionary
WHERE UPPER(pref_name) = UPPER('Cellular retinoic acid-binding protein I')
;
--
SELECT "Approved_Symbol", "Approved_Name"
FROM "c2b2r_HGNC"
WHERE UPPER("Approved_Name") = UPPER('SFRS protein kinase 3')
;
--
SELECT "c2b2r_GENE2UNIPROT"."geneSymbol", "c2b2r_Gi2UNIPROT_new".gi
FROM "c2b2r_Gi2UNIPROT_new","c2b2r_GENE2UNIPROT"
WHERE "c2b2r_GENE2UNIPROT".uniprot="c2b2r_Gi2UNIPROT_new".uniprot
AND "c2b2r_Gi2UNIPROT_new".gi = '50949918'
;
--
SELECT "geneSymbol", uniprot
FROM "c2b2r_GENE2UNIPROT"
WHERE UPPER(uniprot) = UPPER('P26439')
;
--
SELECT cid, std_inchi, openeye_can_smiles, "pubchem_URL"
FROM c2b2r_compound_new
WHERE md5(std_inchi) = md5('InChI=1S/C6H15N/c1-2-3-4-5-6-7/h2-7H2,1H3')
;
--
SELECT *
FROM  c2b2r_compound_new
WHERE cid='5591'
;
--
SELECT openeye_can_smiles, iupac_name, iupac_traditional_name, inchikey, std_inchi
FROM pubchem_compound
WHERE cid = '8102'
;
--
SELECT "Disease_ID","Name","Disorder_class"
FROM c2b2r_omim_disease
WHERE "Name" = 'Histidinemia'
;
--
SELECT "CID"
FROM c2b2r_chemogenomics
WHERE TRIM(primary_source) != 'CTD'
AND med_interested=1
AND "GENE" = 'TUBA1A' limit 10
;
--
SELECT "GENE"
FROM c2b2r_chemogenomics
WHERE TRIM(primary_source) != 'CTD'
AND med_interested=1
AND "CID" = '443495'
;
--
SELECT "CID", "GENE", primary_source
FROM c2b2r_chemogenomics
WHERE TRIM(primary_source) != 'CTD'
AND med_interested = 1
AND "GENE" IN ('BCL2L12', 'CHKA', 'PON1', 'CD52', 'MAPK1', 'TMTC4') LIMIT 50
;
--
SELECT "CID", openeye_can_smiles, primary_source
FROM c2b2r_chemogenomics, c2b2r_compound_new
WHERE c2b2r_chemogenomics."CID" = c2b2r_compound_new.cid
AND TRIM(c2b2r_chemogenomics.primary_source) != 'CTD'
AND c2b2r_chemogenomics.med_interested=1
AND c2b2r_chemogenomics."GENE" = 'TUBA1A'
;
--
-- Requires gNova-Chord and OpenEye license.
-- Replace with RDKit!
-- SELECT cid, tanimoto(gfp, public166keys(keksmiles('" + SMILES + "')))
-- FROM c2b2r_compound_new
-- WHERE gfpbcnt" + " BETWEEN (nbits_set(public166keys(keksmiles('" + SMILES + "'))) * 0.85)::integer" +	"
-- AND (nbits_set(public166keys(keksmiles('" + SMILES + "'))) / 0.85)::integer" +	"
-- AND tanimoto(gfp, public166keys(keksmiles('" + SMILES + "'))) > 0.85 ORDER BY tanimoto DESC, cid"
-- ;
