#!/bin/bash
# Failure Simulation Script: Kill random pods
SERVICE=$1
if [ -z "$SERVICE" ]; then
  echo "Usage: ./kill-pod.sh <service-name>"
  exit 1
fi

echo "Simulating failure for $SERVICE..."
kubectl delete pod -l app=$SERVICE --now
echo "Pod killed. Kubernetes should recreate it automatically (Self-healing)."
