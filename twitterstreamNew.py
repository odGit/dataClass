import oauth2 as oauth
import urllib2 as urllib
import json

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "127361574-4NzT9EG8thjoo6JbsAo4h2JQk7Bm8a5vTb93HuMc"
access_token_secret = "eUyNEDYNL6KulrTN5vprfyfLp6z15p5lWhaZX8CdKw"

consumer_key = "86hZkJi6ocP4Revbcde4A"
consumer_secret = "WQZO94FwsTVvz8VF0y7CCjmvj7Z9bnVXfJdeGNGRI"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  return json.load(response)
#  for line in response:
#    print line.strip()

#if __name__ == '__main__':
#   fetchsamples()

myResults = fetchsamples()
print type(myResults)


