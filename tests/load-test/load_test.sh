#!/bin/bash

URL=${1:-"http://localhost:80/order"}
DURATION=${2:-60}

echo "[LOAD] Hitting $URL for ${DURATION}s"

END_TIME=$((SECONDS + DURATION))

while [ $SECONDS -lt $END_TIME ]; do
  curl -s -X POST $URL > /dev/null &
  sleep 0.1
done

echo "Done. Watch HPA: kubectl get hpa -w"
