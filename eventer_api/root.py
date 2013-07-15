from txrestapi.resource import APIResource
from txrestapi.methods import GET, POST, PUT, ALL
import json

import events

class EventerApi(APIResource):

    @ALL('^/ping')    
    def ping(self, request):
        return json.dumps({'status': 'ok'})

    @POST('^/events')
    def save_event(self, request):
        content = request.content.read()
        content = json.loads(content)

        app_id = content['app_id']
        event_id = content['event_id']
        event_properties = content['event_properties']
        events.save_event(app_id, event_id, event_properties)
        return json.dumps({'status': 'ok'})