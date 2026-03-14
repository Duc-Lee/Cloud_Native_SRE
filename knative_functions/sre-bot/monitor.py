import json
import time

def check_circuit_status(error_rate):
    # Logic to evaluate if we should "open" the circuit
    if error_rate > 0.30:
        print(f"[CIRCUIT] Critical Error Rate: {error_rate*100}%. OPENING CIRCUIT.")
        # Logic to update Nginx ConfigMap to stop traffic or return 503
        return "OPEN"
    return "CLOSED"

def handle(req):
    # Simulate reading error rate from Prometheus metrics
    mock_error_rate = 0.35 
    
    status = check_circuit_status(mock_error_rate)
    
    return json.dumps({
        "circuit_status": status,
        "observed_error_percent": mock_error_rate * 100,
        "action": "lockdown_initiated" if status == "OPEN" else "monitoring",
        "timestamp": int(time.time()),
        "engine": "Knative-Circuit-Breaker"
    })
