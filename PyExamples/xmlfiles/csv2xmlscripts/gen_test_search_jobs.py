import os
import sys

from splunk.testing import SimpleRestTester

sys.path.append(os.path.join(os.path.curdir, '..'))
import generatexml
from generatexml import RestTesterXml

inputfile = 'search_jobs.csv'
outputfile = 'search_jobs_args.xml'

try:
    csvfile = open(inputfile, 'U')
except IOError, e:
    print e

dictreader = generatexml.readcsv(csvfile)
keys = dictreader.fieldnames

if not generatexml.header_valid(keys):
    sys.exit("csv file doesn't have correct format")

request_args = generatexml.get_queryargs(keys)

i = 0

myxml = RestTesterXml(
    "Verifying arguments of search endpoints that will be exposed (SPL-26133)")
myxml.add_auth()

try:
    for line in dictreader:
        if generatexml.format_valid(line):

            myxml.add_test(line, request_args)
            if line['#returncode'] == '201':
                teardown = {'#method': 'DELETE',
                            '#endpoint': '/services/search/jobs/${sid}',
                            '#comment': 'Teardown',
                            '#returncode': '200:retry'}
                myxml.add_test(teardown)
except Exception, e:
    print 'error: ' + str(e)

myxml.write(outputfile)
csvfile.close()

s = SimpleRestTester()
print s.executeTest(outputfile)
