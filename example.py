from pprint import pprint
import urllib2
import feedparser
import ast

from NWSCAPParser import NWSCAPParser
from us_states import states

CAP_FEED_URL_TMPL = u'http://alerts.weather.gov/cap/%(feed_abbr)s.atom'

feeds = ['ga','sc','tn','al','fl']
#feeds = ['tn']
#feeds = ['us']

SEVERE_ONLY = True
IMMEDIATE_ONLY = False

NO_ALERTS_CAP_TITLE = u'There are no active watches, warnings or advisories'

def get_cap_xml(cap_url):
    response = urllib2.urlopen(cap_url)
    return response.read()

def build_cap(cap_url):
    cap = NWSCAPParser(get_cap_xml(cap_url))
    return cap

def parse_feed(d,url):
    seen_ids = []
    _max = 10
    i = 0
    for e in d.entries:
        cap = None
        try:
            if e.id == url:
                print ' (No alerts)'
                break
            if e.id in seen_ids: continue
            seen_ids.append(e.id)
            if SEVERE_ONLY and e.get('cap_severity','').strip().upper() == 'SEVERE':
                cap = build_cap(e.link)
            elif IMMEDIATE_ONLY and e.get('cap_urgency','').strip().upper() == 'IMMEDIATE':
                cap = build_cap(e.link)
            else:
                cap = build_cap(e.link)
        except:
            pprint(e)
            raise
        if cap:
            try:
                pprint(cap.as_dict())
            except:
                pprint(repr(cap.alert))
                raise
        if i >= _max: break
        i += 1

def parse_feeds(feed_abbrs):
    for feed_abbr in feed_abbrs:
        print '*'*20,feed_abbr.upper()
        url = CAP_FEED_URL_TMPL % locals()
        parse_feed(feedparser.parse(url), url)

parse_feeds(feeds)