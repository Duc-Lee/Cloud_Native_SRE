# Cloud Native SRE (CN-SRE) Platform

Hệ thống giả lập môi trường Microservices chuẩn Cloud Native phục vụ nghiên cứu và triển khai các giải pháp SRE (Site Reliability Engineering) tự động hóa. Dự án tập trung vào việc xử lý các kịch bản thực tế về Self-healing, Traffic Scaling và giám sát SLO/SLI.

## 1. Bài toán 
Trong các hệ thống Microservices hiện đại, việc duy trì tính sẵn sàng (Availability) và độ tin cậy (Reliability) đối mặt với nhiều thách thức:
- **Độ phức tạp cao**: Khó khăn trong việc phát hiện và cô lập lỗi giữa hàng chục service liên kết với nhau.
- **Phản ứng chậm**: Việc xử lý sự cố thủ công (manual remediation) thường gây trễ, ảnh hưởng đến trải nghiệm người dùng và vi phạm cam kết chất lượng (SLA/SLO).
- **Lãng phí tài nguyên**: Thiếu cơ chế tự động mở rộng (scaling) linh hoạt dựa trên tải thực tế, dẫn đến việc cấp phát tài nguyên không tối ưu.

## 2. Giải pháp 
Dự án đề xuất mô hình **CN-SRE Platform** tích hợp cơ chế tự động hóa:
- **Self-healing (Tự chữa lành)**: Sử dụng các `sre-bot` (Knative Functions) để tự động restart service hoặc dọn dẹp cache ngay khi phát hiện lỗi từ hệ thống giám sát.
- **Dynamic Scaling**: Tự động điều chỉnh số lượng Pod dựa trên lưu lượng giao dịch thực tế để đảm bảo hiệu năng tối ưu.
- **Observability**: Triển khai đầy đủ hệ thống giám sát SLO/SLI giúp minh bạch hóa trạng thái sức khỏe của toàn bộ Platform.

## 3. Kiến trúc hệ thống
Hệ thống bao gồm 8 microservices chính được viết trên nền tảng Python (FastAPI):
- **Core Services**: `auth`, `user`, `product`, `cart`.
- **Transaction Services**: `order`, `payment`, `notification`.
- **SRE Bot**: Thành phần remediation (Knative) tự động xử lý sự cố.
- **Infrastucture**: Postgres (persistence), Redis (cache), RabbitMQ (event bus).

## 4. Hướng dẫn triển khai
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

## 5. SRE Automation & Testing
Thành phần `sre-bot` trong `knative_functions` sẽ lắng nghe tín hiệu từ Prometheus để thực hiện các hành động tự chữa lành (remediation):
- **Restart service**: Dùng khi hệ thống bị treo hoặc lỗi pod.
- **Flush cache**: Dùng khi dữ liệu cache bị lỗi thời hoặc tràn.
- **Auto-scale**: Tự động tăng pod cho service `payment` khi có burst traffic.

Chạy simulator để verify logic bot:
```bash
make test-sre
```

## 6. Cấu trúc thư mục
- `/services`: Source code của các microservices.
- `/deploy`: Toàn bộ K8s manifests (Secret, Deployment, Ingress).
- `/knative_functions/sre-bot`: Logic xử lý của bot tự động hóa.
- `/tests`: Các kịch bản load test và simulator.
