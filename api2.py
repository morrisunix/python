from urllib.request import urlopen
import urllib
import json


rax_user = 'morrisunix'
rax_api = '2cedf77d21b1d0f577f0f54fdd408df5'

def api_search():
    api_key = rax_api
    post_params = {
            "auth":{"RAX-KSKEY:apiKeyCredentials":{"username":"' + rax_user + '","apiKey":"' + rax_api '"}}
            }
    url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'
#    params = urllib.urlencode(post_params)
    response = urlopen(url, post_params)
    data = json.load(response.read())
    response = urlopen("http://www.google.com/")
    print(response.read())

#    for item in data['serviceCatalog']:
#        print item
#        print item['name'], item['phone']

api_search()
