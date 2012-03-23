from xml2obj import xml2obj
from pprint import pprint

class NWSCAPParser:
    FIPS6 = []
    UGC = []
    INFO_PARAMS = {}
    def __init__(self, raw_cap_xml):
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

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return getattr(self.alert, name)

def test():
    with open(r'cap.GA124CA04A0C28.SpecialWeatherStatement.124CA04A16B4GA.FFCSPSFFC.4bac84c809ce6019c69db271dfee28ad.xml','r') as f:
        src = f.read()
        alert = NWSCAPParser(src)
        print alert.identifier
        print alert.info.effective
        print alert.FIPS6
        print alert.UGC
        print alert.INFO_PARAMS

if __name__=='__main__':
    test()
