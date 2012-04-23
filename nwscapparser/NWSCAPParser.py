from xml2obj import xml2obj
import ast
import json
import re

# used to clean the alert description field by removing multiple spaces
R1 = re.compile(r"^\s{2,}", re.MULTILINE)

class NWSCAPParser:
    def __init__(self, raw_cap_xml, cap_url=None):
        self.xml = raw_cap_xml
        self.url = cap_url
        self.load()
    def load(self):
        self.alert = xml2obj(self.xml)
        self.FIPS6 = []
        [self.FIPS6.append(g.value) for g in self.alert.info.area.geocode if g.valueName.upper() == 'FIPS6']
        self.UGC = []
        [self.UGC.append(g.value) for g in self.alert.info.area.geocode if g.valueName.upper() == 'UGC']
        self.INFO_PARAMS = {}
        [self.INFO_PARAMS.update({p.valueName:p.value}) for p in self.alert.info.parameter]
    def get_clean_text(self, raw_text):
        return R1.sub(" ", raw_text.strip()).replace('\n',' ') 
    def get_clean_description(self):
        return self.get_clean_text(self.alert.info.description)
    def get_clean_instruction(self):
        return self.get_clean_text(self.alert.info.instruction)
    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return getattr(self.alert, name)
    def as_dict(self):
        return ast.literal_eval(repr(self.alert))
    def as_json(self):
        return json.dumps(self.as_dict())
    def __repr__(self):
        return '<NWSCAPParser.NWSCAPParser instance (identifier:%s)>' % self.identifier



