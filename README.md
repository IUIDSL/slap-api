# SLAP REST API

Codebase for the SLAP REST API, normally deployed
via Apache HTTPD as originally on cheminfov.informatics.indiana.edu.  The SLAP REST API
is a central component in SLAP, used by the web app, command line tools, and directly
via HTTP clients.

### Files:

|File|Usage|Comments|Runtime, Pre-processing, or Other|
|---|---|---|---|
|`.htaccess`|Apache config, associates handlers with filetypes.||Runtime|
|`catalog.py`||||
|`convertName2CID.py`||||
|`drug_sim.R`||||
|`fileupload.html`||||
|`generalSearch_test1.py`||||
|`generalSearch_test2.py`||||
|`makePairs.R`|||Pre-processing|
|`odbc6.py`|||Runtime|
|`pathfinder_m.py`||||
|`pathfinder_rank1_backup.py`||||
|`pathfinder_rank2_backup.py`||||
|`pathfinder_rank3_backup.py`||||
|`pathfinder_rank5.py`||||
|`pathfinder_rank_advanced.py`||||
|`pathfinder_rank_backup.py`||||
|`pathfinder_rank_backup_R.py`||||
|`ppDrugTargetPrediction1.py`||||
|`ppPairPrediction2.py`|||Runtime|
|`ppPairPrediction_local.py`||||
|`prediction1.py`||||
|`prediction2_backup.py`||||
|`save_file.py`|||Other|
|`sbv.py`||||
|`sendEmail.py`|||Other|
|`stats.R`||||
|`sum_primes.py`||||
|`test.py`|||Other|


### Dependencies:

 *	R? (Or did I replace this?)
 *	Python (v 2.7+?)
 *	Python pkg: [!] msvcrt		(only in save_file.py)
 *	Python pkg: [X] operator
 *	Python pkg: [X] parse 
 *	Python pkg: [X] pp
 *	Python pkg: [X] profile
 *	Python pkg: [X] psycopg2
 *	Python pkg: [*] rpy2		(Not needed due to revision to solve 2014 outage.)
 *	Python pkg: [X] simplejson
 *	Python pkg: [!] smtplib		(only in sendEmail.py)
 *	Python pkg: [X] SOAPpy
 *	Python pkg: [X] SPARQLWrapper
 *	Python pkg: [X] xml.dom.minidom

