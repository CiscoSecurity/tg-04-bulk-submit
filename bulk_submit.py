import os
import sys
import requests

# Validate a parameter was provided as an argument
if len(sys.argv) < 2:
    sys.exit('Usage:\n %s sample' % sys.argv[0])

inputParam = sys.argv[1]
inputStr = '{}'.format(inputParam)
inputFiles = []

# Check if the supplied parameter is a directory
if os.path.isdir(inputParam):
    print 'You have supplied a directory'
    for (dirpath, dirnames,filenames) in os.walk(inputStr):
        for file in filenames:
            filePath = '{}/{}'.format(dirpath,file)
            inputFiles.append(filePath)

# If the supplied parameter is a file validate it exists
if not os.path.exists(inputParam):
    sys.exit ('File %s doesn\'t exist' % inputParam)

# Append the filename to inputfiles
if not os.path.isdir(inputParam):
    inputFiles.append(inputParam)

url = 'https://panacea.threatgrid.com/api/v2/samples'
api_key = 'asdf1234asdf1234asdf1234'
formData = {'api_key': api_key, 'private': 'true', 'vm':'win7-x64', 'email_notification':'False'}
number_of_files = len(inputFiles)
times_to_submit = 5
time_submitted = 0


if number_of_files is 1:
	print 'Submitting {} {} times'.format(inputFiles[0],times_to_submit)
	while time_submitted < times_to_submit:
		sample = {'sample': open(inputFiles[0], 'rb')}
		r = requests.post(url, files=sample, data=formData, verify=True)
		response = r.json()
		sample_id = response['data']['id']
		print sample_id
		time_submitted += 1

if number_of_files > 1:
	print 'Will submit the following files:'
	for file in inputFiles:
	    print '   {}'.format(file)
	print '\r'
	for file in inputFiles:
		sample = {'sample': open(file, 'rb')}
		r = requests.post(url, files=sample, data=formData, verify=True)
		response = r.json()
		sample_id = response['data']['id']
		print file,sample_id
