'''
Created on Aug 26, 2012

@author: lior
'''
import simplejson
import os, sys
import urllib2
import urllib
import cStringIO
import time

getLocationUrl = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        textFile = sys.argv[1]
    else:
        textFile = 'locations.txt'
    
    

#    locations = ['tel aviv', 'jerosalem']
#    for location in locations:
    
    
    locations = [line.strip() for line in open(textFile)]

        
    for location in locations:
        location = '%s ישראל ' % location
        enCodeLocation = urllib.quote_plus(location)
        getLocationUrlFull = "%s&address=%s" % (getLocationUrl, enCodeLocation)
        output = urllib2.urlopen(getLocationUrlFull,timeout=600) # 600 seconds timeout
        output2 = output.fp
        data = simplejson.load(output2)
        if len(data['results']) > 0 : 
            placeLocation = data['results'][0]['geometry']['location']
            print('%s,%g,%g' % (location, placeLocation['lat'],placeLocation['lng']))
        else:
            print('%s' % (location))
        

    pass
