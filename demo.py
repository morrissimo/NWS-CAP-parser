import sys
import urllib2
from pprint import pprint

from nwscapparser import NWSCAPParser


def test_basic_fields(alert):
    print '---- basic fields ----'
    print alert.identifier
    print alert.info.effective
    print '%d FIPS6 codes:'%len(alert.FIPS6), alert.FIPS6
    print '%d UGC codes:'%len(alert.UGC), alert.UGC
    print '%d INFO_PARAMS:'%len(alert.INFO_PARAMS), alert.INFO_PARAMS


def test_dict_dump(alert):
    print '---- dict dump ----'
    pprint(alert.as_dict())


def test_json_dump(alert):
    print '---- json dump ----'
    pprint(alert.as_json())


if __name__=='__main__':
    # first command line arg is assumed to be a full URL to a CAP
    if len(sys.argv) > 1:
        cap_url = sys.argv[1]
        response = urllib2.urlopen(cap_url)
        src = response.read()
    # testing
    else:
        fn = r'cap.IL124CA04A2F50.SevereThunderstormWarning.xml'
        with open(fn,'r') as f:
            src = f.read()
    alert = NWSCAPParser(src)
    print alert
    test_basic_fields(alert)
    test_dict_dump(alert)
    test_json_dump(alert)

