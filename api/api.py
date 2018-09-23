#!/usr/bin/env python3

import urllib2
import json

local_api = 'asdefws3wdfresdeerffsslkmsdksml'

def api_search(query):
    api_key = local_api
    url = 'https://api.locy.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for item in data['objects']:
        print item['name'], item['phone']
