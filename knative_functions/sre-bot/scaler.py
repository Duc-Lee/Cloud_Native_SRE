import json

def handle(req):
    try:
        data = json.loads(req)
        order_id = data.get("order_id")
        
        # Proactively scale payment service
        return json.dumps({
            "status": "scaling_triggered",
            "target": "payment",
            "reason": f"Order {order_id}"
        })
    except:
        return json.dumps({"status": "error"})
