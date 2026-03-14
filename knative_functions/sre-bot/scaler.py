import json

def handle(req):
    try:
        event = json.loads(req)
        val = float(event.get("amount", 0))
        
        print(f"evaluating order: {val}")
        
        # scale based on load anticipation
        if val > 500:
            print("scaling up payment service (vip)")
            replicas = 5
        else:
            replicas = 1

        return json.dumps({
            "target": "payment",
            "scale": replicas
        })
    except:
        return json.dumps({"err": "invalid payload"})
