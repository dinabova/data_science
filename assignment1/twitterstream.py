import oauth2 as oauth
#import urllib.request as urllib # this is for python versions 2.7.8 and up
import urllib2 as urllib


# See assignment1.html instructions or README for how to get these credentials

api_key = "YXIv0VNdVqleDmhRgpaYn2mYY"
api_secret = "mM1i1V5h6tuOC68fkOxqcl6seLpfW7ZwnlUgMg8xrO3DUABMvY"
access_token_key = "730322637025595393-qgFicNcpg5fMjjPoIlOEVkcWsLcWVkZ"
access_token_secret = "NzqCdK5xrmendnECCO9hGlrDpO67mhrroa7HA77L41rZk"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"
# other methods https://dev.twitter.com/rest/reference/get/search/tweets



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
  url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en" # get statuses on english
  # to search for the term "microsoft", you can pass the following url to the twitterreq function:https://api.twitter.com/1.1/search/tweets.json?q=microsoft
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"

  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print(line.strip())

if __name__ == '__main__':
  fetchsamples()
