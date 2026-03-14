#!/bin/bash

NAMESPACE=${1:-default}
echo "[CHAOS] Testing namespace: $NAMESPACE"

for i in {1..3}
do
  POD=$(kubectl get pods -n $NAMESPACE -l "app" -o jsonpath='{.items[0].metadata.name}' 2>/dev/null)
  if [ -z "$POD" ]; then
    echo "err: no pods"
    exit 1
  fi 
  echo "kill -> $POD"
  kubectl delete pod $POD -n $NAMESPACE --now >/dev/null
  sleep 10
  READY=$(kubectl get pods -n $NAMESPACE -l "app" | grep -v NAME | grep "Running" | wc -l)
  echo "$READY pods up"
done
