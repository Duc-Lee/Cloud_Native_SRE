import json
import logging

log = logging.getLogger("viettel.sre.scaler")

def handle(req):
    # Dynamic scaling for payment service during bursty traffic
    data = json.loads(req or '{}')
    val = float(data.get("amount") or 0)
    
    if val < 500:
        return json.dumps({"op": "skip", "val": val})

    log.info(f"Scaling required: value={val} -> target=payment")
    return json.dumps({
        "action": "scale", 
        "service": "payment",
        "replicas": 5 if val < 1000 else 10,
        "reason": "high_value_order"
    })


