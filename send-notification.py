#!/usr/bin/python

# JSON & requests
import requests
import json

# add argument handling
from sys import argv
script, message = argv

#urllib for encoding
import urllib

# Production credentials
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
username = 'USERNAME'
password = 'PASSWORD'

# URLs
oauth2_url = 'https://auth.psft.co'
pmp_url = 'https://pmp.psft.co'
token_url = oauth2_url + '/oauth/token'

# Build request for token.
data =  urllib.urlencode({ 'grant_type' : 'password', 'client_id' : client_id, 
'client_secret' : client_secret , 'username' : username,  
'password' : password })

# Make request for access token
r = requests.post(token_url, data = data, headers = {'Content-Type' : 'application/x-www-form-urlencoded' } )
access_token = str(json.loads(r.content).get('access_token'))

# get ID of user.
r = requests.get(pmp_url + '/api/v2/users/current', headers = {'Authorization' : 'Bearer ' + access_token } )
user_id = str(json.loads(r.content).get('user').get('id'))

# Create notification URL & content
notification_url = pmp_url + '/api/v2/users/' + user_id + '/notifications?access_token=' + access_token
data = json.dumps({
	'content_id' : 'CONTENT_ID', 
	'message' : message
})

# Send notification to username specified above
r = requests.post( notification_url , data = data, headers = {'Content-Type' : 'application/json'} )
print r