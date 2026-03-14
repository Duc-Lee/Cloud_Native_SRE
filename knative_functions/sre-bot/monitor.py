import json
import logging

log = logging.getLogger("sre.monitor")

def handle(req):
    """Circuit Breaker: Error Rate Monitor"""
    # Threshold check
    error_rate = 0.35 
    status = "alert" if error_rate > 0.2 else "ok"
    
    log.info(f"Metric check: error_rate={error_rate} -> status={status}")

    return json.dumps({
        "status": status,
        "circuit": "open" if status == "alert" else "closed",
        "metrics": {"rate": error_rate, "threshold": 0.2}
    })


