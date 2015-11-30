import urllib
from lxml import etree
import os
import os, glob
import datetime
import logging
import feedparser
import ConfigParser
Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

class MTA(object):
    '''class to hold data about a NYC MTA line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name=name
        self.status=status
        self.text=text
        self.date=date
        self.time=time
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getText(self):
        return self.text
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def getMode(self):
        return self.mode

class Subway(MTA):
    '''class to hold data about a NYC Subway line'''
    def __init__(self, name, status, text, date, time):
        super(Subway, self).__init__(name, status, text, date, time)
        self.Mode='subway'
    
class MTAStatus():

    def __init__(self):
        url='http://web.mta.info/status/serviceStatus.txt'
        self.subwayDataAsXML=urllib.urlopen(url).read()
        #open('subwayData.xml', "w").write(xmlData)
        self.root = etree.XML(self.subwayDataAsXML)

                # uncomment to write XML data for later reference
                    #debugXMLfile = "xml\\mta_%s.xml" % (datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                    #open(debugXMLfile,"w").write(self.subwayDataAsXML)
                    #logging.debug('firefox.exe %s\\%s' % (os.getcwd(), debugXMLfile) )

        # get MTA metadata
        self.responseCode = self.root.xpath('responsecode')[0].text
        self.timeStamp = self.root.xpath('timestamp')[0].text
    def getReportTime(self):
        return self.timeStamp
    def getSubway(self):
        '''Subway data'''
        self.subwayDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('subway/line/name'))):
            name = self.root.xpath('subway/line/name')[count].text
            status = self.root.xpath('subway/line/status')[count].text
            text = self.root.xpath('subway/line/text')[count].text
            date = self.root.xpath('subway/line/Date')[count].text    
            time = self.root.xpath('subway/line/Time')[count].text
            s = Subway(name, status, text, date, time)

            #s = Subway(self.root.xpath('subway'))
            self.subwayDict[s.getName()] = s
        return self.subwayDict

if 1 == 1:
    
    mtaStatus=MTAStatus()
    timeMTA_ReportedData=mtaStatus.getReportTime()
    
    subwayDictionary=mtaStatus.getSubway()
    for name in sorted(subwayDictionary.keys()):
        if subwayDictionary[name].getName() == "BDFM" and subwayDictionary[name].getStatus() == "GOOD SERVICE":
            if subwayDictionary[name].getName() == "ACE" and subwayDictionary[name].getStatus() == "GOOD SERVICE":
                mtasubway = "Both the Blue and Orange subway lines have good service. "
        if subwayDictionary[name].getName() == "BDFM" and not subwayDictionary[name].getStatus() == "GOOD SERVICE":
                mtasubway = "The Orange line has %s " % (subwayDictionary[name].getStatus())
        if subwayDictionary[name].getName() == "ACE" and not subwayDictionary[name].getStatus() == "GOOD SERVICE":
                mtasubway = "The Blue line has %s " % (subwayDictionary[name].getStatus())


if Config.get('main','debug') == str(1):
  print mtasubway
