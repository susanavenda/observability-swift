# SECURITY.md

## 🔐 Security Practices for Observability-Swift

This document outlines the security practices adopted in the `observability-swift` project, especially for handling sensitive data, infrastructure, and monitoring stack integrity.

---

## 1. Access Control

- RBAC (Role-Based Access Control) is used in Kubernetes to restrict user access.
- Limit write access to Elasticsearch indices to specific roles.
- GitHub repository is protected with branch protections and required reviews.

## 2. Secrets Management

- Use Kubernetes secrets (encrypted at rest) for:
  - Kafka credentials
  - Elastic Agent API keys
  - Prometheus targets
- Optionally integrate with external secret managers (e.g., HashiCorp Vault or AWS Secrets Manager).

## 3. Network Policies

- Limit internal traffic using Kubernetes NetworkPolicies.
- Only allow ingress to exposed services (e.g., Kibana, Prometheus UI) via specific ports.

## 4. Audit & Logging

- Enable audit logging in Kubernetes and Elasticsearch.
- Use Elastic Agent to monitor changes and detect anomalies.

## 5. CI/CD Hardening

- GitHub Actions use OIDC-based secrets (no hardcoded credentials).
- All workflows validate inputs and enforce branch protections.

## 6. Infrastructure Security

- Terraform state files are stored securely (encrypted backend).
- Only admin users can modify infrastructure modules.

## 7. System Patching

- Ansible automates RHEL patching monthly.
- Fleet monitors outdated packages and OS version compliance.

## 8. Dependency Scanning

- Python dependencies are scanned using `pip-audit`.
- Docker images are scanned with `trivy`.

## 9. Alerts

- Prometheus alerts on service downtime and unusual metrics.
- Elastic Security and Kibana detect potential breaches or abuse.

## 10. User Authentication

- Enable SSO for Kibana and Prometheus via OIDC or LDAP.
- Enforce 2FA in GitHub and any hosted dashboards.

---

Always follow the principle of least privilege and proactively monitor the stack.
