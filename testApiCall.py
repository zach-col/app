import requests
import json
import time

headers = {
    'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
    'Content-Type': 'application/json',
}
# submit audio file
data = '{"media_url":"http://www.wavsource.com/snds_2018-06-03_5106726768923853/people/famous/king_injustice.wav","metadata":"This is a sample submit jobs option"}'
response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, data=data).json()
print ("got the id", response['id'])
jobId = response['id']

headers = {
    'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
}

while (response['status'] != 'transcribed'):
    response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+ jobId, headers=headers).json()
    print (response['status'])
    time.sleep(0.1)

# gets audio file text
headers = {
    'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
    'Accept': 'text/plain',
}
response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+ jobId +'/transcript', headers=headers).json()

print (response)

