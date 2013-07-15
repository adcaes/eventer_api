from twisted.web.server import Site
from twisted.internet import reactor
from twisted.python import log

import sys
import root

def start():
    the_api = root.EventerApi()
    site = Site(the_api, timeout=None)
    reactor.listenTCP(8080, site)

log.startLogging(sys.stdout)
start()
reactor.run()
