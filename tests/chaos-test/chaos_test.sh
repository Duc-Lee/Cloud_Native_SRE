#!/bin/bash
# Chaos Test: Randomly kill pods to verify Self-healing
# Kịch bản: Xóa ngẫu nhiên các pod để xem K8s có tự khởi động lại (Self-healing) hay không.

NAMESPACE=${1:-default}
echo "--- Bắt đầu Chaos Test trên Namespace: $NAMESPACE ---"

for i in {1..5}
do
  POD=$(kubectl get pods -n $NAMESPACE -l "app" -o jsonpath='{.items[0].metadata.name}')
  if [ -z "$POD" ]; then
    echo "Không tìm thấy pod nào để xóa."
    exit 1
  fi
  
  echo ">>> [$(date)] Đang xóa Pod: $POD"
  kubectl delete pod $POD -n $NAMESPACE --now
  
  echo "Chờ 10 giây để K8s tự phục hồi..."
  sleep 10
  
  READY=$(kubectl get pods -n $NAMESPACE -l "app" | grep -v NAME | grep "Running" | wc -l)
  echo "Số lượng Pod đang chạy: $READY"
done

echo "--- Chaos Test Hoàn Tất ---"
