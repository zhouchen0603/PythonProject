import os
import sys
import re
import csv
from xml.etree import ElementTree as ET

methods = ['GET', 'POST', 'DELETE', 'PUT']

NONARGSCHAR = '#'
METHOD = '%smethod' % NONARGSCHAR
ENDPOINT = '%sendpoint' % NONARGSCHAR
RETURNCODE = '%sreturncode' % NONARGSCHAR
COMMENT = '%scomment' % NONARGSCHAR
XPATH = '%sxpath' % NONARGSCHAR
REGEX = '%sregex' % NONARGSCHAR
SAVE = '%ssave' % NONARGSCHAR
PAUSE = '%spause' % NONARGSCHAR


def readcsv(csvhandler, reader='dict'):
    """
    returns list or dict of items from csv data
    """
    dialect = csv.Sniffer().sniff(csvhandler.read(2048))
    if reader == 'dict':
        csvhandler.seek(0)
        return csv.DictReader(csvhandler, dialect=dialect)
    if reader == 'list':
        csvhandler.seek(0)
        return csv.reader(csvhandler, dialect=dialect)


def header_valid(keys):
    """
    >>> print header_valid([METHOD, ENDPOINT, RETURNCODE])
    True
    """
    if METHOD not in keys:
        return False
    if ENDPOINT not in keys:
        return False
    if RETURNCODE not in keys:
        return False
    return True


def format_valid(input):
    if cell_invalid(input[METHOD]):
        return False
    if cell_invalid(input[ENDPOINT]):
        return False
    if cell_invalid(input[RETURNCODE]):
        return False
    return True


def get_queryargs(keys):
    """
    >>> print get_queryargs(['#notargument', 'argument'])
    ['argument']
    >>> print get_queryargs(['#notargument'])
    []
    >>> print get_queryargs(['argument'])
    ['argument']
    """
    list = []
    for item in keys:
        if not item.startswith('#'):
            list.append(item)
    return list


def cell_invalid(value):
    """
    >>> cell_invalid(None)
    True
    >>> cell_invalid('')
    True
    >>> cell_invalid(' ')
    True
    >>> cell_invalid('0')
    False
    """
    if value is None:
        return True
    if value.strip() is '':
        return True
    return False


def fixexcelhack(value):
    """
    >>> fixexcelhack("#")
    '#'
    >>> fixexcelhack("# ")
    ' '
    >>> fixexcelhack("#1")
    '1'
    >>> fixexcelhack("1")
    '1'
    >>> fixexcelhack(" ")
    ' '
    """
    keyword = NONARGSCHAR
    if not value.startswith(keyword):
        return value
    if value == NONARGSCHAR:
        return value
    return value[len(keyword):]


class XmlBuilder(object):

    def _add_node(self, parentnode, nodename, content=None, attrib={}):
        if parentnode is None:
            return None
        e = ET.SubElement(parentnode, nodename)
        if content is not None:
            e.text = fixexcelhack(content).strip()
        for key in attrib:
            if not cell_invalid(attrib[key]):
                e.set(key, attrib[key].strip())
        return e


class RestTesterXml(XmlBuilder):
    root = None

    def __init__(self, desc=None):
        self.root = ET.Element("tests")
        self._add_node(self.root, "desc", desc)

    def add_baseuri(self, baseuri):
        u = baseuri
        # simple error handling
        if len(u.split(':')) is not 2:
            u = "localhost:8089"
        splitted = u.split(":")
        self._add_node(self.root, "hostname", splitted[0])
        self._add_node(self.root, "port", splitted[1])

    def add_auth(self, username="admin", password="changeme"):
        auth = self._add_node(self.root, "auth", attrib={'mode': 'digest'})
        self._add_node(auth, "username", username)
        self._add_node(auth, "password", password)

    def add_test(self, testinput, arguments=[]):

        value = testinput[RETURNCODE].split(':')
        returncode = value[0].strip()
        retry = False
        if len(value) > 1:
            if value[1].strip() == 'retry':
                retry = True

        test = RestTestXml(self._add_node(self.root, "test"),
                           testinput[METHOD],
                           testinput[ENDPOINT],
                           returncode, retry)

        if COMMENT in testinput:
            if not cell_invalid(testinput[COMMENT]):
                test.add_desc(testinput[COMMENT])

        if len(arguments) > 0:
            test.add_arguments(testinput, arguments)

        if XPATH in testinput:
            test.add_expxpath(testinput)

        if REGEX in testinput:
            test.add_expregex(testinput)

        if SAVE in testinput:
            if not cell_invalid(testinput[SAVE]):
                test.store(testinput)

        if PAUSE in testinput:
            if not cell_invalid(testinput[PAUSE]):
                t = self._add_node(self.root, "test")
                self._add_node(t, "pause", testinput[PAUSE])

    def add_backupinfo(self):
        pass

    def write(self, filename):
        try:
            ET.ElementTree(self.root).write(filename)
        except IOError, e:
            print e


class RestTestXml(XmlBuilder):
    test = None
    xml = None

    def __init__(self, test, method, endpoint, returncode, retry=False):
        self.test = test

        self.request = self._add_node(self.test, "request")
        self.method = self._add_node(self.request, "method", method)
        path = self._add_node(self.request, "path", endpoint)

        self.response = self._add_node(self.test, "response")
        returncode = self._add_node(self.response, "status", returncode)
        if retry:
            returncode.set('retryUntilTrue', 'true')

    def add_desc(self, desc=None):
        desc = self._add_node(self.test, "desc", desc)

    def add_arguments(self, testinput, args):
        if self.method.text == 'GET':
            arguments = self._add_node(self.request, "query")
        elif self.method.text == 'POST':
            arguments = self._add_node(self.request, "form")
        for key in args:
            if not cell_invalid(testinput[key]):
                self._add_node(arguments, "arg", testinput[key], {'name': key})

    def add_expbody(self, code):
        pass

    def add_expheader(self):
        pass

    def add_expsubstring(self):
        pass

    def add_expregex(self, testinput):
        regex = self._add_node(self.response, "regex")
        for key in testinput:
            if key == REGEX and not cell_invalid(testinput[key]):
                self._add_node(regex, "pattern", testinput[key])

    def add_expxpath(self, testinput):
        if self.xml is None:
            self.xml = self._add_node(self.response, "xml")
        for key in testinput:
            if key == XPATH and not cell_invalid(testinput[key]):
                value = testinput[key].split(':')
                xpath = self._add_node(self.xml, "xpath", attrib={
                                       'selector': value[0]})
                if len(value) > 1:
                    xpath.text = value[1]

    def store(self, testinput):
        if self.xml is None:
            self.xml = self._add_node(self.response, "xml")
        value = testinput[SAVE].split(':')
        xpath = self._add_node(self.xml, "xpath", attrib={
                               'save': value[0], 'selector': value[1]})

if __name__ == "__main__":

    import doctest
    doctest.testmod()
