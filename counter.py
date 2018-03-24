import requests
from xml.etree.ElementTree import *
import sys
import datetime

def get_date(date_str):
  ymd = [int(i) for i in date_str.split('-')]
  return datetime.datetime(ymd[0], ymd[1], ymd[2])

args = sys.argv
if len(args) < 1:
  print 'error'
  sys.exit()
user = args[1]
from_date = get_date(args[2])
to_date = datetime.datetime.now().strftime('%Y-%m-%d')
print 'user : @%s' % user
print 'from : %s' % from_date.strftime('%Y-%m-%d')
print 'to : %s' % to_date

req = requests.get('https://github.com/users/%s/contributions' % user)
if not req:
  print "%s is an org repo or does not exist." % user
  sys.exit()
  
root = fromstring(req.text)

g_tags = root.find('g')

contributions = 0

for g in g_tags.findall('g'):
  for rect in g.findall('rect'):
    if from_date < get_date(rect.get('data-date')):
      contributions += int(rect.get('data-count'))

print 'contributions : %d' % contributions
    

