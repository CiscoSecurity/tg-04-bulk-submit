[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Threat Grid Bulk Submit:
Easily submit files to Threat Grid via the API. A directory of files or a single file may be supplied as a command line argument. 

When submitting a direcotry everything, including files in sub-directories, will be submitted. The file name and associated sample ID will be printed to the console.

When submiting a file, the default is to submit the file one time. Changing the times_to_submit variable to 5 will result files being submitted 5 times. The sample IDs of the submissions will be printed to the console.

### Before using you must update the following:
- tg_api_key

If you want to submit an individual file more than once
- times_to_submit 

### Usage:
To submit a file:
```
python bulk_submit.py PO58923.pdf
```

To submit files in a directory:
```
python bulk_submit.py Samples
```

### Example script output:
Output when submitting a file:
```
Submitting PO58923.pdf once
3cee093d98a4aadc13de18c24ce6df03
```
Output when submitting a directory:
```
You have supplied a directory
Will submit the following files:
   Samples\attachment.zip
   Samples\Not_A_Virus.exe
   Samples\PO58923.pdf
   Samples\MoreSamples\00c5014631aa95c6ca453ec2453aed3fad5bca04d4f08ec6f3d259f16d090ad8
   Samples\MoreSamples\01ddf47d2013e56022e58433081aa11ae8871e1ac698e1dafdb4242f08b4281b
   Samples\MoreSamples\7c9f50fb47d205fea9422af09a1218342a8b0cfbf4435d9cd808fb530af4b23b

Samples\attachment.zip b664d1d0d2f0ab1db1a8f3e361bd911a
Samples\Not_A_Virus.exe f4cdad31f143a85f8d3468f151263597
Samples\PO58923.pdf.exe 313bcf290e52557c76a87bb6d587dfe0
Samples\MoreSamples\00c5014631aa95c6ca453ec2453aed3fad5bca04d4f08ec6f3d259f16d090ad8 597674741de491405372b304b04af665
Samples\MoreSamples\01ddf47d2013e56022e58433081aa11ae8871e1ac698e1dafdb4242f08b4281b b3b07306c909f87e7996f203bf0a0796
Samples\MoreSamples\7c9f50fb47d205fea9422af09a1218342a8b0cfbf4435d9cd808fb530af4b23b 0eec9a2b8d2b4a0c477348ac62945854
```
