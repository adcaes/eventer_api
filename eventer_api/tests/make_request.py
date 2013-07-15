from twisted.web.server import Request
from twisted.web.server import Site
from datetime import datetime
import json
from StringIO import StringIO

import eventer_api.root as root

the_api = root.EventerApi()
site = Site(the_api, timeout=None)

class FakeChannel(object):
    transport = None

def makeRequest(method, path, post_data=None):
    req = Request(FakeChannel(), None)
    req.prepath = req.postpath = None
    req.method = method
    req.path = path
    req.content = StringIO(post_data)
    resource = site.getChildWithDefault(path, req)
    return resource.render(req)



TESTDATA = {'app_id': 'test_app', 'event_id': 'test_event', 'event_properties': {'version': 1234, 'updated': str(datetime.now())}}
URL = 'http://localhost:8880/form'


print makeRequest('POST', '/events', json.dumps(TESTDATA))