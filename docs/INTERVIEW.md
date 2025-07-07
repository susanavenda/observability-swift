# Interview Preparation Guide

This document includes commonly asked questions, technical theory, and concepts relevant for DevOps, SRE, and Observability Engineering interviews.

## General Observability Questions
- What is observability? How is it different from monitoring?
  - Observability is the ability to understand the internal state of a system based on its external outputs. Monitoring typically involves collecting and displaying predefined metrics, while observability includes logs, metrics, and traces to diagnose unknown issues.
- Explain the three pillars of observability: logs, metrics, and traces.
  - Logs provide detailed event records, metrics offer numerical data over time, and traces track the flow of requests across services to diagnose performance bottlenecks.
- What is OpenTelemetry? How does it relate to observability?
  - OpenTelemetry is an open-source project that provides standardized APIs and SDKs for collecting telemetry data (logs, metrics, traces) to improve observability across distributed systems.

## Logging and ELK
- Describe the components of the ELK stack.
  - ELK stands for Elasticsearch (search and analytics engine), Logstash (data processing pipeline), and Kibana (visualization tool).
- How do you ingest logs into Elasticsearch?
  - Logs can be ingested via Logstash pipelines, Beats agents, or Elasticsearch APIs.
- What is the purpose of Logstash? Can it be replaced?
  - Logstash processes and transforms log data before indexing it into Elasticsearch. It can be replaced by other ingestion tools like Fluentd or directly using Beats depending on use case.

## Kafka & Stream Processing
- What is Kafka used for in a logging pipeline?
  - Kafka acts as a distributed messaging system to buffer and transport logs reliably between producers and consumers.
- What is the difference between a Kafka Producer and Consumer?
  - Producers send data to Kafka topics; consumers read data from these topics.
- How do Kafka Connect and Kafka Streams differ?
  - Kafka Connect is used for integrating Kafka with external systems (data sources/sinks), while Kafka Streams is a client library for processing and analyzing data in Kafka.

## Prometheus & Monitoring
- What is the Blackbox Exporter?
  - It is a Prometheus exporter that probes endpoints over HTTP, HTTPS, DNS, TCP, etc., to monitor their availability and responsiveness.
- How does Prometheus perform service discovery and scraping?
  - Prometheus uses service discovery mechanisms (like Kubernetes, Consul) to find targets and scrapes metrics endpoints at configured intervals.
- How would you alert on endpoint downtime using Prometheus?
  - By defining alerting rules that trigger when metrics (e.g., probe success) indicate an endpoint is unreachable for a certain duration.

## Elastic Agent & Fleet
- What is Fleet in the Elastic ecosystem?
  - Fleet is a centralized management system for Elastic Agents, enabling easy deployment, configuration, and monitoring.
- How do you enroll agents into Fleet?
  - Agents are enrolled by providing a Fleet Server URL and enrollment token during agent installation.
- What are advantages of Elastic Agent over legacy Beats?
  - Elastic Agent consolidates multiple Beats into a single agent with unified management and security features.

## GitOps & CI/CD
- What is GitOps? How does it differ from traditional CI/CD?
  - GitOps uses Git as the single source of truth for declarative infrastructure and application deployments, enabling automated, auditable, and version-controlled delivery. Traditional CI/CD may rely more on imperative scripts and manual steps.
- Explain your experience with GitHub Actions or other pipelines.
  - [Add personal experience here]
- How do you manage secrets in CI/CD workflows?
  - Secrets are stored securely using encrypted secrets managers or vaults and injected into pipelines at runtime without exposing them in logs or code.

## Ansible & Automation
- What is Ansible used for in a DevOps environment?
  - Ansible automates configuration management, application deployment, and task orchestration using simple YAML playbooks.
- How would you patch a RHEL system using Ansible?
  - By writing a playbook that uses the `yum` or `dnf` module to update packages on RHEL hosts.
- How do you handle idempotency in Ansible playbooks?
  - By using modules that ensure desired state without causing changes if the system is already compliant.

## Kubernetes & Terraform
- Describe how you would deploy an app to Kubernetes.
  - Create deployment manifests or Helm charts defining pods, services, and other resources, then apply them using `kubectl` or CI/CD pipelines.
- What is the purpose of Helm charts?
  - Helm charts package Kubernetes resources and configurations to simplify deployment and management of applications.
- How do you provision cloud infrastructure using Terraform?
  - Write declarative Terraform configuration files describing resources, then apply them to create and manage infrastructure in a reproducible way.

## Security & Governance
- How do you secure Elasticsearch and Kibana?
  - Enable authentication and authorization, use TLS encryption, restrict network access, and audit logs.
- What is RBAC and how is it configured in Kubernetes?
  - Role-Based Access Control (RBAC) restricts user permissions by defining roles and binding them to users or groups.
- How do you manage secrets across different environments?
  - Use secret management tools like HashiCorp Vault or Kubernetes Secrets with proper access controls and encryption.

---
Prepared by Susana Venda as part of the observability-swift portfolio project.