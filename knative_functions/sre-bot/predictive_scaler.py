import json
import os
from kubernetes import client, config

def handle(req):
    """
    Knative Predictive Autoscaler
    Triggers based on 'OrderCreated' events to scale 'payment-service' 
    proactively before the payment request hit.
    """
    try:
        data = json.loads(req)
        order_id = data.get("order_id")
        amount = data.get("amount")
        
        print(f"Knative-Scaler: High-value order detected ({order_id}, ${amount}).")
        print(f"Knative-Scaler: Proactively scaling 'payment-service' replicas up by 2.")

        # In a real K8s environment:
        # config.load_incluster_config()
        # apps_v1 = client.AppsV1Api()
        # deployment = apps_v1.read_namespaced_deployment_scale("payment-service", "default")
        # deployment.spec.replicas += 2
        # apps_v1.replace_namespaced_deployment_scale("payment-service", "default", deployment)

        return json.dumps({
            "status": "proactive_scaling_triggered",
            "target": "payment-service",
            "reason": f"Anticipating payment for order {order_id}"
        })
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})
