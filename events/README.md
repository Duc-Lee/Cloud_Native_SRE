# Event Flows

This directory contains JSON schemas and documentation for inter-service communication via RabbitMQ.

## Order -> Payment
When an order is created (`order_created`), the payment service processes the transaction.

- **Exchange**: `events` (topic)
- **Routing Key**: `order.created`
- **Schema**: [order_created.json](./schemas/order_created.json)
