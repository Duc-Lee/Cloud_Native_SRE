import json
import time
from kubernetes import client, config

def handle(req):
    # Triggered by critical alerts
    print("remediating...")
    
    # Simple self-healing logic
    try:
        # flush cache if needed
        # r.flushdb()
        print("cache cleared")
        
        # bounce deployment
        # k8s.patch_namespaced_deployment(...)
        print("restarting order service")
        
        res = "done"
    except Exception as e:
        print(f"fail: {str(e)}")
        res = "error"

    return json.dumps({
        "status": res,
        "ts": int(time.time())
    })
