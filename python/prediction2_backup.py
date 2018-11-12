#!/usr/bin/env python


from mod_python import apache
import string
import sys
import SOAPpy

from xml.dom.minidom import parse 
from SPARQLWrapper import JSON
from SPARQLWrapper import SPARQLWrapper
import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/html/rest/Chem2Bio2RDF/.python-eggs'


def handler(req):
    #try:
        #s = SOAPpy.WSDL.Proxy('http://cheminfov.informatics.indiana.edu:8080/polypharmacology/services/Sea?wsdl')
        #s1 = SOAPpy.WSDL.Proxy('http://cheminfov.informatics.indiana.edu:8080/polypharmacology/services/QSAR?wsdl')
    #except RuntimeError, e:
        #req.write(str(e))
        #return apache.HTTP_FAILED_DEPENDENCY
    

    uriParts = req.uri.split(':')
    if(len(uriParts) == 2):
        gene = uriParts[-1]
        cid = int(uriParts[-2].split('/')[-1])
        limit = 200
    #else:
        #limit = int(uriParts[-1])
        #gene = uriParts[-2]
        #cid = int(uriParts[-3].split('/')[-1])
    startname = "http://chem2bio2rdf.org/pubchem/resource/pubchem_compound/"+str(cid)
    endname = "http://chem2bio2rdf.org/uniprot/resource/gene/"+gene
    path2 = "/var/www/html/rest/Chem2Bio2RDF/slap/"
    maxL = 3
    op = 2
    import pathfinder_rank1
    results =  pathfinder_rank1.generalSearch2(startname, endname, op, maxL, path2)
    req.write(str(results[0])+"\n"+str(results[1])+"\n"+str(results[2]))
    #req.write("Predictive results form Sea Model: " + results +startname +"\n"+endname+ "\r\n")
    return apache.OK        
        
