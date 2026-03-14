#!/bin/bash
# Latency Test: Measure response times of the shared
# Kịch bản: Đo thời gian phản hồi của Gateway để kiểm tra SLO (Service Level Objectives).

URL=${1:-"http://localhost:80/orders"} # Target Kong Gateway
COUNT=${2:-10}

echo "--- Bắt đầu Latency Test tới: $URL ---"

for i in $(seq 1 $COUNT)
do
  RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}\n' -X POST $URL)
  echo ">>> [Request $i] Time: ${RESPONSE_TIME}s"
  sleep 0.5
done

echo "--- Latency Test Hoàn Tất ---"
