# 🛠️ Makefile for Cloud SRE Platform

.PHONY: deploy-k8s deploy-knative load-test clean help

help:
	@echo "Sử dụng các lệnh sau:"
	@echo "  make deploy-k8s     - Triển khai toàn bộ K8s Manifests"
	@echo "  make deploy-knative - Triển khai Knative Service"
	@echo "  make load-test      - Chạy thử nghiệm tải (10 requests)"
	@echo "  make clean          - Xoá toàn bộ tài nguyên đã triển khai"

deploy-k8s:
	kubectl apply -f deploy/kubernetes/

deploy-knative:
	kubectl apply -f deploy/kubernetes/knative-service.yaml

load-test:
	bash tests/load-test/load_test.sh http://localhost:80/orders 10

clean:
	kubectl delete -f deploy/kubernetes/
	kubectl delete -f deploy/kubernetes/knative-service.yaml
