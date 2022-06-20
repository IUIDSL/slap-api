# ﻿SLAP troubleshooting

How to diagnose and correct problems when SLAP malfunctions.  That is, the web app http://cheminfov.informatics.indiana.edu:8080/slap.


1. SLAP the web app depends on Tomcat, Apache-HTTPD, and Postgresql.  
Are these services running?  Restarting services may correct problem.
1. Note that SLAP does not depend on Virtuoso [right?].
1. The web app depends on the SLAP REST API, as documented at http://slapfordrugtargetprediction.wikispaces.com/API.  Test the REST API.  Example URLs:
  * http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/slap/5591:PPARG
1. If the SLAP REST API does work, perhaps the Tomcat web app itself is the problem.  Restart Tomcat.  If needed, the files are in /usr/share/tomcat5/webapps/slap/.  
1. If the SLAP REST API does not work, try some other REST requests.  These use Apache-HTTPD (port 80).  If these fail the problem could be Apache-HTTPD.
  * http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/Bayes\_Model/5880:NR1I2
  * http://cheminfov.informatics.indiana.edu/rest/Chem2Bio2RDF/Sea\_Model/5591:PPARG
1. Note that REST API testing can be done via various clients (wget, curl, browsers).  It seems that error messages are sometimes client dependent, and browsers show mod\_python errors which wget does not.
1. The REST API depends on Python programs which can be run locally (http://slapfordrugtargetprediction.wikispaces.com/SLAP+interfaces).  Files are in /var/www/html/rest/Chem2Bio2RDF/slap/.
1. Please do not make any irreversible changes!  Document any changes.


### Packages used by SLAP

|Package|Description|
|---|---|
|Apache HTTPD|webserver|
|Apache Tomcat| Java servlet container|
|JME| Java Molecular Editor (applet)|
|JQuery| JavaScript library|
|CytoscapeWeb| Flash plugin for network visualization|
|CDK| Cheminfo Java kit used by webapp (maybe) |
|BioJava| Java kit used by webapp (maybe)|
|Blast| Used by webapp (maybe)|
|R| Used by webservice (previous to May 2014)|
|Virtuoso| (Not used by SLAP at runtime, I think.  However, dir exists at /var/www/html/rest/Chem2Bio2RDF/slap/virtuoso.|
|C++| (or maybe other compiled language) See compiled binary executables in /var/www/html/rest/Chem2Bio2RDF/slap: `findPath_m`, `pathfinder_m`,(maybe not needed, see `pathfinder\_m.py`), `PreProcess` (maybe not needed)|
|Psycopg2| Python API for Postgres|



_Jeremy Yang
May 22, 2014_
