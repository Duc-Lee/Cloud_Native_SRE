import json
import logging

log = logging.getLogger("viettel.sre.monitor")

def handle(req):
    print("Checking monitor...")
    # ti le loi 
    rate = 0.35 

    if rate > 0.2:
        print("NGUY HIEM: error rate cao qua!")
        return '{"status": "alert", "circuit": "open"}'
    else:
        print("Van on...")
        return '{"status": "ok", "circuit": "closed"}'


