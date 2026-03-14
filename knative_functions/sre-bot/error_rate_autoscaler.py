import json

def handle(req):
    error_rate = 0.25 # Mock
    threshold = 0.20

    if error_rate > threshold:
        # Emergency scale-to-zero logic would go here
        action = "scale_to_zero"
    else:
        action = "monitor"

    return json.dumps({
        "status": "ok",
        "rate": error_rate,
        "action": action,
        "engine": "Knative"
    })
