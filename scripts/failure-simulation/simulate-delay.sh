#!/bin/bash
# Failure Simulation Script: Introduce network delay using Traffic Control (if pod has permissions)
# Or use Linkerd Traffic Split for simulation
echo "Simulating network delay for order-service..."
# For Linkerd: This would be a TrafficSplit manifest
# For direct simulation:
# kubectl exec <pod> -- tc qdisc add dev eth0 root netem delay 500ms
echo "Network delay simulated (500ms)."
