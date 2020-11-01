#!/usr/bin/env python

#use the regax module
import re

#read in the file
#in_file = open('source').read()

#or use string as input
in_file = '''
     <trk>
         <trkseg>
              <trkpt lat = "38.8577288" lon = "-9.0997973"/>
              <trkpt lat = "38.8576322" lon = "-9.1000000"/>
              <trkpt lat = "38.8577538" lon = "-9.1000000"/>
        </trkseg>
    </trk>
'''

#Find matches using regex
matches = re.findall('<trkpt lat = "([-0-9/.]+)" lon="(-0-9/.]+)"/>',in_file)

#make new file lines by combinig lat and lon from matches
out_lines = [lon + ',' + lat for lat,lon in matches]

#convert array of strings to single string
out_lines = '/n'.join(out_lines)

print out_lines
#output to new file
#open('dest','w').write(out_lines)
