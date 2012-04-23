# NWS CAP Parser

A Python module to make parsing National Weather Service (NWS) alerts simple.

##  Common Alerting Protocol (CAP)

The NWS publishes weather alerts and advisories in the CAP format via Atom feeds. More information - and a 
full list of US feeds - can be found on the NWS CAP [home page](http://alerts.weather.gov/).

## Module Details

### NWSCAPParser

The nwscapparser module exports a single class, `NWSCAPParser`. Pass a string containing the
XML from a CAP alert as the only param to the initialization call:
```python
from nwscapparser import NWSCAPParser
f = r'cap.IL124CA04A2F50.SevereThunderstormWarning.xml'	# included (actual) alert
src = open(f,'r').read()
alert = NWSCAPParser(src)
```

Of note, the instance exposes the FIPS6 county codes (also known as SAME codes) that the alert references, so that affected 
counties may be more easily referenced. See the demo file `demo.py` for complete examples of the methods and fields 
available in a `NWSCAPParser` instance.

### us_states

The module also exports a dictionary `us_states` with keys that are two-letter US state abbreviations and values 
that are full state names, to aid in iterating through the feeds offered by the NWS, which are published by state 
abbreviations. For example, the CAP feed for Arizona (AZ) can be accessed at the URL `http://alerts.weather.gov/cap/az.php?x=1`.
