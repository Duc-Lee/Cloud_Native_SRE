#!/bin/bash
# Pod deletion chaos test

NAMESPACE=${1:-default}
echo "Starting chaos test in namespace: $NAMESPACE"

for i in {1..3}
do
  # Target a random pod from our services
  POD=$(kubectl get pods -n $NAMESPACE -l "app" -o jsonpath='{.items[0].metadata.name}')
  
  if [ -z "$POD" ]; then
    echo "No pods found."
    exit 1
  fi
  
  echo "[$(date)] Killing pod: $POD"
  kubectl delete pod $POD -n $NAMESPACE --now
  
  sleep 10
  
  READY=$(kubectl get pods -n $NAMESPACE -l "app" | grep -v NAME | grep "Running" | wc -l)
  echo "Pods currently running: $READY"
done
