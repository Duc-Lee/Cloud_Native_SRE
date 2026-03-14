### Error Rate (5xx)
1. Check `app` label in alert.
2. Logs: `kubectl logs -l app=<app-name>`
3. Check PostgreSQL connection pooling.
4. Rollback: `kubectl rollout undo deployment/<app-name>`

### High Latency
1. Check CPU limits.
2. Check slow Postgres queries or RabbitMQ lag.
3. Scale: `kubectl scale deployment <app-name> --replicas=<count>`

### Service Down
1. Status: `kubectl get pods -l app=<app-name>`
2. Check OOMKill or config issues.
3. Check Nginx gateway routing.
