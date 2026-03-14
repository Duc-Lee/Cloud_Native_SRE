#!/bin/bash
# Latency test for SLO validation

URL=${1:-"http://localhost:80/order"}
COUNT=${2:-10}

echo "Testing latency on $URL ($COUNT requests)"

for i in $(seq 1 $COUNT)
do
  RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}\n' -X POST $URL)
  echo "[Request $i] Latency: ${RESPONSE_TIME}s"
  sleep 0.5
done
