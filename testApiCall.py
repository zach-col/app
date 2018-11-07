import requests
import json


headers = {
    'Authorization': 'Bearer put_api_key_here',
    'Content-Type': 'application/json',
}
# submit audio file
data = '{"media_url":"http://www.wavsource.com/snds_2018-06-03_5106726768923853/people/famous/king_injustice.wav","metadata":"This is a sample submit jobs option"}'
response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, data=data).json()
print "got the id", response['id']


headers = {
    'Authorization': 'Bearer put_api_key_here',
}
response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/' + response['id'], headers=headers).json()

print response


# gets audio file text
#newHeaders = {
#    'Authorization': 'Bearer 01lmbrBli3wfUkywmTkQHX24P-EYBS3dd_m-eyBTZ2lGpKHvm29VlDO7zX123ciVqaNfmcaE6iUlzTw38-6QeQzDcvqVM',
#    'Accept': 'text/plain',
#}
#newResponse = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/%7Bid%7D/transcript', headers=headers)
#response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/%3Cinsert%20job%20id%20here%3E', headers=headers)


