#!/bin/bash

URL=${1:-"http://localhost:80/order"}
COUNT=${2:-10}

echo "[LATENCY] Checking $URL ($COUNT reqs)"

for i in $(seq 1 $COUNT)
do
  TIME=$(curl -o /dev/null -s -w '%{time_total}\n' -X POST $URL)
  echo "$i: ${TIME}s"
  sleep 0.5
done
