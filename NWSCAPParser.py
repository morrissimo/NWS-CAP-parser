from xml2obj import xml2obj
from pprint import pprint
import ast
import json
import re

# used to clean the alert description field by removing multiple spaces
R1 = re.compile(r"^\s{2,}", re.MULTILINE)

class NWSCAPParser:
    FIPS6 = []
    UGC = []
    INFO_PARAMS = {}
    def __init__(self, raw_cap_xml):
        self.xml = raw_cap_xml
        self.alert = xml2obj(raw_cap_xml)
        self.load_fips6()
        self.load_ugc()
        self.load_info_params()
    def load_fips6(self):
        [self.FIPS6.append(g.value) for g in self.alert.info.area.geocode if g.valueName.upper() == 'FIPS6']
    def load_ugc(self):
        [self.UGC.append(g.value) for g in self.alert.info.area.geocode if g.valueName.upper() == 'UGC']
    def load_info_params(self):
        [self.INFO_PARAMS.update({p.valueName:p.value}) for p in self.alert.info.parameter]
    def get_clean_description(self):
        return R1.sub(" ", self.alert.info.description.strip()).replace('\n','')
    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return getattr(self.alert, name)
    def as_dict(self):
        return ast.literal_eval(repr(self.alert))
    def as_json(self):
        return json.dumps(self.as_dict())

def test_basic_fields(alert):
    print '---- basic fields ----'
    print alert.identifier
    print alert.info.effective
    print alert.FIPS6
    print alert.UGC
    print alert.INFO_PARAMS

def test_dict_dump(alert):
    print '---- dict dump ----'
    pprint(alert.as_dict())

def test_json_dump(alert):
    print '---- json dump ----'
    pprint(alert.as_json())

def test_clean_desc(alert):
    print '---- get_clean_description ----'
    print repr(alert.get_clean_description())

if __name__=='__main__':
    fn = r'cap.GA124CA04A0C28.xml'
    with open(fn,'r') as f:
        src = f.read()
    alert = NWSCAPParser(src)
    test_basic_fields(alert)
    test_dict_dump(alert)
    test_json_dump(alert)
    test_clean_desc(alert)
