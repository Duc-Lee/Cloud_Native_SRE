# Cloud Native SRE (CN-SRE) Platform

Hệ thống giả lập môi trường Microservices chuẩn Cloud Native phục vụ nghiên cứu và triển khai các giải pháp SRE (Site Reliability Engineering) tự động hóa. Dự án tập trung vào việc xử lý các kịch bản thực tế về Self-healing, Traffic Scaling và giám sát SLO/SLI.

## 1. Kiến trúc hệ thống
Hệ thống bao gồm 8 microservices chính được viết trên nền tảng Python (FastAPI):
- **Core Services**: `auth`, `user`, `product`, `cart`.
- **Transaction Services**: `order`, `payment`, `notification`.
- **SRE Bot**: Thành phần remediation (Knative) tự động xử lý sự cố.
- **Infrastucture**: Postgres (persistence), Redis (cache), RabbitMQ (event bus).

## 2. Hướng dẫn triển khai
Dự án hỗ trợ triển khai nhanh qua Makefile.

### Local Development (Docker Compose)
1. Copy cấu hình mẫu: `cp .env.example .env`
2. Build & Up:
   ```bash
   make build
   docker-compose up -d
   ```

### Kubernetes (Production-ready)
Triển khai lên Cluster k8s (yêu cầu kubectl đã cấu hình):
```bash
make deploy
```
*Note: Ingress đã cấu hình Basic Auth (`leanhduc` / `anhdc2005`) để bảo vệ gateway.*

## 3. SRE Automation & Testing
Thành phần `sre-bot` trong `knative_functions` sẽ lắng nghe tín hiệu từ Prometheus để thực hiện các hành động tự chữa lành (remediation):
- **Restart service**: Dùng khi hệ thống bị treo hoặc lỗi pod.
- **Flush cache**: Dùng khi dữ liệu cache bị lỗi thời hoặc tràn.
- **Auto-scale**: Tự động tăng pod cho service `payment` khi có burst traffic.

Chạy simulator để verify logic bot:
```bash
make test-sre
```

## 4. Cấu trúc thư mục
- `/services`: Source code của các microservices.
- `/deploy`: Toàn bộ K8s manifests (Secret, Deployment, Ingress).
- `/knative_functions/sre-bot`: Logic xử lý của bot tự động hóa.
- `/tests`: Các kịch bản load test và simulator.

---
**Maintainer**: SRE Project Team
**Contact**: support@sre-project.io
