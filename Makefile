# SRE Project Makefile

# Build docker images for all services
build:
	docker build -t auth-service:latest services/auth
	docker build -t cart-service:latest services/cart
	docker build -t notification-service:latest services/notification
	docker build -t order-service:latest services/order
	docker build -t payment-service:latest services/payment
	docker build -t product-service:latest services/product
	docker build -t user-service:latest services/user
	docker build -t sre-bot-remedian:latest knative_functions/sre-bot

# Deploy system to Kubernetes
deploy:
	kubectl apply -f deploy/kubernetes/
	kubectl apply -f deploy/kubernetes/knative-service.yaml

# Run the SRE simulator script
test:
	export PYTHONPATH="knative_functions/sre-bot" && python tests/simulator_sre.py

# Cleanup all k8s resources
clean:
	kubectl delete -f deploy/kubernetes/
	kubectl delete -f deploy/kubernetes/knative-service.yaml

# Help command for quick reference
help:
	@echo "Commands:"
	@echo "  make build   - Build all docker images"
	@echo "  make deploy  - Apply k8s manifests"
	@echo "  make test    - Run SRE bot simulator"
	@echo "  make clean   - Remove all k8s resources"

