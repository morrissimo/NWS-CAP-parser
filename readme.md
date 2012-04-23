# NWS CAP Parser

A lightweight Python module to make parsing National Weather Service (NWS) alerts easy.

##  Common Alerting Protocol (CAP)

The NWS publishes weather alerts and advisories in the CAP format via Atom feeds. More information - and a 
full list of US feeds - can be found on the NWS CAP [home page](http://alerts.weather.gov/).

## NWSCAPParser

The nwscapparser module exports a single class, NWSCAPParser. To use this class, pass a string containing the
XML from a CAP alert as the only param to the initialization call:
```python
fn = r'cap.IL124CA04A2F50.SevereThunderstormWarning.xml'	# included (actual) alert
src = open(fn,'r').read()
alert = NWSCAPParser(src)
```

See the demo file `demo.py` for more examples of the methods and fields available in a parsed alert instance.
