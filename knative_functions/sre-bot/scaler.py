import json

def handle(req):
    try:
        # Expecting JSON payload from 'OrderCreated' event
        data = json.loads(req)
        order_id = data.get("order_id", "unknown")
        amount = float(data.get("amount", 0))
        
        print(f"[SCALER] Order {order_id} received. Amount: ${amount}")
        
        if amount > 500:
            # VIP Scaling: Proactively scale payment service up
            print(f"[VIP] High order value detected. Scaling 'payment' replicas -> 5")
            action = "priority_scale_up"
            target_replicas = 5
        else:
            print("[SCALER] Standard order. No extra scaling needed.")
            action = "none"
            target_replicas = 1

        return json.dumps({
            "status": "processed",
            "order": order_id,
            "action": action,
            "target": "payment",
            "replicas": target_replicas
        })
    except Exception as e:
        return json.dumps({"status": "error", "msg": str(e)})
