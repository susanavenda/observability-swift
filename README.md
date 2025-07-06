# observability-swift
# FullStack Observability Pipeline

A complete observability and infrastructure automation stack that simulates a real-world production environment for DevOps and SRE workflows. This project includes **Kafka**, **Elastic Stack (Elasticsearch, Kibana, Fleet, Elastic Agent)**, **Prometheus + Blackbox Exporter**, **Ansible**, **Terraform**, and **GitHub Actions CI/CD**, all running on Kubernetes.

This setup is ideal for preparing for interviews, testing distributed systems, and demonstrating expertise across logging, metrics, monitoring, automation, and Infrastructure-as-Code.

---

## Project Mission

To build and operate a **resilient, observable, and automated platform** that:
- Ingests logs via **Kafka**
- Processes logs with a **Python consumer**
- Ships logs to **Elasticsearch**
- Visualizes data in **Kibana**
- Monitors services with **Prometheus + Blackbox**
- Automates patching with **Ansible**
- Uses **CI/CD pipelines** for testing and validation
- Manages infrastructure via **Terraform**

---

## Stack Overview

| Component         | Purpose                                         |
|------------------|-------------------------------------------------|
| **Kafka**         | Ingest logs and decouple producers/consumers   |
| **Producer**      | Python app sending JSON logs to Kafka          |
| **Consumer**      | Python app enriching and forwarding logs       |
| **Elasticsearch** | Central storage and indexing of logs           |
| **Kibana**        | Dashboards and visualization                   |
| **Fleet/Elastic Agent** | System and container monitoring       |
| **Prometheus + Blackbox** | Synthetic uptime and endpoint checks |
| **Ansible**       | RHEL patching automation                       |
| **Terraform**     | Provisioning Kubernetes/EKS infrastructure     |
| **GitHub Actions**| CI/CD for linting, testing, and deployment     |

---

## Project Structure
observability-pipeline/
├── ansible/                  # RHEL patching role and playbook
├── kafka/                   # Producer and consumer in Python
├── elastic/                 # Fleet server, agent, dashboards
├── monitoring/              # Prometheus Blackbox configuration
├── terraform/               # Terraform configs (EKS, K8s)
├── .github/workflows/       # GitHub Actions CI/CD pipeline
├── docs/                    # Interview prep, architecture, security
└── README.md

---

## 🚀 Setup Guide

### 1️⃣ Start Kafka and Run Log Pipeline
- Deploy Kafka locally (Docker/Bitnami) or on K8s (Strimzi)
- Run `kafka/producer/producer.py` to send logs
- Run `kafka/consumer/consumer.py` to consume and enrich logs

### 2️⃣ Deploy Elastic Stack
- Use Docker or Helm for Elasticsearch + Kibana
- Deploy Fleet Server and enroll Elastic Agents
- Import dashboards from `elastic/dashboards/`

### 3️⃣ Enable Prometheus Monitoring
- Deploy Prometheus Operator
- Apply `monitoring/blackbox-exporter/blackbox-deploy.yaml`
- Monitor uptime of services like Kafka, ES, Kibana

### 4️⃣ Automate with Ansible
- Use `ansible/playbook.yml` to patch RHEL systems
- Extend to install agents or handle patching logic

### 5️⃣ CI/CD with GitHub Actions
- Triggers on push to `main`
- Lints Python with `flake8`
- Tests consumer with `pytest`

### 6️⃣ Terraform Infrastructure (Optional)
- Use `terraform/eks-module` to provision EKS or K8s
- Use remote state and modules for reusable setup

---

## 📘 Documentation

- `ARCHITECTURE.md`: How all services interact (logs, metrics, CI/CD)
- `GIT_STRATEGY.md`: Branching, pull request, and release strategy
- `SECURITY.md`: RBAC, access control, and secret handling
- `INTERVIEW.md`: Sample interview questions and theory

---

## ✅ Use Cases

- Interview and take-home project showcase
- Personal DevOps practice environment
- End-to-end observability pipeline simulation
- Logging and metric testing in Kubernetes

---

## 💡 Bonus Ideas

- Add OTEL for traces and span correlation
- Add a DLQ to Kafka consumer
- Add custom Kibana alerts
- Integrate Grafana for Prometheus metrics

---

## Author

Created by Susana Venda a DevOps engineer preparing for advanced platform engineering and observability roles. Inspired by real-world use cases from Elastic, and SRE best practices.
