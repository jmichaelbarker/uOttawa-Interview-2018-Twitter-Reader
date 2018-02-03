from TwitterAPI import TwitterAPI
from collections import OrderedDict
import urllib.request
import json

# Get CSV from URL
with urllib.request.urlopen('https://wipebook.org/vnps.csv') as response:
	content = response.read()

# Split CSV into array of bytestrings, remove final carriage return
users = content.split(b'\r\n,')
users[-1] = users[-1].replace(b'\r\n', b'')

# Remove first user listing (b'0')
users.pop(0)

# Set up TwitterAPI object
api = TwitterAPI("pCDkwTJMC1BNaf2WqjMAlXzrF", "nfkMbXlH3SUt8Y3exNFeTCBqD2DLqm5tbNF6TA4nLTDe9UlI4q", "3134136299-WW8pMs3Fa2rcvB4AyxA1rN0THlRXP0w5YDhga9A", "t7W3DLPCq5VschssqvAk6dbyTwSnk5xdfJ5iQuW9sSarX")

api_responses = {}

users = users[len(users)-10:] # Testing (due to API limit)

# Iterate over users, make API call on user, parse JSON response to python3 dict and add 'followers_count' key to API responses dict
for user in users:
	api_responses[user] = json.loads(api.request('users/show', {'screen_name':user}).text).get('followers_count')

# Sort dictionary to list of tuples
sorted_followers = [(k, api_responses[k]) for k in sorted(api_responses, key=api_responses.get, reverse=True)]

# Print usernames and followers
for user in sorted_followers:
	print(user[0].decode("utf-8") + ":", user[1])