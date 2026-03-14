# Cloud Native SRE Project

This project simulates a cloud-native microservices system with a focus on SRE (Site Reliability Engineering) automation. It includes auto-scaling, self-healing bots, and observability tools.

## System Components

- **Services**: 7 microservices (auth, cart, notification, order, payment, product, user) built with Python.
- **SRE Bot**: Knative functions for automated remediation (restarting services, clearing cache).
- **Messaging**: RabbitMQ for asynchronous communication.
- **Data**: Postgres for persistence and Redis for caching.
- **Observability**: Prometheus and Grafana for metrics and visualization.

## Project Structure

```text
/services           - Microservice source code
/knative_functions  - SRE bot automation scripts
/deploy             - Kubernetes manifests and helm charts
/database           - SQL migrations and init scripts
/sre                - SLO/SLI configs and alerting rules
/tests              - Load tests and SRE simulators
```

## Getting Started

### 1. Build & Deploy
Use the provided Makefile to build and deploy everything:

```bash
# Build all docker images
make build

# Deploy to Kubernetes
make deploy
```

### 2. Monitoring
Access Grafana to view the system health and SLO dashboards:
- URL: `http://localhost:3000` (after port-forwarding)

### 3. SRE Automation
The SRE bot in `knative_functions/sre-bot` is triggered by Prometheus alerts to perform self-healing actions.

## Testing

Run the local simulator to verify the bot logic:
```bash
make test
```

For load testing:
```bash
bash tests/load-test/load_test.sh http://localhost:80/orders 60
```
