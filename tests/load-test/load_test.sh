#!/bin/bash
# Load Test: Flood order-service to trigger HPA
# Kịch bản: Gửi liên tiếp các yêu cầu POST tới order-service để tăng tải CPU, kích hoạt Auto-scaling.

URL=${1:-"http://localhost:3000/orders"}
DURATION=${2:-60} # Giây

echo "--- Bắt đầu Load Test tới: $URL (Trong $DURATION giây) ---"
echo "Kế hoạch: Tạo tải để kích hoạt HPA (Horizontal Pod Autoscaler)."

END_TIME=$((SECONDS + DURATION))

while [ $SECONDS -lt $END_TIME ]; do
  # Gửi request ẩn đi output
  curl -s -X POST $URL > /dev/null &
  sleep 0.1
done

echo "--- Đã gửi xong các yêu cầu. Chờ HPA cập nhật (có thể mất 1-2 phút) ---"
echo "Mẹo: Chạy lệnh 'kubectl get hpa -w' để theo dõi quá trình co giãn."
