import json
import sys
import os

# Add the function directory to sys.path
sys.path.append(os.path.join(os.getcwd(), 'knative_functions', 'sre-bot'))

import app
import scaler
import monitor

def test_app():
    resp = app.handle(json.dumps({"action": "test"}))
    data = json.loads(resp)
    assert data["status"] == "success"
    assert "executed" in data
    print("Standard request: PASS")

def test_scaler():
    resp = scaler.handle(json.dumps({"amount": 100}))
    data = json.loads(resp)
    assert data["op"] == "skip"
    print("Below threshold: PASS")
    resp = scaler.handle(json.dumps({"amount": 1000}))
    data = json.loads(resp)
    assert data["action"] == "scale"
    assert data["replicas"] == 10
    print("Above threshold: PASS")

def test_monitor():
    resp = monitor.handle("")
    data = json.loads(resp)
    assert data["status"] == "alert"
    assert data["circuit"] == "open"
    print("Alert condition: PASS")

if __name__ == "__main__":
    test_app()
    test_scaler()
    test_monitor()
    print("\nVerification: DONE")

