import os
import sys
import requests

# Validate a parameter was provided as an argument
if len(sys.argv) < 2:
    sys.exit('Usage:\n %s sample' % sys.argv[0])

input_param = sys.argv[1]
input_files = []

# Check if the supplied parameter is a directory
if os.path.isdir(input_param):
    print('You have supplied a directory')
    for (dirpath, dirnames, filenames) in os.walk(input_param):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            input_files.append(file_path)
else:
    # Append the provided parameter to input_files
    input_files.append(input_param)

# If the supplied parameter is a file validate it exists
if not os.path.exists(input_param):
    sys.exit('File {} doesn\'t exist'.format(input_param))

url = 'https://panacea.threatgrid.com/api/v2/samples'
tg_api_key = 'asdf1234asdf1234asdf1234'
form_data = {'api_key': tg_api_key, 'private': 'true'}
number_of_files = len(input_files)
times_to_submit = 1
submitted_count = 0

if number_of_files == 1:
    if times_to_submit == 1:
        print('Submitting {} once'.format(input_files[0]))
    if times_to_submit > 1:
        print('Submitting {} {} times'.format(input_files[0], times_to_submit))
    while submitted_count < times_to_submit:
        sample = {'sample': open(input_files[0], 'rb')}
        request = requests.post(url, files=sample, data=form_data, verify=True)
        response = request.json()
        sample_id = response['data']['id']
        print(sample_id)
        submitted_count += 1

if number_of_files > 1:
    print('Will submit the following files:')
    for file in input_files:
        print('   {}'.format(file))
    print('\r')
    for file in input_files:
        sample = {'sample': open(file, 'rb')}
        request = requests.post(url, files=sample, data=form_data, verify=True)
        response = request.json()
        sample_id = response['data']['id']
        print(file, sample_id)
