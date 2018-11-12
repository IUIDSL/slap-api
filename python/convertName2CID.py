#!/usr/bin/python
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import sys
import urllib

from xml.dom import minidom
infile = open("/var/www/html/rest/Chem2Bio2RDF/slap/Dicts/drug_names", "r")
name=name.strip()
for line in infile:
	line=line.strip() 
	results=retrieveCIDsByName(line)
	if len(results)>0:
		print line+"\t"+results
	else
		print line+"\t"+"NA"
infile.close()
	
