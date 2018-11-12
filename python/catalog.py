import simplejson, urllib2, sys, string
from datetime import datetime
baseUrl = "http://myserver/arcgis/rest/services"

def getCatalog(folderName):
  catalog = simplejson.load(urllib2.urlopen(baseUrl + "/" + folderName + "?f=json"))
  print '%s (%s)' % (('ROOT' if folderName == '' else folderName), 'ERROR' if "error" in catalog else ('%d service(s)' % (len(catalog['services']))))
  if "error" in catalog: return
  services = catalog['services']
  for service in services:
    response = simplejson.load(urllib2.urlopen(baseUrl + '/' + service['name'] + '/' + service['type'] + "?f=json"))
    print '%s %s (%s)' % (service['name'], service['type'], 'ERROR' if "error" in response else 'SUCCESS')
  folders = catalog['folders']
  for folder in folders:
    getCatalog(folder)

startTime = datetime.now()
getCatalog('')
print 'Elapsed Time: %s' % (datetime.now() - startTime)