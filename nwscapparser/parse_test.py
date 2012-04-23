# http://alerts.weather.gov/
# http://alerts.weather.gov/cap/ga.php?x=0
# to get counties (and all sorts of other crap) from lat/lon, use http://maps.google.com/maps/geo?ll=40,-85
# to get counties from lat/lon with SAME codes (FIPS), use http://data.fcc.gov/api/block/find?latitude=34.74&longitude=-85.25

import feedparser
from pprint import pprint
from us_states import states

u = r'http://alerts.weather.gov/cap/%(feed_abbr)s.php?x=1'

#feeds = ['ga','sc','tn','al','fl']
#feeds = ['tn']
feeds = ['us']


SEVERE_ONLY = True
IMMEDIATE_ONLY = False

def parse_cap(c):
    pprint(c)
    for e in c.entries:
        pprint(e)
        try:
            print '='*10,e.cap_event.upper()
            print 'Id:',e.id
            print 'Published:',e.published
            print 'Updated:',e.updated
            print 'Effective:',e.cap_effective
            print 'Expires:',e.cap_expires
            print 'Counties:',e.cap_areadesc
            print 'Summary:',e.summary
        except:
            raise

def parse_feed(d):
    seen_ids = []
    for e in d.entries:
        try:
            if e.id in seen_ids: continue
            seen_ids.append(e.id)
            if SEVERE_ONLY or IMMEDIATE_ONLY:
                if SEVERE_ONLY and e.get('cap_severity','').strip().upper() == 'SEVERE':
                    parse_cap(feedparser.parse(e.link))
                if IMMEDIATE_ONLY and e.get('cap_urgency','').strip().upper() == 'IMMEDIATE':
                    parse_cap(feedparser.parse(e.link))
            else:
                parse_cap(feedparser.parse(e.link))
        except:
            pprint(e)
            raise

def parse_feeds(feed_abbrs):
    for feed_abbr in feed_abbrs:
        print '*'*20,feed_abbr.upper()
        parse_feed(feedparser.parse(u%locals()))

parse_feeds(feeds)