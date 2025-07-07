

# Architecture Overview

This project sets up a complete observability and infrastructure stack tailored for DevOps, SREs, and platform engineers. It combines logging, metrics, monitoring, automation, and CI/CD over a Kubernetes-based environment.

## Components & Data Flow

1. **Log Pipeline**  
   - **Producer (Python)**: Sends JSON-formatted logs to Kafka topics.  
   - **Kafka**: Acts as a message queue to decouple log ingestion and processing.  
   - **Consumer (Python)**: Reads messages from Kafka, enriches them, and forwards to Elasticsearch.

2. **Elastic Stack**  
   - **Elasticsearch**: Stores and indexes logs.  
   - **Kibana**: Visualizes logs via dashboards.  
   - **Fleet Server + Elastic Agent**: Collects metrics and logs from hosts and containers.

3. **Monitoring**  
   - **Prometheus**: Scrapes metrics from services.  
   - **Blackbox Exporter**: Tests uptime and HTTP/TCP responsiveness.

4. **Automation**  
   - **Ansible**: Automates RHEL patching and agent installation.  
   - **Terraform**: Provisions cloud infrastructure (e.g., EKS).  
   - **GitHub Actions**: Lints, tests, and validates changes before deployment.

## Deployment Models

- **Docker Compose** for local testing of Kafka and ELK.
- **Kubernetes/Minikube/OpenShift** for full distributed deployment.
- **Podman + kube** for hybrid, container-native alternatives.

## Future Extensions

- Add OpenTelemetry Collector for tracing.
- Integrate Grafana for unified metrics visualization.
- Introduce Kafka Dead Letter Queue (DLQ) support.
- Expand Terraform to provision observability tooling.
