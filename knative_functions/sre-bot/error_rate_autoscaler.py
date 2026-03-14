import json
import requests

def handle(req):
    """
    Knative Circuit Breaker Scaler
    Monitors error rates and triggers 'Scale-to-Zero' if the system is unhealthy.
    """
    # Simulate fetching error rate from Prometheus
    error_rate = 0.25  # Mock: 25% error rate detected
    threshold = 0.20

    if error_rate > threshold:
        print(f"Knative-SRE: CRITICAL ERROR RATE ({error_rate*100}%).")
        print("Knative-SRE: Triggering Emergency Scale-to-Zero to protect DB.")
        
        # Action: Call K8s API or Knative Service API to set replicas to 0
        action = "scale_to_zero_initiated"
    else:
        action = "monitoring"

    return json.dumps({
        "status": "success",
        "current_error_rate": error_rate,
        "action_taken": action,
        "engine": "Knative-Eventing"
    })
