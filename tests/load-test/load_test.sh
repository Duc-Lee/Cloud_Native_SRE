#!/bin/bash
# Simple load generator for HPA testing

URL=${1:-"http://localhost:80/order"}
DURATION=${2:-60}

echo "Generating load on $URL for $DURATION seconds"

END_TIME=$((SECONDS + DURATION))

while [ $SECONDS -lt $END_TIME ]; do
  curl -s -X POST $URL > /dev/null &
  sleep 0.1
done

echo "Load test complete. Check HPA status with: kubectl get hpa"
