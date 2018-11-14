[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Threat Grid Bulk Submit

Easily Submit Files to Threat Grid via the API. Can submit a directory full of files or it can be configured to submit the same file multiple times.

### Before using you must update the following:
- Line 30: api_key 

If you want to submit an individual file more than once
- Line 33: times_to_submit 

### Usage

To submit a file:
```
python bulk_submit.py file.exe
```

To submit files in a directory:
```
python bulk_submit.py directory
```
