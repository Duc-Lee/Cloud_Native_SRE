# --- Viettel Cloud Native SRE (CN-SRE) ---
# Project: cloud-native-sre
# Author: SRE Team <sre-team@viettel.com.vn>

# Image versioning
VERSION=$(shell git rev-parse --short HEAD 2>/dev/null || echo "v1")
REGISTRY=viettel-registry.local

# Main targets
all: build deploy

# Building microservices
build:
	@echo ">> Build version: $(VERSION)"
	docker build -t $(REGISTRY)/auth:$(VERSION) services/auth
	docker build -t $(REGISTRY)/cart:$(VERSION) services/cart
	docker build -t $(REGISTRY)/notification:$(VERSION) services/notification
	docker build -t $(REGISTRY)/order:$(VERSION) services/order
	docker build -t $(REGISTRY)/payment:$(VERSION) services/payment
	docker build -t $(REGISTRY)/product:$(VERSION) services/product
	docker build -t $(REGISTRY)/user:$(VERSION) services/user
	docker build -t $(REGISTRY)/sre-bot:$(VERSION) knative_functions/sre-bot

# K8s deployment
deploy:
	kubectl apply -f deploy/kubernetes/
	kubectl apply -f deploy/kubernetes/knative-service.yaml

# Simulator for SRE testing
test-bot:
	export PYTHONPATH="knative_functions/sre-bot" && python tests/simulator_sre.py

# Cleanup
clean:
	kubectl delete -f deploy/kubernetes/ --ignore-not-found
	kubectl delete -f deploy/kubernetes/knative-service.yaml --ignore-not-found

help:
	@echo "Viettel SRE Platform"
	@echo "--------------------"
	@echo "make build    : Build images"
	@echo "make deploy   : Deploy k8s"
	@echo "make test-bot : Run simulator"
	@echo "make clean    : Remove resource"

