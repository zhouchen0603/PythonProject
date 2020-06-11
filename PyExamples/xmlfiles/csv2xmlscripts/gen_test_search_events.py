import os
import sys

from splunk.testing import SimpleRestTester

sys.path.append(os.path.join(os.path.curdir, '..'))
import generatexml
from generatexml import RestTesterXml

inputfile = 'search_events.csv'
outputfile = 'search_events_args.xml'

try:
    csvfile = open(inputfile, 'U')
except IOError, e:
    print e

dictreader = generatexml.readcsv(csvfile)
keys = dictreader.fieldnames

if not generatexml.header_valid(keys):
    sys.exit("csv file doesn't have correct format")

myxml = RestTesterXml(
    "Verifying arguments of /services/search/jobs/{sid}/events that will be exposed (SPL-26133)")
myxml.add_auth()

setup = {'#method': 'POST',
         '#endpoint': '/services/search/jobs',
         '#comment': 'Test Setup',
         '#returncode': '201',
         'search': 'search index=_internal',
         '#save': 'sid://sid'}
myxml.add_test(setup, ['search'])

setup = {'#method': 'POST',
         '#endpoint': '/services/search/jobs/${sid}/control',
         '#comment': 'Make sure the TTL is long enough for the duration of the whole test suite',
         '#returncode': '200',
         'action': 'setttl',
         'ttl': '3600'}
myxml.add_test(setup, ['action', 'ttl'])

request_args = generatexml.get_queryargs(keys)

try:
    for line in dictreader:
        if generatexml.format_valid(line):
            myxml.add_test(line, request_args)
except Exception, e:
    print e

teardown = {'#method': 'DELETE',
            '#endpoint': '/services/search/jobs/${sid}',
            '#comment': 'Teardown',
            '#returncode': '200',
            '#substring': 'Search job cancelled.'}
myxml.add_test(teardown)

myxml.write(outputfile)
csvfile.close()

s = SimpleRestTester()
print s.executeTest(outputfile)
