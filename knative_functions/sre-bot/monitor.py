import json
import time

def handle(req):
    # monitor error rates
    err_rate = 0.35 
    
    if err_rate > 0.3:
        print(f"high error rate ({err_rate}) - locking down")
        state = "OPEN"
    else:
        state = "CLOSED"
    
    return json.dumps({
        "circuit": state,
        "rate": err_rate,
        "updated": int(time.time())
    })
